# Roulex Casino V0.1

> **INFORMATION :** Le design et les mises en page actuelles sont temporaires et en attente d'une refonte graphique.

## 🚀 Liste des idées globales et détails du projet

### Outils utilisés

* **Backend :** Python, Flask
* **Frontend :** HTML5, CSS3, JavaScript
* **Base de données / Stockage :** JSON (`utilisateurs.json`, `logs.json`)
* **Environnement :** VS Code

---

### 🎮 Fonctionnalités

#### Premier lancement & Authentification
* **Page de Connexion / Inscription (`index.html`) :** Permet à l'utilisateur de se connecter ou de créer un compte.
* **Gestion des Profils (`register_py.py`, `login_py.py`) :** Création et vérification automatisées dans `data/utilisateurs.json`.
* **Traçabilité (`logs.py`) :** Historique des actions enregistré dans `data/logs.json`.

#### Menu principal & Profil (`index.html`, `profile.html`)
L'utilisateur a accès aux sections suivantes :

* **Boutique** *(À venir plus tard)*
* **Jouer** (Jeux disponibles ou en cours de développement) :
  * [ ] Pile ou Face
  * [ ] Devine le nombre
  * [ ] Blackjack *(Prévu)*
  * [ ] Roulette
  * [ ] ...
* **Paramètres / Profil (`profile_py.py`)** :
  * [x] Changer son pseudo
  * [x] Changer son mot de passe
  * [ ] Réinitialiser le profil
  * [ ] ...
* **Login / Register (`login_py.py` et `register_py.py` )** :
  * [x] S'enregistrer [nom, pseudo, mdp]
  * [x] Se connecter  [pseudo, mdp]
> **Note :** Une page dédiée regroupant les règles des jeux, les mentions légales, les remerciements et les sources est prévue.

---

## 📁 Arborescence réelle du projet

```text
Casino/
├── app.py                 # Application principale Flask
├── POUR LE FRONTEND.txt   # Instruction pour le frontend 
├── README.md              # Ce fichier markdown            
│
├── server/                # Modules Python
│   │
│   ├── login_py.py        # Gestion de la connexion
│   ├── register_py.py     # Gestion de l'inscription
│   ├── profile_py.py      # Gestion des paramètres de profil
│   └── logs.py            # Script de gestion des journaux d'événements
│
├── static/                # Fichiers statiques
│   │
│   ├── css/               # Feuilles de style CSS
│   └── imgs/              # Ressources (images, logos)
│
├── templates/             # Vues HTML (Jinja2)
│   │
│   ├── index.html         # Page d'index 
│   ├── login.html         # Page de login
│   ├── register.html      # Page d'enregistrement 
│   └── profile.html       # Page de profile
│
└── data/                  # Base de données locales
    ├── utilisateurs.json  # Données des utilisateurs 
    └── logs.json          # Historique des événements
```

---

*Développé par RouyouteDev & Alex.*<br>
*Designé par WattGab & Meitsu*