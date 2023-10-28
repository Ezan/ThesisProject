from flask import Flask, render_template, request
from app.v1 import pdf2txt, Image_Desc_Extracted_Split_Joining_allPapers as image_desc_join, \
    Image_Extraction_From_Research_Papers_script as image_extract, \
    Image_Extracted_Desc_Splitting_Common_code as image_common_desc, paper_scraper, join_all_captions as caption_join, \
    Image_Description_Extraction as image_desc, caption_image_join

import  os
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/paper', methods=['GET','POST'])
def paper():
    if request.method == 'POST':
        result=request.form['paper']
        paper_scraper.scrape(result)
        # print (video)
        filespath = '../datasets/papers'
        paperList = []
        for file in os.listdir(filespath):
            paperList.append(file)
        # commentList = pd.DataFrame.from_csv(fileName)
        # data = {'message': result, 'code': 'SUCCESS'}
        # return render_template('papers.html', data=paperList)
        image_extract.extract_image()
        pdf2txt.convert()
        image_desc.extract()
        image_common_desc.extract()
        image_desc_join.split_join()
        caption_join.join_all()
        subprocess.call(['sh', './util_image.sh'])
        caption_image_join.join()


if __name__=="__main__":
    app.run(debug = True)