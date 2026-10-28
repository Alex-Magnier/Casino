import json
import os

def logs_func(char :str):
    """ FONCTION QUI GERE LES LOGS
    :param char: chaine de charactere contenant le message
    :return: None """
    # CHEMAIN D'ACCES DU FICHIER LOGS JSON
    basedir = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(basedir, 'data', 'logs.json')

       
    with open(filepath, "r", encoding="utf-8") as f:
        log = json.load(f)
    print (log)
    res =[]
    char = [f"DD:HH:MM:SS {char}"]
    for elt in log:
        res.append(elt)
    res.append(char)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(res, f, indent=2)