from flask import Flask, redirect, url_for, render_template, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)


app.config['SECRET_KEY'] = 'ad2415b22b9f75eb718ca3a723045915'


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", content=["tim", "jason", "bill"])


@app.route("/valves")
def valves():
    return render_template('valves.html', title='Valves')


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


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
