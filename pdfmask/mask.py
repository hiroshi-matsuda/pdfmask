import sys

from PyPDF2 import PdfFileWriter, PdfFileReader


USAGE = """Usage:
  pdfmask mask-pdf-path target-pdf-path1 [target-pdf-path2 [...]]
"""


def mask_all_pages(masking_page, source_pdf):
    output_pdf = PdfFileWriter()
    pages = source_pdf.getNumPages()
    print(f"{pages} page(s)", end="\t", flush=True)
    for p in range(pages):
        page = source_pdf.getPage(p)
        page.mergePage(masking_page)
        output_pdf.addPage(page)
    return output_pdf


def main():
    if len(sys.argv) < 3:
        print(USAGE)
        sys.exit(1)
        return
    masking_pdf = PdfFileReader(open(sys.argv[1], "rb"))
    masking_page = masking_pdf.getPage(0)
    for source_path in sys.argv[2:]:
        print(source_path, end="\t", flush=True)
        try:
            source_pdf = PdfFileReader(open(source_path, 'rb'), strict=False)
        except Exception as e:
            print("        \tfailed", e, sep="\t") 
            continue
        try:
            output_pdf = mask_all_pages(masking_page, source_pdf)
            if source_path[-4:].lower() == ".pdf":
                output_path = source_path[:-4] + ".masked.pdf"
            else:
                output_path = source_path + ".masked.pdf"
            with open(output_path, "wb") as out:
                output_pdf.write(out)
            print("succeeded")
        except Exception as e:
            print("failed", e, sep="\t") 


if __name__ == "__main__":
    main()
