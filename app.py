import server.login_py as login_py
import server.register_py as register_py
# import server.profile_py as profile_py
from flask import Flask, render_template, request

CONST_USERNAME = None
CONST_COIN = None


app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/register_page", methods=["GET", "POST"])
def register_page():
    print("page register html")
    return render_template("register.html")


@app.route("/login_page", methods=["GET", "POST"])
def login_page():
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    temp = register_py.register_func()
    return render_template("register.html", nom = temp)


@app.route("/login", methods=["GET", "POST"])
def login():
    temp = login_py.login_func()
    global CONST_COIN
    global CONST_USERNAME
    CONST_USERNAME = temp[1]
    CONST_COIN = temp[2]
    return render_template("login.html", msg=temp[0], coin=CONST_COIN, username=CONST_USERNAME)


# @app.route("/profile", methods=["GET", "POST"])
# def profile():
#     return profile_py.profile_func(CONST_USERNAME, CONST_COIN)


if __name__ == "__main__":
    app.run(debug=True)