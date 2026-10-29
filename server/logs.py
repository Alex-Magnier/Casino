import json
import os
import datetime

def logs_func(char :str):
    """ FONCTION QUI GERE LES LOGS
    :param char: chaine de charactere contenant le message
    :return: None """


    # RECUP LA DATE "str mois" JJ: HH:MM:SS
    now = datetime.datetime.now()
    now = now.strftime("%B %d: %H:%M:%S")



    # CHEMAIN D'ACCES DU FICHIER LOGS JSON
    basedir = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(basedir, "..",'data', 'logs.json')


    with open(filepath, "r", encoding="utf-8") as f:
        log = json.load(f)
    print (log)
    res =[]
    char = [f"{now} {char}"]
    for elt in log:
        res.append(elt)
    res.append(char)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(res, f, indent=2)