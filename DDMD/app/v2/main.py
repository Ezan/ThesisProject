from flask import Flask, render_template, request
from app.v1 import paper_scraper

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/paper', methods=['GET','POST'])
def paper():
    if request.method == 'POST':
        result=request.form['paper']
        paper_scraper.scrape(result)


if __name__=="__main__":
    app.run(debug = True)


# flask --app ./DDMD/app/v2/main.py --debug run