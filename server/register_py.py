from flask import Flask, render_template, request
from . import logs
import json
import os

def register_func():
    """ Fonction qui gere le register, le retour dépend de si la connexion est réussie ou pas

    :return: str, str"""
    nom_affiche = None

    if request.method == "POST":
        # RECUP INFOS DU FORM REGISTER
        username_reg = request.form.get("username_register")
        password_reg = request.form.get("password_register")
        name_reg = request.form.get("name_register")
        age_reg = request.form.get("age_register")
        new_user = {"username": username_reg, "password": password_reg, "name":name_reg, "coin":100}
        users = [] 


        # VERIFICATIONS DES DATAS
        basedir = os.path.abspath(os.path.dirname(__file__))
        filepath = os.path.join(basedir, "..", 'data', 'utilisateurs.json')
        
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                try:
                    users = json.load(f)
                except json.JSONDecodeError:
                    users = []

        # VERIFIE SI LA CHECKBOX A ETE COCHEE SINON ENREGISTREMNET ANNULE, MESSAGE D ERREUR A L UTILISATEUR
        if age_reg == "on":
            pass
        else:
                return "register failed, you must be 18 year old"
        
        # SI USERNAME DEJA PRIS ENREGISREMENT ANNULE, MESSAGE D ERREUR A L UTILISATEUR
        for elt in users:
            if username_reg in elt["username"]:
                return "register failed, username already taken"
        users.append(new_user)

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(users, f, ensure_ascii=False, indent=4)

        # SI REUSSI ENREGISTRE L UTILISATEUR ET SES DATAS
        if username_reg:
            logs.logs_func(f"{username_reg} registered")
            nom_affiche = username_reg
            
    return f"register complete {nom_affiche}"