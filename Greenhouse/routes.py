from flask import redirect, url_for, render_template, flash, redirect
from Greenhouse import app
from Greenhouse.forms import RegistrationForm, LoginForm, TimeInput
from Greenhouse.models import User
from datetime import datetime, date


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", content=["tim", "jason", "bill"])


@app.route("/valves", methods=['GET', 'POST'])
def valves():
    form = TimeInput()
    if form.validate_on_submit():
        difference = datetime.combine(
            date.today(), form.duration.data) - datetime.today()
        dateTimeA = datetime.now() + difference
        flash('Watering started', 'success')
        string = dateTimeA.strftime("%H:%M")
        print(string)
        return render_template('valves.html', title='Valves', form=form, date_string=string)
    return render_template('valves.html', title='Valves', form=form, date_string='')


@app.route("/automation")
def automation():
    return render_template('automation.html', title='Automation')


@app.route("/notifications")
def notifications():
    return render_template('notifications.html', title='Notifications')


@app.route("/system")
def system_activation():
    return render_template('system_activation.html', title='System Activation')


@app.route("/data")
def data():
    return render_template('data.html', title='Data')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'zievys.titas@gmail.com' and form.password.data == 'admin':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check Email and Password', 'danger')
    return render_template('login.html', title='Login', form=form)