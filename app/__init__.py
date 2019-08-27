from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_mail import Mail
# flask_cors CORS allows local hosts to communicate without restriction
# avoids cross origin reference errors

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)
mail = Mail(app)


from app import routes
