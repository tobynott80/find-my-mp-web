from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def getImage(mpId):
    url = "https://members-api.parliament.uk/api/Members/" + str(mpId) + "/PortraitUrl"
    resp = requests.get(url)
    data = resp.json()
    if resp.status_code != 200:
        return ""
    return data["value"]


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
            data = data["items"][0]["value"]
            print(data)
            # mp = json.loads(data)
            constituency = data["name"]
            mpName = data["currentRepresentation"]["member"]["value"]["nameDisplayAs"]
            mpParty = data["currentRepresentation"]["member"]["value"]["latestParty"]["name"]
            mpId = data["currentRepresentation"]["member"]["value"]["id"]
            mpImgUrl = getImage(mpId)
            return render_template('results.html', constituency=constituency, mpName=mpName, mpParty=mpParty, mpImgUrl=mpImgUrl)
    else:
        return 400

if __name__ == '__main__':
    app.run(debug=True)