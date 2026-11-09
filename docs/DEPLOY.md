# Publicação gratuita (GitHub Pages)

O repositório já inclui `.github/workflows/pages.yml`, que publica a pasta `frontend/` a cada envio para a branch `main`.

## Primeira publicação
1. Crie uma conta e um repositório novo em https://github.com (ex.: `mercadofacil`). Páginas de repositório público são gratuitas; para repositório privado confira o plano vigente do GitHub.
2. Na pasta do projeto:
```bash
git init -b main
git add .
git commit -m "MercadoFácil v1.0.0 (demonstração)"
git remote add origin https://github.com/SEU_USUARIO/mercadofacil.git
git push -u origin main
```
3. No GitHub: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
4. Abra a aba **Actions** e aguarde o fluxo "Publicar no GitHub Pages" ficar verde.
5. O link será `https://SEU_USUARIO.github.io/mercadofacil/`. Todos os caminhos são relativos, então funciona nesse subendereço.

## Atualizar
```bash
git add . && git commit -m "descreva a mudança" && git push
```
Em ~1 minuto o site é atualizado. O histórico fica no GitHub; marque versões com `git tag v1.1.0 && git push --tags`. Para voltar a uma versão: `git revert <commit>` e `git push`.

## Alternativa: Cloudflare Pages (gratuito)
Conecte o repositório em https://dash.cloudflare.com → Workers & Pages → Pages. Comando de build: *(vazio)*; diretório de saída: `frontend`.

## Checklist antes de divulgar
- Trocar WhatsApp/e-mail em `frontend/js/core/config.js`.
- Conferir `docs/CREDITOS_IMAGENS.md`.
- Abrir o link no celular e testar uma compra e o painel admin.
- Opcional: remover `docs/original/entrega_original.zip` do repositório público (ele só serve como arquivo histórico).

## Limitações da hospedagem estática
Sem Python, sem banco, sem pedidos centralizados. Cada visitante vê apenas os próprios dados (ver `BANCO_DE_DADOS.md`).
