from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.forms import LoginForm
from werkzeug.security import check_password_hash

main = Blueprint('main', __name__)  # define blueprint here

@main.route('/login', methods=['GET', 'POST'])
def login():
    from app import mongo  # ←✅ import locally here
    form = LoginForm()

    if request.method == 'POST':
        print("Form submitted")
        print("Form valid?", form.validate_on_submit())
        print("Username entered:", form.username.data)
        print("Password entered:", form.password.data)

        admin = mongo.db.admins.find_one({'username': form.username.data})
        print("Admin document:", admin)

        if admin and check_password_hash(admin['password'], form.password.data):
            session['admin'] = admin['username']
            flash('Login successful', 'success')
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid credentials', 'danger')

    return render_template('login.html', form=form)



@main.route('/')
def home():
    return render_template('home.html')


@main.route('/logout')
def logout():
    session.pop('admin', None)
    flash('Logged out.', 'info')
    return redirect(url_for('main.login'))


@main.route('/show-admins')
def show_admins():
    admins = mongo.db.admins.find()
    return "<br>".join([f"{a['username']}" for a in admins])


@main.route('/dashboard')
def dashboard():
    if 'admin' not in session:
        return redirect(url_for('main.login'))
    return f"Welcome, {session['admin']}!"
