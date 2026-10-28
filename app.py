# IMPORT DES 
import login_py, register_py, profile_py
from flask import Flask, render_template, request

CONST_USERNAME = None
CONST_COIN = None


app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    return register_py.register_func()


@app.route("/login", methods=["GET", "POST"])
def login():
    temp = login_py.login_func()
    global CONST_COIN
    global CONST_USERNAME
    CONST_USERNAME = temp[1]
    CONST_COIN = temp[2]
    return render_template("index.html", msg=temp[0], coin=CONST_COIN, username=CONST_USERNAME)


@app.route("/profile", methods=["GET", "POST"])
def profile():
    return profile_py.profile_func(CONST_USERNAME, CONST_COIN)


if __name__ == "__main__":
    app.run(debug=True)