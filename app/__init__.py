from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 

app.config['SECRET_KEY'] = 'abc'
app.config['WTF_CSRF_ENABLED'] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///testingdb"

db = SQLAlchemy(app)     
