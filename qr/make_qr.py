"""
Generate one QR code per week, sized for the 0.95in box in the handbook.

    pip install "qrcode[pil]"
    python3 make_qr.py

Edit BASE to your live GitHub Pages URL, then drop the PNGs into the spreads.
"""
import qrcode
from qrcode.constants import ERROR_CORRECT_M

BASE = "https://YOURNAME.github.io/maker-weeks/weeks.html"
WEEKS = range(1, 26)
OUT = "."

for n in WEEKS:
    img = qrcode.QRCode(version=None, error_correction=ERROR_CORRECT_M, box_size=10, border=2)
    img.add_data(f"{BASE}#week{n}")
    img.make(fit=True)
    img.make_image(fill_color="black", back_color="white").save(f"{OUT}/week{n:02d}.png")
    print(f"week{n:02d}.png  ->  {BASE}#week{n}")
