from flask import Flask

app = Flask(__name__)

from app import web
from app import api
