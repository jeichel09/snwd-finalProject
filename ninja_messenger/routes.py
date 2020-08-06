from flask import flash, make_response, render_template, request, redirect, url_for
from ninja_messenger import app, db
from ninja_messenger.forms import RegisterForm, LoginForm, MessageForm
from ninja_messenger.models import User, Message
from flask_login import login_user, current_user, logout_user, login_required

db.create_all()

@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def index():
    form = MessageForm()
    if form.validate_on_submit():
        message = Message(recipient=form.recipient.data, message=form.message.data, author=current_user)
        db.session.add(message)
        db.session.commit()
        flash('Your message has been sent!')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        #user = User.query.filter_by(email=form.email.data).first()
        user = db.session.query(User).filter_by(email=form.email.data).first()
        if user and User.check_password:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password!', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        #hashed_password = User.set_password(form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')