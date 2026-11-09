# Melhorias, comparação original × final e limitações

## Comparação
| Aspecto | Original | Final (v1.0.0) |
|---|---|---|
| Arquivos de código | 3 versões da loja (multi-arquivo, `loja_unica` ×2 divergentes) + `admin_unico` + `shop.js` órfão | 1 versão organizada em `frontend/` |
| Admin | 2 scripts com 4 funções duplicadas | `admin-core.js` + `admin-extra.js` sem duplicidade |
| Fotos | 41 reais | **as mesmas 41, idênticas por hash** |
| Busca × categoria | uma ignorava a outra | combinadas |
| Categorias na loja | 5 botões fixos | geradas do catálogo |
| Segurança de HTML | nome/categoria/imagem sem escape na loja | escapados |
| Carrinho | só em memória, sem alterar quantidade | persistente, com − e + |
| Produtos | cadastrar/editar (sem excluir) | + excluir com confirmação |
| Foto no admin | só um aviso para copiar o arquivo | reduz e guarda a foto no navegador |
| Demonstração | sem aviso, contato nem restauração para o visitante | faixa, WhatsApp, restaurar, rodapé |
| Celular | 1 regra responsiva (só boas-vindas) | loja e admin responsivos (360–1280 px) |
| Acessibilidade | carrinho em `div`, sem rótulos, sem foco | botões, rótulos, foco, Esc, movimento reduzido |
| Imagens | todas carregadas de imediato | `loading="lazy"` |
| Publicação | manual | GitHub Pages automático |
| Documentação | LEIA-ME de 6 linhas | 10 documentos |
| Testes | nenhum | 46 verificações automatizadas + checklist |
| `otimizar.py` | sobrescrevia as fotos | `tools/otimizar_imagens.py`, não destrutivo |

## Verificado (Chromium, Playwright 1.63)
`smoke_playwright.py` 38/38 e `importacao_playwright.py` 8/8, sem erros de JavaScript: loja, filtros, carrinho, pedido e estoque, XSS, admin (login, editar, criar, excluir, foto, CSV, XLSX, XML), impressão de comandas, restauração e ausência de rolagem horizontal em 360/390/768/1280 px.

## Não verificado
Firefox e Safari/WebKit (não instalados no ambiente de teste), toque em aparelho real, leitores de tela, desempenho medido (Lighthouse).

## Limitações
- Demonstração sem backend: dados por navegador, não compartilhados; senha `admin123` pública e sem proteção real.
- Fotos enviadas pelo admin ficam só no navegador (limite ~5 MB do `localStorage`).
- Catálogo continua com 41 itens e 5 categorias; sem hortifrúti, açougue e padaria (sem fotos novas disponíveis; o ambiente não tinha internet).
- Fotos: 8 com resolução menor; fonte individual não registrada; `LICENSE` do código não definida.
- Contato (WhatsApp/e-mail) provisório. Categorias do catálogo original mantidas como estavam (ex.: Coca e Leite em Mercearia, Batata Frita congelada em Mercearia).
- `tools/otimizar_imagens.py` gera WebP, mas o site ainda não os usa.

## Funcionalidades futuras sugeridas
Backend + banco (ver `BANCO_DE_DADOS.md`) com login real; pedidos centralizados e notificação; WebP/`srcset`; novas categorias com fotos; relatórios; PWA; revisão das categorias; definição de licença.
