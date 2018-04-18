from flask import Flask, render_template
from data import Businesses, Reviews
app = Flask(__name__)

Businesses = Businesses()
Reviews = Reviews()

@app.route("/")
def home_index():
    return render_template('home.html', businesses = Businesses)

@app.route("/customreview")
def customreview_index():
    return render_template('customreview.html')

@app.route("/accuracy")
def accuracy_index():
    return render_template('accuracy.html')

@app.route('/restaurants')
def restaurants_index():
    return render_template('restaurants.html', businesses = Businesses)

@app.route('/restaurants/<biz_id>')
def restaurant_index(biz_id):
    business = [b for i, b in enumerate(Businesses) if biz_id in b["business_id"]]
    reviews = [r for j, r in enumerate(Reviews) if biz_id in r["business_id"]]
    return render_template('restaurant.html', business = business[0], reviews = reviews)
