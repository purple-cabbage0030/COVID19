from flask import Flask, render_template, request, jsonify
from crawler import Crawling

app = Flask(import_name=__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/', methods=['get'])
def index():
    return render_template('index.html')

@app.route('/covidchart', methods=['get'])
def get_covid():
    return ""

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)