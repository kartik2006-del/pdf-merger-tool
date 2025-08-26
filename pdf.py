try:
    from PyPDF2 import PdfMerger

except ImportError:
    print("Error: PyPDF2 is not installed. Run \' pip install PyPDF2\' and try again")
    exit()

def pdf_merger():
    merger=PdfMerger()
    files=['sample 1 .pdf','sample 2 .pdf']
    for file in files:
        merger.append(file)

    merger.write('merger.pdf')
    merger.close()

    print('Merging completed successfully ! ')
pdf_merger()