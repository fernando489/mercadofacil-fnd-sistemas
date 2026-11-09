# Manual do desenvolvedor

## Rodar e testar
```bash
cd frontend && python3 -m http.server 8000          # abrir http://localhost:8000
pip install playwright openpyxl && playwright install chromium
python3 tests/smoke_playwright.py                    # 38 verificações
python3 tests/importacao_playwright.py               # 8 verificações (xlsx/xml/impressão)
for f in frontend/js/*/*.js; do node --check $f; done  # sintaxe
```
Roteiro manual: `tests/CHECKLIST_MANUAL.md`.

## Tarefas comuns
- **Contato da empresa / senha demo:** `frontend/js/core/config.js`.
- **Catálogo inicial:** `frontend/js/core/dados.js` (campos `id, name, category, price, stock, image, active`). Quem já tem dados no navegador só vê a mudança após "Restaurar".
- **Nova foto:** copie o JPG para `frontend/assets/images/products/` com nome em minúsculas e hífens (`leite-integral.jpg`) e registre em `docs/CREDITOS_IMAGENS.md`.
- **Cores:** `frontend/css/base.css` (vermelho `#d41229`) e ajustes responsivos em `css/responsive.css`.
- **Novo campo de produto:** `dados.js`, formulário em `admin.html`, `edit()`/submit em `admin-core.js`, `renderProducts` e importador em `admin-extra.js`, exibição em `loja.html`.

## Cuidados
- Escape todo texto de produto/pedido com `esc()` ao montar HTML (o catálogo pode vir de arquivos importados).
- Mantenha as chaves `mercado_demo_produtos_v2`, `mercado_demo_pedidos_v1`, `mercado_demo_carrinho_v1` (ou migre os dados). Se mudar o formato, crie `..._v3`.
- Mantenha a ordem dos scripts do admin (core antes de extra).
- **Nunca** rode ferramentas que sobrescrevam as fotos originais; `tools/otimizar_imagens.py` grava em `webp/` e é opcional (o site ainda não usa os WebP).
- Compatibilidade: a importação `.xlsx` usa `DecompressionStream` (Chrome/Edge 80+, Firefox 113+, Safari 16.4+, segundo a MDN). Só Chromium foi testado.

## Versionamento
`git commit` a cada mudança, `git tag v1.1.0` nas versões, e registre em `CHANGELOG.md`.
