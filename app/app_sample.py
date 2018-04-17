from flask import Flask, render_template
from data import Businesses
app = Flask(__name__)

Businesses = Businesses()

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
def profile(biz_id):
	return render_template('business.html', biz_id = biz_id, businesses = Businesses)
