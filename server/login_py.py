from flask import Flask, render_template, request
from . import logs
import json
import os

def login_func():
        """ Fonction qui gere le login, le retour dépend de si la connexion est réussie ou pas

        :return: SI LOGIN TRUE:    str, str, int
        :return: SI LOGIN FALSE:   str, None, None"""
        username_login = request.form.get("username_login")
        password_login = request.form.get("password_login")
        # RECUP LA LISTE DES USERS DANS LE JSON
        basedir = os.path.abspath(os.path.dirname(__file__))
        filepath = os.path.join(basedir, ".." , 'data', 'utilisateurs.json')


        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                users = json.load(f)

        # parcours de la liste des utilisateurs
        # structure elt = {"username":"str","password":"str", "coin":"int"}
        msg = False
        for elt in users:
            if elt['username'] == username_login and elt['password'] == password_login:
                COIN = elt['coin']
                USERNAME = elt['username']
                msg = True
        if msg == True:
            logs.logs_func(f"{username_login} logged")
            return f"Loggin sucessfull {username_login} !", USERNAME, COIN
        if msg == False:
            print(f"{username_login} failed !")
            return "Login failed, please try again.", None, None
