# Armazenamento de dados

## Atual (demonstração)
Sem banco de dados. Tudo em `localStorage`, por navegador:

| Chave | Conteúdo |
|---|---|
| `mercado_demo_produtos_v2` | lista de produtos `{id, name, category, price, stock, image, active}` |
| `mercado_demo_pedidos_v1` | lista de pedidos `{id, customer, unit, phone, created_at, day, total, status, items:[{id, name, price, qty}]}` |
| `mercado_demo_carrinho_v1` | carrinho `{ "<id>": {nome, preco, qtd} }` |
| `sessionStorage: demo_admin` | marca de login do admin (some ao fechar a aba) |

Limites: ~5 MB por site; dados não são compartilhados entre aparelhos; o visitante pode apagá-los. Fotos enviadas pelo admin ocupam esse espaço.

## Futuro (proposta, **não implementada**)
Se a FND quiser operação real (vários aparelhos, pedidos centralizados) será preciso backend. O GitHub Pages **não executa Python nem acessa banco**; opções compatíveis:
1. **FastAPI + PostgreSQL** em um serviço de hospedagem de aplicações (verifique as condições gratuitas vigentes), com o `frontend/` consumindo a API por `fetch`.
2. **Backend como serviço** (ex.: Supabase, que usa PostgreSQL) chamado direto do frontend estático, com autenticação e regras de acesso do próprio serviço.

Esquema sugerido: `produtos(id, nome, categoria, preco_centavos, estoque, imagem, ativo)`, `pedidos(id, cliente, unidade, telefone, criado_em, status, total_centavos)`, `itens_pedido(pedido_id, produto_id, nome, preco_centavos, quantidade)`, `usuarios_admin(id, email, senha_hash)`. Valores monetários em centavos inteiros; estoque baixado em transação. O login por senha fixa do admin atual **deve ser substituído** por autenticação real.
