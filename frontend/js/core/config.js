// Configuração da demonstração. EDITE os dados de contato abaixo antes de publicar.
const CONFIG = {
  DEMO: true,
  EMPRESA: 'FND Sistemas',
  WHATSAPP: '5541996546349',            // DDI+DDD+número, só dígitos
  EMAIL: 'contato@fndsistemas.com.br',
  SENHA_DEMO: 'admin123',
  CHAVES: ['mercado_demo_produtos_v2', 'mercado_demo_pedidos_v1', 'mercado_demo_carrinho_v1']
};
function ligarDemo() {
  if (!CONFIG.DEMO) return;
  const msg = encodeURIComponent('Olá! Vi a demonstração do MercadoFácil e gostaria de saber mais.');
  const bar = document.createElement('div');
  bar.className = 'demo-bar'; bar.setAttribute('role', 'note');
  bar.innerHTML = '<span><b>Versão de demonstração</b>: produtos e pedidos fictícios, sem compras nem cobranças reais.</span>' +
    '<span class="demo-actions"><button type="button" id="btn-reset-demo">Restaurar dados de exemplo</button>' +
    `<a id="btn-contato" href="https://wa.me/${CONFIG.WHATSAPP}?text=${msg}" target="_blank" rel="noopener">Fale com a ${CONFIG.EMPRESA}</a></span>`;
  document.body.prepend(bar);
  document.getElementById('btn-reset-demo').onclick = () => {
    if (!confirm('Restaurar produtos, pedidos e carrinho para os dados de exemplo?')) return;
    CONFIG.CHAVES.forEach(k => localStorage.removeItem(k)); location.reload();
  };
  if (!document.body.classList.contains('welcome-page')) {
    const f = document.createElement('footer'); f.className = 'site-footer';
    f.innerHTML = `<p><b>MercadoFácil | ${CONFIG.EMPRESA}</b></p><p>Seu negócio mais perto dos clientes.</p><p><a href="https://wa.me/${CONFIG.WHATSAPP}?text=${msg}" target="_blank" rel="noopener noreferrer">WhatsApp: (41) 99654-6349</a> · <a href="https://fndsistemas.netlify.app/" target="_blank" rel="noopener noreferrer">Site FND Sistemas</a></p><p>Versão demonstrativa: pedidos e pagamentos simulados. Dados armazenados somente neste navegador.</p><p>Imagens ilustrativas; marcas pertencem aos respectivos titulares.</p>`;
    document.body.append(f);
  }
}
document.addEventListener('DOMContentLoaded', ligarDemo);
