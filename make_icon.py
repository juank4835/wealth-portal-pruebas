"""Genera apple-touch-icon.png 180x180 — versión PRUEBAS.

Fondo negro + 4 barras naranjas (no verdes) para diferenciar del prod.
"""
from PIL import Image, ImageDraw

SIZE = 180
BLACK = (0, 0, 0, 255)
ORANGE = (255, 159, 10, 255)  # iOS systemOrange — indica "test/preview"

img = Image.new('RGBA', (SIZE, SIZE), BLACK)
d = ImageDraw.Draw(img)

BAR_W = 20
Y_BASE = 138
RADIUS = 4
bars = [
    (48, 108), (76, 86), (104, 64), (132, 38),
]
for cx, ytop in bars:
    x1, x2 = cx - BAR_W//2, cx + BAR_W//2
    d.rounded_rectangle([x1, ytop, x2, Y_BASE], radius=RADIUS, fill=ORANGE)

img.save('/Users/juank4835/Documents/wealth-portal-pruebas/apple-touch-icon.png')
print('Saved apple-touch-icon.png (PRUEBAS · barras naranjas)')
