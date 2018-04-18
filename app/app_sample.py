from flask import Flask, render_template
from data import Businesses, Reviews
app = Flask(__name__)

Businesses = Businesses()
Reviews = Reviews()

@app.route("/")
def home_index():
    return render_template('home.html', businesses = Businesses)

@app.route("/livedemo")
def livedemo_index():
    return render_template('livedemo.html')

@app.route("/accuracy")
def accuracy_index():
    return render_template('accuracy.html')

@app.route('/biz/<biz_id>')
def biz_index(biz_id):
    business = [b for i, b in enumerate(Businesses) if biz_id in b["business_id"]]
    reviews = [r for j, r in enumerate(Reviews) if biz_id in r["business_id"]]
    return render_template('business.html', business = business[0], reviews = reviews)
