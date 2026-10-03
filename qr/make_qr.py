"""
Generate one QR code per week, sized for the QR box in the handbook.

border=4 is the quiet zone the QR spec requires. Anything less and scanners
struggle once the code is printed small.

    pip install "qrcode[pil]"
    python3 make_qr.py

Edit BASE to your live GitHub Pages URL. make_spreads.py picks these up
automatically and embeds them in the printed pages.
"""
import qrcode
from qrcode.constants import ERROR_CORRECT_M

BASE = "https://confidevop.github.io/maker-weeks/weeks.html"
WEEKS = range(1, 26)
OUT = "."

for n in WEEKS:
    img = qrcode.QRCode(version=None, error_correction=ERROR_CORRECT_M, box_size=10, border=4)
    img.add_data(f"{BASE}#week{n}")
    img.make(fit=True)
    img.make_image(fill_color="black", back_color="white").save(f"{OUT}/week{n:02d}.png")
    print(f"week{n:02d}.png  ->  {BASE}#week{n}")
