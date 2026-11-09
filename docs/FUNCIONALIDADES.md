# Funcionalidades (somente o que existe e foi verificado)

## Loja (`loja.html`)
- Carrossel de 3 banners (setas, pontos, troca automática; não anda sozinho com "movimento reduzido").
- Catálogo com foto, categoria, preço e botão Adicionar; produto sem estoque mostra "Esgotado".
- Busca por nome **combinada** com filtro de categoria; categorias geradas do catálogo.
- Seletor de quantidade por produto e validação contra o estoque.
- Carrinho em janela própria, com − e + por item, remoção e total; **persiste ao recarregar**.
- Checkout: nome, bloco/apartamento e telefone. Baixa o estoque, registra o pedido (status "Novo") e confirma com o número.
- Faixa de demonstração, contato por WhatsApp, restaurar dados de exemplo e rodapé de imagens ilustrativas.

## Painel administrativo (`admin.html`)
- Login com senha da demo (a senha é pública; não há segurança real no navegador).
- Indicadores: pedidos e vendas do dia, produtos com estoque baixo (≤ 5).
- **Pedidos:** filtro por data, mudança de status (Novo, Em separação, Concluído, Cancelado), impressão de comanda individual ou de todas.
- **Produtos e estoque:** cadastro, edição, exclusão com confirmação, ativar/ocultar, ajuste rápido de estoque (salva ao sair do campo), envio de foto (reduzida a 500 px e guardada no navegador).
- **Atualizar loja por arquivo:** importa `.xlsx`, `.xml` ou `.csv` (colunas aceitas em português ou inglês); exporta o catálogo em CSV; restaura o catálogo padrão (mantém os pedidos).

## Não existe (não é prometido)
Pagamento, login de clientes, envio de pedidos para outro computador, banco de dados, controle de acesso real, relatórios históricos, hortifrúti/açougue/padaria no catálogo inicial.
