from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home_index():
    return render_template('home.html')

@app.route("/livedemo")
def livedemo_index():
    return render_template('livedemo.html')

@app.route("/accuracy")
def accuracy_index():
    return render_template('accuracy.html')

@app.route('/biz/<biz_id>')
def profile(biz_id):
	return """


	<!DOCTYPE html>
<html>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>
<h2>Hello, """ + biz_id + """

</body>
</html>
"""
