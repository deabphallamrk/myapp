from homepage.views import *

@app.route('/')
def home():
    return '<h1>Hello World</h1>'
