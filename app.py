from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/search')
def search():
    postcode = request.args.get('search')
    url = "https://members-api.parliament.uk/api/Location/Constituency/Search?searchText="+ postcode
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        if data["totalResults"] == 0:
            return render_template('index.html', notFound=True)
        else:
            print(data)
            mp = json.loads(data)
            print(mp["nameDisplayAs"])
            return 
    else:
        return 400

if __name__ == '__main__':
    app.run(debug=True)