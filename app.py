import server.login_py as login_py
import server.register_py as register_py
import server.profile_py as profile_py
from flask import Flask, render_template, request

CONST_USER = None

app = Flask(__name__)

# ROUTES DE REDIRECTION 

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/register_page", methods=["GET", "POST"])
def register_page():
    return render_template("register.html")

@app.route("/login_page", methods=["GET", "POST"])
def login_page():
    return render_template("login.html")

@app.route("/profile_page", methods=["GET", "POST"])
def profile_page():
    return render_template("profile.html", username = CONST_USER["username"], name = CONST_USER["name"], coin = CONST_USER["coin"])


# ROUTES LOGIN / REGISTER

@app.route("/register", methods=["GET", "POST"])
def register():
    temp = register_py.register_func()
    return render_template("register.html", nom = temp)

@app.route("/login", methods=["GET", "POST"])
def login():
    temp = login_py.login_func()
    global CONST_USER
    CONST_USER = temp[1]
    return render_template("login.html", msg=temp[0])

@app.route("/change_info", methods=["GET", "POST"])
def change_info():
    global CONST_USER
    CONST_USER = profile_py.change_info_func(CONST_USER)
    return render_template("profile.html", username = CONST_USER["username"], name = CONST_USER["name"], coin = CONST_USER["coin"])

if __name__ == "__main__":
    app.run(debug=True)