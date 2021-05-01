from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", content=["tim", "jason", "bill"])


@app.route("/valves")
def valves():
    return render_template('valves.html', title='valves')


if __name__ == "__main__":
    app.run(debug=True)
