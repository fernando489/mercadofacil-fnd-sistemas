"""Gera versões WebP em frontend/assets/images/products/webp/. NUNCA altera os JPGs originais.
Requer: pip install pillow"""
import os
from PIL import Image
ORIG = os.path.join(os.path.dirname(__file__), '..', 'frontend', 'assets', 'images', 'products')
DEST = os.path.join(ORIG, 'webp'); os.makedirs(DEST, exist_ok=True)
for nome in sorted(os.listdir(ORIG)):
    if nome.lower().endswith('.jpg'):
        im = Image.open(os.path.join(ORIG, nome)).convert('RGB'); im.thumbnail((400, 400))
        im.save(os.path.join(DEST, nome[:-4] + '.webp'), quality=85); print('ok', nome)
