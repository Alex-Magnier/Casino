import datetime

# Récupérer la date et l'heure actuelles
maintenant = datetime.datetime.now()

# Afficher le jour, l'heure, les minutes et les secondes formatés
print(maintenant.strftime("%B %d: %H:%M:%S"))