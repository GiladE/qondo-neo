from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:docker@localhost:5432/qondo_neo'
db = SQLAlchemy(app)

from app import web
from app import api
from app.models import *
