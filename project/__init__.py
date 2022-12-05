from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__, template_folder='templates', static_folder='static')
#здесь я указывала secret key через os
app.secret_key = ''
#здесь я указывала путь к db
app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# The absolute path of the directory containing images for users to download
app.config["CLIENT_IMAGES"] = "E:/AudiotoText/Flask_File_Downloads/filedownload/files/image"

# The absolute path of the directory containing CSV files for users to download
app.config["CLIENT_CSV"] = "E:/AudiotoText/Flask_File_Downloads/filedownload/files/csv"

# The absolute path of the directory containing PDF files for users to download
app.config["CLIENT_PDF"] = "E:/AudiotoText/Flask_File_Downloads/filedownload/files/pdf"

db = SQLAlchemy(app)
manager = LoginManager(app)

from project import models, routes

db.create_all()
