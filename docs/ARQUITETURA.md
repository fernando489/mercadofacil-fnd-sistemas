# Arquitetura

Aplicação **estática**: HTML + CSS + JavaScript puro, sem servidor. Todo o estado fica no navegador.

## Páginas
| Arquivo | Papel | Scripts carregados |
|---|---|---|
| `frontend/index.html` | Boas-vindas (escolha loja ou admin) | `config.js` |
| `frontend/loja.html` | Loja do cliente (script embutido na página) | `config.js`, `dados.js`, `base.js` |
| `frontend/admin.html` | Painel administrativo | `config.js`, `dados.js`, `base.js`, `admin-core.js`, `admin-extra.js` |

## Módulos JavaScript
- `js/core/config.js`: dados da empresa, senha da demo, chaves de armazenamento; injeta a faixa de demonstração, o botão de contato, o botão "Restaurar dados de exemplo" e o rodapé.
- `js/core/dados.js`: catálogo inicial (`INITIAL_PRODUCTS`, 41 produtos).
- `js/core/base.js`: utilitários (`$`, `money`, `esc`), leitura/gravação no `localStorage` (`getProducts`, `saveProducts`, `getOrders`, `saveOrders`) e `imgSrc` (caminho seguro da imagem).
- `js/admin/admin-core.js`: login, abas, formulário de produto, upload de foto, leitura de CSV.
- `js/admin/admin-extra.js`: pedidos do dia, comandas, estoque rápido, exclusão, importação Excel/XML/CSV, exportação e restauração.
- `loja.html` (script interno): carrossel, filtros, carrinho, checkout.

`admin-core.js` e `admin-extra.js` compartilham variáveis globais (`products`, `orders`). `admin-extra.js` **deve carregar depois** do core, pois define `refresh`, `renderOrders` e `renderProducts`.

## Fluxo de dados
```
dados.js (INITIAL_PRODUCTS) ──┐
                              ├─> getProducts() ─> loja / admin
localStorage (produtos v2) ───┘      ▲
loja: finalizar pedido ──> saveProducts (baixa estoque) + saveOrders
admin: editar/importar ──> saveProducts      admin: status ──> saveOrders
```
Se não houver dados no `localStorage` (ou o catálogo for apagado), usa-se `INITIAL_PRODUCTS`. Loja e admin só compartilham dados quando abertos **na mesma origem** (mesmo endereço), como no GitHub Pages ou em `localhost`.

## Imagens
`frontend/assets/images/products/*.jpg` (41 fotos). O campo `image` do produto guarda o nome do arquivo ou, para fotos enviadas pelo admin, um `data:image/jpeg;base64,...`. Imagens carregam com `loading="lazy"`.

## Decisões
- **Sem backend:** a demonstração não precisa; GitHub Pages só serve arquivos estáticos e **não executa Python**. Ver `BANCO_DE_DADOS.md` para a evolução.
- **Catálogo em `.js` e não `.json`:** permite abrir por duplo clique (sem servidor), o que `fetch` de JSON impediria.
- **Sem frameworks:** o código existente já resolve tudo com JavaScript puro; um framework só aumentaria a manutenção.
