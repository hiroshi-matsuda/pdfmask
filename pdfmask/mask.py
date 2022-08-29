from decimal import Decimal
import os
import sys

from PyPDF2 import PdfFileWriter, PdfFileReader


USAGE_PDFMASK = """Usage:

  pdfmask [-d output_dir] mask-pdf-path target-pdf-path1 [target-pdf-path2 [...]]

    -d output_dir Use output_dir for saving masked PDF files
"""

USAGE_PDFLAMINATE = """Usage:

  pdflaminate [-d output_dir] header-footer-pages-pdf-path target-pdf-path1 [target-pdf-path2 [...]]

    -d  Use output_dir for saving laminated PDF files
"""

MM = Decimal(0.3528)
MAX_SIZE_DIFF = Decimal(1)


def validate_sizes(page_width, page_height, mask_width, mask_height):
    return abs(page_width - mask_width) * MM <= MAX_SIZE_DIFF and abs(page_height - mask_height) * MM <= MAX_SIZE_DIFF


def mask_all_pages(masking_pdf, masking_page, never_repeat, source_pdf):
    output_pdf = PdfFileWriter()
    masking_num_pages = masking_pdf.getNumPages()
    source_num_pages = source_pdf.getNumPages()
    print(f"{source_num_pages} page(s)", end="\t", flush=True)
    for p in range(source_num_pages):
        if masking_page == masking_num_pages:
            return None, masking_num_pages
        page = source_pdf.getPage(p)
        mask = masking_pdf.getPage(masking_page)
        page_size = page.mediaBox
        mask_size = mask.mediaBox
        if not validate_sizes(page_size.getWidth(), page_size.getHeight(), mask_size.getWidth(), mask_size.getHeight()):
            raise Exception(f"Incompatible page size: page#{p + 1}=({page_size.getWidth() * MM:.3f}, {page_size.getHeight() * MM:.3f}), mask#{masking_page + 1}=({mask_size.getWidth() * MM:.3f}, {mask_size.getHeight() * MM:.3f})")
        page.mergePage(mask)
        output_pdf.addPage(page)
        masking_page += 1
        if masking_page == masking_num_pages:
            if not never_repeat:
                masking_page = 0
    return output_pdf, masking_page


def exec(suffix, never_repeat, usage):
    if len(sys.argv) >= 5 and sys.argv[1] == "-d":
        suffix = None
        output_dir = sys.argv[2]
        os.makedirs(output_dir, exist_ok=True)
        mask_pdf_path = sys.argv[3]
        source_pdf_paths = sys.argv[4:]
    elif len(sys.argv) >= 3 and sys.argv[1] != "-d":
        output_dir = None
        mask_pdf_path = sys.argv[1]
        source_pdf_paths = sys.argv[2:]
    else:
        print(usage)
        sys.exit(1)
        return
    masking_pdf = PdfFileReader(open(mask_pdf_path, "rb"))
    masking_page = 0
    for source_pdf_path in source_pdf_paths:
        print(source_pdf_path, end="\t", flush=True)
        try:
            source_pdf = PdfFileReader(open(source_pdf_path, 'rb'), strict=False)
        except Exception as e:
            print("        \tfailed", e, sep="\t") 
            continue
        try:
            output_pdf, masking_page = mask_all_pages(masking_pdf, masking_page, never_repeat, source_pdf)
            if output_pdf is None:
                print("        \tfailed", f"Insufficient number of pages in mask-pdf ({masking_page + 1})", sep="\t")
                print(f"Error: verify {mask_pdf_path}")
                sys.exit(1)
                return
            if output_dir is not None:
                p = source_pdf_path.replace("\\", "/").split("/")
                output_path = f"{output_dir}/{p[-1]}"
            elif source_pdf_path[-4:].lower() == ".pdf":
                output_path = source_pdf_path[:-4] + suffix
            else:
                output_path = source_pdf_path + suffix
            with open(output_path, "wb") as out:
                output_pdf.write(out)
            print("succeeded")
        except Exception as e:
            print("failed", e, sep="\t") 


def main_mask():
    exec(suffix=".masked.pdf", never_repeat=False, usage=USAGE_PDFMASK)


def main_laminate():
    exec(suffix=".laminated.pdf", never_repeat=True, usage=USAGE_PDFLAMINATE)


if __name__ == "__main__":
    main_mask()
