import pdf2image
import PIL
import os
import argparse

# TODO for the future:
# store files temporarily in /tmp/

parser = argparse.ArgumentParser(description='Simple script to make PDFs searchable')
parser.add_argument(
    'input_file',
    help='filepath for PDF to be targeted'
)
parser.add_argument(
    '-o',
    '--output',
    default='out',
    help='output filepath'
)

args = parser.parse_args()

# do stuff with parsed args here:

INPUT_FILE = args.input_file
SAVE_PATH = ''
OUTPUT_FILE = 'out'
# if fpath contains a .pdf at the end, remove it. tesseract does this automatically
fpath = os.path.splitext(args.output)[0]
if os.path.exists(fpath):
    OUTPUT_FILE = os.path.basename(fpath)
    SAVE_PATH = os.path.dirname(fpath)

pages = pdf2image.convert_from_path(INPUT_FILE)
ocr_command = open('ocr_command', 'w')

counter = 1
print('Number of pages: ' + str(len(pages)))
for page in pages:
    fp = SAVE_PATH+'pg_'+str(counter)+'.tiff'
    page.save(fp)
    ocr_command.write(fp+'\n')
    print('Saving ' + fp)
    counter += 1

# execute tesseract command
command = 'tesseract ocr_command '+fpath+' -l eng pdf'
ocr_command.close()
print('Executing "' + command + '"')
os.system(command)

# delete all the pdf files
pdf_files = open('ocr_command', 'r')
lines = pdf_files.read().splitlines()
for line in lines:
    print('Deleting ' + line)
    os.remove(line)
pdf_files.close()
os.remove('ocr_command')