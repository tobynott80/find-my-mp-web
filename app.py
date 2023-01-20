from flask import Flask, render_template, request
import requests
import jso
import jso

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/search')
def search():
    postcode = request.args.get('search')
    url = "https://members-api.parliament.uk/api/Location/Constituency/Search?searchText="+ postcode
    resp = requests.get(url)
    data = resp.json()
    if resp.status_code == 200:
        if data["totalResults"] == 0:
            return render_template('index.html', notFound=True)
        else:
            print(data)
            return str(data["items"][0]["value"]["currentRepresentation"]["member"]["value"]["id"])
    else:
        return 400
    return render_template('search.html',
                           postcode=postcode)

if __name__ == '__main__':
    app.run(debug=True)