from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS
from flask_session import Session
from datetime import timedelta
import redis
import os

# Initialize Flask app and configure SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = "egD%w%nhmpT@PH!SLxaWr7t5%PW8sBUF&NiB4kwDYChxUysKy@BJqiGyNRsJ$rocFaz$N"
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_COOKIE_PATH'] = '/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/tripfundtracker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager = LoginManager(app)
CORS(app, supports_credentials=True)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
Session(app)


# Global Static Parameters
temp_folder = './temp'
templates_folder = './Templates'
default_password = 'nsct@123'
fr_template_file_path = templates_folder+'/odm_file.docx'
fund_doc_template_file_path = templates_folder+'/fund_file.docx'
FIRST_LEVEL = 1
DGA_LEVEL = 4
LAST_LEVEL = 8
LEVEL_NO_SIGNATURE_NEEDED = [7,8]
LEVEL_BEFORE_DGA_FOR_ODM = [1, 2, 3]
LEVEL_BEFORE_DGA_FOR_FDM = [5, 6]
COMPLETED_STATUS = 1
REJECTED_STATUS = -1