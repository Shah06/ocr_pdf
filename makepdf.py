import pdf2image
import PIL
import os

INPUT_FILE = 'test.pdf'
SAVE_PATH = ''
OUTPUT_FILE = 'out'

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
command = 'tesseract ocr_command '+OUTPUT_FILE+' -l eng pdf'
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
#os.remove('ocr_command')
