from flask import Flask
app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!" + 
    
@app.route('/user/<rest_id>')
def profile(rest_id):
	return """


	<!DOCTYPE html>
<html>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>
<h2>Hello, """ + rest_id + """

</body>
</html>
"""
    