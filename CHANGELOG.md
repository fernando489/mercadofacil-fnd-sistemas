# Changelog

## [1.0.0] — 2026-11-09 — Profissionalização da demonstração
### Organização
- Projeto reorganizado em `frontend/`, `docs/`, `tests/`, `tools/`; três versões divergentes da loja unificadas em uma.
- Páginas renomeadas: `teste.html`→`index.html` (boas-vindas), `index.html`→`loja.html`.
- `admin.js` + `admin-extra.js` sem funções duplicadas (`admin-core.js` + `admin-extra.js`).
- `shop.js` (órfão, nunca carregado) removido; `otimizar.py` substituído por `tools/otimizar_imagens.py`, que não sobrescreve originais.
### Correções
- Busca e categoria agora funcionam juntas; categorias geradas do catálogo.
- Escape de HTML na loja (risco de XSS com dados importados).
### Novidades
- Faixa de demonstração, contato FND, restaurar dados de exemplo, rodapé de imagens ilustrativas.
- Carrinho persistente com ajuste de quantidade; exclusão de produto; envio de foto no admin.
- Layout responsivo, acessibilidade básica, imagens sob demanda.
- Ortografia do catálogo (Água Sanitária, Fubá, Hambúrguer, Loção, Papel Higiênico, Ração, Sabão em Pó, Comedouro).
- Publicação automática no GitHub Pages; documentação completa; testes automatizados.
### Preservado
- 41 fotografias originais (idênticas por hash), catálogo, preços, categorias, regras de estoque/pedido, chaves de `localStorage` e formato de importação.
