# Yelp Review Challenge

Can't upload filtered restaurants to GitHub because the file to filter and the resulting file are too large, so add yelp_business.csv from Kaggle (https://www.kaggle.com/yelp-dataset/yelp-dataset/data) to the data_sample folder and then run the filter_businesses.py script to get restaurant csv file.

To get first 750,000 restaurant reviews: add yelp_reviews.csv from Kaggle (https://www.kaggle.com/yelp-dataset/yelp-dataset/data) to the data_sample folder and then run the restaurant_reviews.py script to get the restaurant reviews csv file.

# Run Flask App
1. Update pip `$curl https://bootstrap.pypa.io/get-pip.py | python`

2. Install flask `$pip install Flask`

3. Enter directory w/ flask file `$cd app`

4. Open flask file `$open .`

5. Run flask file in debug Mode `$export FLASK_DEBUG=1` `$export FLASK_APP=app_sample.py` `$flask run`

6. Paste Generated Address in Browser `http://127.0.0.1:5000/`
