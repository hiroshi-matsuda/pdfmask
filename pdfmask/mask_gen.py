import sys

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.units import mm
from reportlab.lib.colors import white


USAGE = """Usage:
  pdfmask_gen output_pdf_path pagesize margin-left margin-right margin-top margin-bottom [mask-color-red mask-color-green mask-color-blue]

    pagesize     A4 or letter
    margin-*     float value in millimeter
    mask-color-* float value from 0.0 to 1.0 (default=1.0)
"""

PAGESIZES = {"a4": A4, "letter": letter}


def draw_mask_rect(target, pagesize, margins, rgb):
    target.setFillColorRGB(*rgb)
    target.rect(
        margins[0],
        margins[2],
        pagesize[0] -  margins[0] - margins[1],
        pagesize[1] -  margins[2] - margins[3],
        stroke=0,
        fill=1,
    )


def main():
    if len(sys.argv) not in [7, 10] or sys.argv[2].lower() not in ["a4", "letter"]:
        print(USAGE)
        sys.exit(1)
        return
    pdf_path = sys.argv[1]
    pagesize = PAGESIZES[sys.argv[2].lower()]
    margins = [float(_) * mm for _ in sys.argv[3:7]]
    if len(sys.argv) >= 10:
        rgb = [float(_) for _ in sys.argv[7:10]]
    else:
        rgb = 1.0, 1.0, 1.0

    target = canvas.Canvas(pdf_path, pagesize=pagesize)
    draw_mask_rect(target, pagesize, margins, rgb)
    target.save()


if __name__ == "__main__":
    main()
