
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/search')
def search():
    postcode = request.args.get('search')
    return render_template('search.html',
                           postcode=postcode)

if __name__ == '__main__':
    app.run(debug=True)