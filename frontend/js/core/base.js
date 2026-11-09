const $=s=>document.querySelector(s);const money=n=>Number(n).toLocaleString('pt-BR',{style:'currency',currency:'BRL'});const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const KEY='mercado_demo_produtos_v2', ORDERKEY='mercado_demo_pedidos_v1';
function getProducts(){try{const v=JSON.parse(localStorage.getItem(KEY));if(Array.isArray(v)&&v.length)return v}catch{}return INITIAL_PRODUCTS}
function saveProducts(v){localStorage.setItem(KEY,JSON.stringify(v))}
function getOrders(){try{return JSON.parse(localStorage.getItem(ORDERKEY))||[]}catch{return []}}
function saveOrders(v){localStorage.setItem(ORDERKEY,JSON.stringify(v))}
// Caminho seguro da imagem (espaços/acentos codificados; sem extensão => .jpg; .jfif => .jpg)
function imgSrc(name){if(!name)return '';if(/^(data:|https?:)/i.test(name))return name;let n=String(name).trim().replace(/\.jfif$/i,'.jpg');if(!/\.(jpe?g|png|webp|gif)$/i.test(n))n+='.jpg';return 'assets/images/products/'+encodeURIComponent(n)}
const hoje=(d=new Date())=>d.toLocaleDateString('sv');
