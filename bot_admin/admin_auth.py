from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user
from flask_admin.menu import MenuLink
from flask_admin import Admin
from .custom_admin_views import MyModelView, MyAdminIndexView
from .forms import LoginForm
from .models import Users
from . import app, db

admin_auth = Blueprint('admin_auth', __name__)

admin = Admin(app, index_view=MyAdminIndexView(), name='Admin panel', template_mode='bootstrap4')
admin.add_view(MyModelView(Users, db.session))
admin.add_link(MenuLink(name=f'Logout', category='', url='/logout'))


@admin_auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = Users.query.filter_by(username=username, password=password).first()

        if user:
            login_user(user)
            flash('You are logged successfully!', category='success')
            return redirect('/admin')
        else:
            flash('Username or password invalid! Try again.', category='danger')
            return redirect(url_for('admin_auth.login'))

    return render_template('login.html', form=form)


@admin_auth.route('/logout')
def logout():
    logout_user()
    flash("Logged out!", category='info')
    return redirect(url_for('admin_auth.login'))
