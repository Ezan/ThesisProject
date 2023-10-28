from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

import os
import time

def createDir(path):
    if not os.path.isdir(path):
        os.makedirs(path)
    return path    

def pdf2txt(filename):
    output_string = StringIO()
    with open(filename, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
        return output_string.getvalue()

def convert():
    # if __name__ == "__main__":
    start = time.time()
    not_include = ['doi_ids', 'elsevier']
    # path = './datasets/pdf'                         # Directory which contain pdf data
    path = '../../datasets/'  # Directory which contain pdf data
    save_dir = createDir('../../datasets/txt')          # Create a directory for saving txt datas
    error = []
    for index, dir_name in enumerate(os.listdir(path)):
        # print('{}------------------------------------------------'.format(dir_name))
        fullname = os.path.join(path, dir_name)
        print('{}------------------------------------------------'.format(fullname))
        if os.path.isdir(fullname) and not dir_name in not_include:
            for index2, filename in enumerate(os.listdir(fullname)):
                if filename.endswith('.pdf'):
                    try:
                        fullname2 = os.path.join(fullname, filename)
                        txt = pdf2txt(fullname2)        # Convert pdf to txt
                        out_filename = os.path.join(save_dir, filename.replace('.pdf','.txt'))
                        with open(out_filename, 'w') as out_file:
                            out_file.write(txt)         # Save the result
                    except:
                        error.append('{}\t{}'.format(dir_name, filename))
                        print('Error: {} ============================================'.format(filename))
                        continue
                    if (index2+1)%100 == 0:
                        print('{}/{}---------------------------------------------'.format(index2+1, len(os.listdir(fullname))))
    with open('../../datasets/error_pdf2txt.txt', 'w') as out_error:
        out_error.write('\n'.join(error))               # Save the error result
    print('Running Time: {} seconds'.format(time.time()-start))


# if __name__ == "__main__":
#     convert()