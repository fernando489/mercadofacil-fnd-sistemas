"""Testa importação .xlsx/.xml e impressão de comandas. Requer: pip install playwright openpyxl"""
import subprocess, time, os
from openpyxl import Workbook
from playwright.sync_api import sync_playwright
ROOT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','frontend')
srv=subprocess.Popen(['python3','-m','http.server','8791'],cwd=ROOT,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
B='http://localhost:8791/'; res=[]; erros=[]
def ok(n,c): res.append(bool(c)); print('OK   ' if c else 'FALHA',n)
wb=Workbook(); ws=wb.active; ws.append(['id','nome','categoria','preço','estoque','imagem','ativo'])
ws.append([1,'Absorvente','Higiene',12.5,3,'absorvente.jpg',1]); ws.append([None,'Maçã Fuji','Hortifrúti','R$ 7,90',15,'',1]); wb.save('/tmp/imp.xlsx')
open('/tmp/imp.xml','w',encoding='utf-8').write('<?xml version="1.0" encoding="UTF-8"?><produtos><produto><nome>Absorvente</nome><categoria>Higiene</categoria><preco>4,25</preco><estoque>11</estoque><ativo>1</ativo></produto><produto><nome>Pão Francês</nome><categoria>Padaria</categoria><preco>0,90</preco><estoque>100</estoque></produto></produtos>')
try:
  with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(); pg.on('pageerror',lambda e:erros.append(str(e))); pg.on('dialog',lambda d:d.accept())
    pg.goto(B+'admin.html'); pg.evaluate('localStorage.clear()'); pg.reload(); pg.fill('[name=password]','admin123'); pg.click('#loginForm .primary'); pg.click('[data-tab=import]')
    def imp(f): pg.set_input_files('#importForm input[type=file]',f); pg.click('#importForm .primary'); pg.wait_for_timeout(500)
    imp('/tmp/imp.xlsx'); g=pg.evaluate('getProducts()')
    ok('xlsx: atualiza existente (preço 12,5 / estoque 3)', next(x for x in g if x['id']==1)['price']==12.5 and next(x for x in g if x['id']==1)['stock']==3)
    ok('xlsx: cria novo com preço "R$ 7,90"', any(x['name']=='Maçã Fuji' and x['price']==7.9 and x['category']=='Hortifrúti' for x in g))
    imp('/tmp/imp.xml'); g=pg.evaluate('getProducts()')
    ok('xml: atualiza existente (preço 4,25 / estoque 11)', next(x for x in g if x['id']==1)['price']==4.25 and next(x for x in g if x['id']==1)['stock']==11)
    ok('xml: cria novo (Pão Francês, Padaria)', any(x['name']=='Pão Francês' and x['category']=='Padaria' for x in g))
    ok('importação preserva imagem existente', next(x for x in g if x['id']==1)['image']=='absorvente.jpg')
    # pedido + impressão
    pg.evaluate("saveOrders([{id:1,created_at:'hoje',day:hoje(),customer:'Ana',unit:'B2 202',phone:'41999',items:[{id:1,name:'Absorvente',qty:2,price:9.99}],total:19.98,status:'Novo'}])")
    pg.reload(); pg.click('#refreshOrders')
    with pg.expect_popup() as pop: pg.click('[data-print="1"]')
    w=pop.value; w.wait_for_load_state(); ok('imprimir comanda individual abre com dados', 'COMANDA #1' in w.content() and 'Ana' in w.content()); w.close()
    with pg.expect_popup() as pop: pg.click('#printAll')
    w=pop.value; w.wait_for_load_state(); ok('imprimir todas as comandas', 'COMANDA #1' in w.content()); w.close()
    pg.select_option('[data-status="1"]','Concluído'); ok('mudar status do pedido', pg.evaluate('getOrders()[0].status')=='Concluído')
    b.close()
finally: srv.terminate()
print('erros JS:',erros or 'nenhum'); print(f'{sum(res)}/{len(res)} OK')
