from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS

# Initialize Flask app and configure SQLAlchemy
app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/tripfundtracker'
app.secret_key = "s!zQ!vyg!#MVKi6K&!K#xfhjS5b!2n4uR"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

# Global Static Parameters
upload_folder = './ODM_PDF_FILES'
generate_fr_folder = './ODM_WORD_FILES'
templates_folder = './Templates'
fr_template_file_path = templates_folder+'/odm_file.docx'
FIRST_LEVEL = 1
LAST_LEVEL = 6
COMPLETED_STATUS = 1
REJECTED_STATUS = -1