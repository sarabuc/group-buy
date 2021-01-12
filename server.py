# serve.py

from flask import Flask
from flask import render_template



# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    # message = "Hello, World"
    return app.send_static_file('index.html')

app.run(debug=True, port=5000)
