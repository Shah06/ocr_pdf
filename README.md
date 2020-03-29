# ocr_pdf
Simple python3 script to make PDF searchable. Made to make my life easier when scanning schoolwork.

### Requirements:
1. [Tesseract](https://github.com/tesseract-ocr/tesseract). Tested with 4.1.1
2. `PIL` and `pdf2image`.

### Usage:
```
usage: makepdf.py [-h] [-o OUTPUT] input_file

Simple script to make PDFs searchable

positional arguments:
  input_file            filepath for PDF to be targeted

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output filepath
```

### Upcoming (?) Features:
1. Use `/tmp/` to store files
2. Ability to output to plaintext
3. Take in other image formats as input, and output a PDF
4. Ability to apply an adaptive contrast/sharpening filter to PDF
