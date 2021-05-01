from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", content=["tim", "jason", "bill"])


@app.route("/valves")
def valves():
    return render_template('valves.html', title='valves')


@app.route("/automation")
def automation():
    return render_template('automation.html', title='automation')


@app.route("/notifications")
def notifications():
    return render_template('notifications.html', title='automation')


@app.route("/system")
def system_activation():
    return render_template('system_activation.html', title='automation')


@app.route("/data")
def data():
    return render_template('data.html', title='automation')


if __name__ == "__main__":
    app.run(debug=True)
