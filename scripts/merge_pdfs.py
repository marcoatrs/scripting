import sys
from argparse import ArgumentParser
from pathlib import Path

import PyPDF2 as pdf

parser = ArgumentParser()
parser.add_argument('--source', '-s', type=str, help='PDFs path')
parser.add_argument('--output', '-o', type=str, help='output filename', default='merge_pdf.pdf')

args = parser.parse_args()

merger = pdf.PdfMerger()
folder_path = Path(args.source)

if not folder_path.exists():
    print('Folder not found')
    sys.exit(1)

for path in folder_path.glob('*.pdf'):
    merger.append(path)

output = args.output
if not output.endswith(".pdf"):
    output += '.pdf'

merger.write(output)
merger.close()
