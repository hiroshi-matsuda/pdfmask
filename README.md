# pdfmask
A command line tool for masking the content area in PDF

## Installation

```console
$ pip install pdfmask
```

## Create mask PDF file

### Example

```console
$ pdfmask_gen mask-A4-20_20_30_30.pdf A4 20 20 30 30
```

### Usage

```
pdfmask_gen output-mask-pdf-path pagesize margin-left margin-right margin-top margin-bottom [mask-color-red mask-color-green mask-color-blue]
```
- `pagesize`
  - `A4` or `letter`
- `margin-*`
  - float value in millimeter
- `mask-color-*`
  - float value from 0.0 to 1.0 (default=1.0)

## Apply mask to target PDF files

### Example

```console
$ pdfmask mask-A4-20_20_30_30.pdf ./papers/*.pdf

./papers/A1-1.pdf      5 page(s)       succeeded
./papers/A1-2.pdf      5 page(s)       succeeded
./papers/A1-3.pdf      6 page(s)       failed Incompatible page size: page#1=(297.058, 209.916), mask#1=(210.013, 297.019)
./papers/A1-4.pdf      6 page(s)       succeeded
```

### Usage

```
pdfmask [-d output_dir] mask-pdf-path target-pdf-path1 [target-pdf-path2 [...]]

    -d output_dir Use output_dir for saving masked PDF files
```

If `-d` option not specified, the masked output files will be placed in the same directory of target-pdf-path and have the suffix `.masked.pdf`.

## Laminate pages in PDF files

`pdflaminate` is useful for adding headers, footers, and page numbers.

### Example

```console
$ pdflaminate -d dist/ header_footer_pages.pdf ./papers/*.pdf

./papers/A1-1.pdf      5 page(s)       succeeded
./papers/A1-2.pdf      5 page(s)       succeeded
./papers/A1-3.pdf      6 page(s)       failed Incompatible page size: page#1=(297.058, 209.916), mask#1=(210.013, 297.019)
./papers/A1-4.pdf      6 page(s)       succeeded
```

### Usage

```
pdflaminate [-d output_dir] header-footer-pages-pdf-path target-pdf-path1 [target-pdf-path2 [...]]

    -d  Use output_dir for saving laminated PDF files
```

`header-footer-pages-pdf` is supposed to have the page namubers and to be laminated with individually created PDF files.

If `-d` option not specified, the laminated output files will be placed in the same directory of target-pdf-path and have the suffix `.laminated.pdf`.


## License and Dependencies

- `pdfmask` is distributed under the terms of BSD-3-Clause license:
  - [BSD-3-Clause license](https://raw.githubusercontent.com/hiroshi-matsuda/pdfmask/main/LICENSE)
- `reportlab` is distributed under the terms of BSD-3-Clause license:
  - See https://www.reportlab.com/
- `PyPDF2` is distributed under the license below:
  - See https://raw.githubusercontent.com/py-pdf/PyPDF2/main/LICENSE

## Change Logs

### v0.2

#### v0.2.0
- 2022.08.29
- Add `pdflaminate` command
- Add page size checking
- Drop `--never-repeat` option

### v0.1

#### v0.1.1
- 2022.08.28
- Add `--never-repeat` option to `pdfmask`

#### v0.1.0
- 2022.08.28
- The first version
