from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    nom_affiche = None

    if request.method == "POST":
        username_reg = request.form.get("username_register")
        password_reg = request.form.get("password_register")
        new_user = {"username": username_reg, "password": password_reg}
    
        users = [] 
        
        basedir = os.path.abspath(os.path.dirname(__file__))
        filepath = os.path.join(basedir, 'data', 'utilisateurs.json')
        
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                try:
                    users = json.load(f)
                except json.JSONDecodeError:
                    users = [] 
        users.append(new_user)

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(users, f, ensure_ascii=False, indent=4)

        if username_reg:
            print(f"\n--- Données enregistrées dans : {filepath} ---")
            print(f"Username : {username_reg}")
            print(f"Password : {password_reg}")
            print("-----------------------------------------------\n")

            nom_affiche = username_reg
            
    return render_template("index.html", nom=nom_affiche)

if __name__ == "__main__":
    app.run(debug=True)