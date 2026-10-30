from flask import Flask, render_template, request
from . import logs
import json
import os

def change_info_func (user :list):
    """Fonction qui change les information de l'utilisateur
    
    :param user: :list
    :return: :list:dict"""

    username = request.form.get("username_change")
    name = request.form.get("name_change")
    password = request.form.get("password_change")
    password_confirm = request.form.get("password_change_confirm")
    
    # RECUP LA LISTE DES USERS DANS LE JSON
    basedir = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(basedir, ".." , 'data', 'utilisateurs.json')
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            users = json.load(f)

    # VERIFICATION SI IL Y A CHANGEMENT
    change, change_info = False, False
    change_username = False
    old_username = user["username"]
    for elt in users:
        if elt['username'] == user["username"]:
            if username != "":
                user["username"] = username
                change = True
                change_username = True
            if name != "":
                user['name'] = name
                change_info = True
                change = True
            if password != "" and password_confirm != "":
                user["password"] = password
                change_info = True
                change = True

    # SI CHANGEMENT ON EFFACE LES ANCIENNE DONNES ET EN ECRIT DES NOUVELLES
    if change == True:
        for elt in users:
            if elt['username'] == old_username:
                users.remove(elt)
                users.append(user)
                with open(filepath, "w", encoding="utf-8") as f:
                    json.dump(users, f, ensure_ascii=False, indent=4)
    if change_username == True:
        logs.logs_func(f"{old_username} changed username to {user["username"]}")
        if change_info == True:
            logs.logs_func(f"{user["username"]} previously: {old_username} changed info")
    else:
        logs.logs_func(f"{user["username"]} changed info")
    return user