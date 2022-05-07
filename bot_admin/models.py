from . import db, login_manager
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255))
    username = db.Column(db.String(60), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)

    def __init__(self, full_name):
        self.full_name = full_name

    def __repr__(self):
        return f"User {self.full_name}"


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))
