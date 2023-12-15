from flask import Flask, render_template, request
# from app.v1 import paper_scraper
from download import download_and_unzip_from_html

app = Flask(__name__, template_folder='templates')
html_page_url = 'https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/00/00/'

# Replace 'YOUR_PUBMED_API_KEY' with your actual PubMed API key
PUBMED_API_KEY = 'YOUR_PUBMED_API_KEY'

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/paper', methods=['GET','POST'])
def paper():
    if request.method == 'POST':
        # result=request.form['paper']
        # paper_scraper.scrape(result)
        return download_and_unzip_from_html(html_page_url)


if __name__=="__main__":
    app.run(debug = True)


# flask --app ./DDMD/app/v2/main.py --debug run