from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
from navenio import app, db, bcrypt, basic_auth
from navenio.forms import RegistrationForm, LoginForm, SignalCrossing
from navenio.models import User
from flask_login import login_user, current_user, logout_user, login_required
from navenio.crossings import get_number_of_value_crossings


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account was created and you can login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            # next_page = request.args.get('next')
            return redirect('calcs') #if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful', 'danger')
    return render_template('login.html', title='Login', form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/calcs", methods=['GET', 'POST'])
@login_required
def calcs():
    form = SignalCrossing()
    counter = 0
    if form.validate_on_submit():
        signal_str = form.signal.data
        try:
            value = float(form.crossing_value.data)
            signal_list = signal_str.split()
            signal = [float(e) for e in signal_list]
            counter = get_number_of_value_crossings(signal, value)
        except:
            flash('wrong input', 'danger')
    return render_template('calcs.html', title='Calcs', form=form, counter = counter)

@app.route("/remote", methods=['GET', 'POST'])
@basic_auth.required
def remote():
    req_data = request.get_json()

    signal = req_data['signal']
    value = req_data['value']
    counter = get_number_of_value_crossings(signal, value)
    return jsonify(counter)
