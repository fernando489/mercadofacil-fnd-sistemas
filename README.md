# MercadoFácil — demonstração da FND Sistemas

Minimercado autônomo para condomínios: loja para o cliente, painel administrativo, estoque e pedidos.
Esta versão é uma **demonstração pública**: roda 100% no navegador, sem servidor e sem banco de dados.
Produtos e pedidos são fictícios, ficam no navegador de cada visitante e **nenhuma compra ou cobrança é real**.

## Como executar localmente
1. Baixe/extraia o projeto.
2. Abra `frontend/index.html` com duplo clique **ou**, na pasta `frontend/`, rode `python3 -m http.server 8000` e acesse `http://localhost:8000`.
3. Painel admin: botão "Admin" na loja ou `frontend/admin.html`. Senha da demonstração: `admin123` (pública, sem proteção real).

## Tecnologias (todas reais no projeto)
| Tecnologia | Finalidade | Documentação oficial |
|---|---|---|
| HTML5 | Estrutura das 3 páginas | https://developer.mozilla.org/docs/Web/HTML |
| CSS3 | Visual e responsividade | https://developer.mozilla.org/docs/Web/CSS |
| JavaScript (ES2020, sem framework) | Loja, carrinho, admin, importação | https://developer.mozilla.org/docs/Web/JavaScript |
| Web Storage (`localStorage`/`sessionStorage`) | Persistência da demo | https://developer.mozilla.org/docs/Web/API/Web_Storage_API |
| `DecompressionStream` + `DOMParser` | Leitura de `.xlsx`/`.xml` sem bibliotecas | https://developer.mozilla.org/docs/Web/API/DecompressionStream |
| GitHub Pages + GitHub Actions | Hospedagem gratuita estática | https://docs.github.com/pages |
| Python 3 + Pillow *(opcional)* | `tools/otimizar_imagens.py` | https://pillow.readthedocs.io |
| Playwright + Python *(só para testes)* | `tests/*.py` | https://playwright.dev/python |

Não há `package.json`, build, framework nem dependências de execução. Versões: o projeto não fixa versões de bibliotecas porque não usa nenhuma; os testes foram executados com Playwright 1.63 (Chromium).

## Estrutura
```
frontend/   site publicado (index, loja, admin, css, js, assets, data)
docs/       documentação e a entrega original preservada (docs/original/)
tests/      testes automatizados e checklist manual
tools/      utilitários (otimização de imagens, não destrutiva)
.github/    publicação automática no GitHub Pages
```
Documentação: [Arquitetura](docs/ARQUITETURA.md) · [Funcionalidades](docs/FUNCIONALIDADES.md) · [Manual do usuário](docs/MANUAL_USUARIO.md) · [Manual do desenvolvedor](docs/MANUAL_DESENVOLVEDOR.md) · [Banco de dados](docs/BANCO_DE_DADOS.md) · [Deploy](docs/DEPLOY.md) · [Melhorias, comparação e limitações](docs/MELHORIAS_E_COMPARACAO.md) · [Créditos das imagens](docs/CREDITOS_IMAGENS.md) · [Changelog](CHANGELOG.md)

## Antes de publicar
- Troque o WhatsApp e o e-mail provisórios em `frontend/js/core/config.js`.
- Leia `docs/CREDITOS_IMAGENS.md` (origem e licença das fotos).
- Licença do código: **ainda não definida** (não há arquivo `LICENSE` de propósito).
