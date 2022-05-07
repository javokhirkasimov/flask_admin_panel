from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from environs import Env

env = Env()
env.read_env()

app = Flask(__name__, static_url_path='/static', template_folder='templates')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = env.str('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{user}:{password}@localhost/{db_name}'.format(
    user=env.str('DB_USER'),
    password=env.str('DB_PASSWORD'),
    db_name=env.str('DB_NAME')
)

db = SQLAlchemy(app)

login_manager = LoginManager(app)

# register blueprints
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

from .admin_auth import admin_auth as admin_auth_blueprint
app.register_blueprint(admin_auth_blueprint)
