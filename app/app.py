from flask import Flask, render_template, request
import requests
import sys
import os

app = Flask(__name__)

def getImage(mpId):
    url = "https://members-api.parliament.uk/api/Members/" + str(mpId) + "/PortraitUrl"
    resp = requests.get(url)
    data = resp.json()
    if resp.status_code != 200:
        return ""
    return data["value"]

def getNews(mpName):
    newsResults = []
    if guardianKey == '':
        return 0
    else:
        headers = {
            'api-key': guardianKey,
        }
        url = "https://content.guardianapis.com/search?q=" + str(mpName)
        resp = requests.request("GET", url, headers=headers)
        if resp.status_code == 200:
            print("Sucessfully Reached Guardian API")
            data = resp.json()
            data = data["response"]["results"]
            for i in data:
                iDate = i["webPublicationDate"]
                iDate = iDate[0:9]
                iNews = newsItem(i["webTitle"],iDate,i["webUrl"])
                newsResults.append(iNews)
            return newsResults
        elif resp.status_code == 401:
            print("Unauthorised: Please Check Guardian API key")
            return newsResults

class newsItem:
        def __init__(self, title, date, url):
            self.title = title
            self.date = date
            self.url = url

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
            constituency = data["name"]
            mpName = data["currentRepresentation"]["member"]["value"]["nameDisplayAs"]
            mpParty = data["currentRepresentation"]["member"]["value"]["latestParty"]["name"]
            mpId = data["currentRepresentation"]["member"]["value"]["id"]
            mpImgUrl = getImage(mpId)
            mpNews = getNews(mpName)
            return render_template('results.html', constituency=constituency, mpName=mpName, mpParty=mpParty, mpImgUrl=mpImgUrl, mpNews=mpNews)
    else:
        return 400

if __name__ == '__main__':
    if os.environ.get('GUARDIAN_KEY') == '':
        guardianKey = str(input("Please enter the guardian API key \n Note: leave this blank to disable news functionality: "))
    else:
        guardianKey = os.environ.get('GUARDIAN_KEY')
        print("Set guardian API key as " + guardianKey)
        app.run(host='0.0.0.0', port=80)