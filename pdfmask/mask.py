import sys

from PyPDF2 import PdfFileWriter, PdfFileReader


USAGE = """Usage:

  pdfmask [--never-repeat] mask-pdf-path target-pdf-path1 [target-pdf-path2 [...]]

    --never-repeat  Aligning pages with mask-pdf and target-pdf
"""


def mask_all_pages(masking_pdf, masking_page, never_repeat, source_pdf):
    output_pdf = PdfFileWriter()
    masking_num_pages = masking_pdf.getNumPages()
    source_num_pages = source_pdf.getNumPages()
    print(f"{source_num_pages} page(s)", end="\t", flush=True)
    for p in range(source_num_pages):
        if masking_page == masking_num_pages:
            return None, masking_num_pages
        page = source_pdf.getPage(p)
        page.mergePage(masking_pdf.getPage(masking_page))
        output_pdf.addPage(page)
        masking_page += 1
        if masking_page == masking_num_pages:
            if not never_repeat:
                masking_page = 0
    return output_pdf, masking_page


def main():
    if len(sys.argv) >= 4 and sys.argv[1] == "--never-repeat":
        never_repeat = True
        mask_pdf_path = sys.argv[2]
        source_pdf_paths = sys.argv[3:]
    elif len(sys.argv) >= 3 and sys.argv[1] != "--never-repeat":
        never_repeat = False
        mask_pdf_path = sys.argv[1]
        source_pdf_paths = sys.argv[2:]
    else:
        print(USAGE)
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
            if source_pdf_path[-4:].lower() == ".pdf":
                output_path = source_pdf_path[:-4] + ".masked.pdf"
            else:
                output_path = source_pdf_path + ".masked.pdf"
            with open(output_path, "wb") as out:
                output_pdf.write(out)
            print("succeeded")
        except Exception as e:
            print("failed", e, sep="\t") 


if __name__ == "__main__":
    main()
