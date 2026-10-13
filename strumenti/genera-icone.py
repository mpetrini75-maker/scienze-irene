r"""Disegna le icone dell'app (emoji su fondo verde acqua) con Pillow e il font emoji di Windows.
Provvisorie: per icone belle vedi la scheda icone-immagini-usa-image-ai.
Uso:  py strumenti\genera-icone.py
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

R = Path(__file__).resolve().parent.parent
FONT = r"C:\Windows\Fonts\seguiemj.ttf"
for lato in (180, 192, 512):
    img = Image.new("RGB", (lato, lato), "#2E7D6B")
    d = ImageDraw.Draw(img)
    f = ImageFont.truetype(FONT, int(lato * 0.55))
    d.text((lato / 2, lato / 2), "\U0001F9EC", font=f, embedded_color=True, anchor="mm")
    img.save(R / f"icon-{lato}.png")
    print("scritta", f"icon-{lato}.png")
