from flask import Flask, render_template
from data import Businesses, Reviews
from sentiment import overall_sentiments_list, overall_sentiments_ave, overall_sentiments_std, category_sentiments_list, category_sentiments_ave, category_sentiments_std
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
    overall_list = overall_sentiments_list(reviews)
    overall_ave = overall_sentiments_ave(reviews)
    overall_std = overall_sentiments_std(reviews)
    category_list = category_sentiments_list(reviews)
    category_ave = category_sentiments_ave(reviews)
    category_std = category_sentiments_std(reviews)
    return render_template('restaurant.html', business=business[0], reviews=reviews, overall_list=overall_list, overall_ave=overall_ave, overall_std=overall_std, category_list=category_list, category_ave=category_ave, category_std=category_std)

if __name__ == "__main__":
	app.run()
