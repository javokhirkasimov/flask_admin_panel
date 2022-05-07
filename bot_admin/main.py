from flask import Blueprint, redirect

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    return redirect('/admin')
