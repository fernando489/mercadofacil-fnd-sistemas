# Manual do usuário

## Cliente (loja)
1. Abra a loja. Use a busca ou os botões de categoria para encontrar produtos.
2. Ajuste a quantidade com **−/+** e toque em **Adicionar**.
3. Abra **Meu carrinho**. Altere quantidades ou remova itens.
4. Preencha nome, bloco/apartamento e telefone e toque em **Finalizar pedido**. Você verá o número do pedido.
5. Na demonstração nada é cobrado nem entregue.

## Administrador
1. Abra **Admin** e entre com a senha da demonstração (`admin123`).
2. **Compras do dia:** escolha a data, altere o status de cada pedido e imprima comandas.
3. **Produtos e estoque:** clique em **+ Novo produto** ou **Editar**; altere o estoque direto na tabela; use **Excluir** para remover (pedidos antigos não mudam).
4. **Foto:** em "Enviar foto real" escolha PNG, JPG ou WebP. Ela fica só neste navegador; para uma foto permanente, coloque o arquivo em `assets/images/products/` e informe o nome no campo de imagem.
5. **Atualizar loja (Excel/XML):** envie a planilha com as colunas id, nome, categoria, preço, estoque, imagem, ativo. Com `id` (ou nome igual) atualiza o produto; sem, cadastra um novo. Modelos em `data/`.

## Problemas comuns
- *Dados sumiram:* os dados ficam neste navegador; limpar dados do site ou usar outro aparelho mostra o catálogo de exemplo.
- *Impressão não abre:* permita pop-ups do site.
- *Quero voltar ao início:* use **Restaurar dados de exemplo** na faixa superior.
