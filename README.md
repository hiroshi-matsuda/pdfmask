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
$ pdfmask mask-A4-20_20_30_30.pdf some_paper.pdf
```

### Usage

```
pdfmask [--never-repeat] mask-pdf-path target-pdf-path1 [target-pdf-path2 [...]]

    --never-repeat  Aligning pages with mask-pdf and target-pdf
```

The masked output files will be placed in the same directory of target-pdf-path and have the suffix `.masked.pdf`.

To specify a mask-pdf file with multiple pages, use the `--never-repeat` option.
This is useful for adding headers, footers, and page numbers.

## License and Dependencies

- `pdfmask` is distributed under the terms of BSD-3-Clause license:
  - [BSD-3-Clause license](https://raw.githubusercontent.com/hiroshi-matsuda/pdfmask/main/LICENSE)
- `reportlab` is distributed under the terms of BSD-3-Clause license:
  - See https://www.reportlab.com/
- `PyPDF2` is distributed under the license below:
  - See https://raw.githubusercontent.com/py-pdf/PyPDF2/main/LICENSE

## Change Logs

### v0.1

#### v0.1.1
- 2022.08.28
- Add `--never-repeat` option to `pdfmask`

#### v0.1.0
- 2022.08.28
- The first version
