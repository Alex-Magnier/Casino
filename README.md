<img src="/static/imgs/casino.png" width="200" alt="Texte alternatif">

# Roulex Casino V0.1
# INFORMATION : Le design et les mises en pages actuelles sont temporraires et en attente d'un design

### Liste des idées globales en details du projet

* Outils possible à utiliser :
    * __TKinter__ ou version __WEB__ avec __HTML5__ et __CSS3__
    * __Python__
    * __VS Code__

Premier lancement :
* Demande a l'utilisateur de choisir don pseudo
    * Création d'un fichier __JSON__ qui contiendra toutes ses informations pour les stocker et les réutiliser à chaques lancement ou chaques jeux
    <br>
* Arrivée dans un menu ou l'utilisateur aura le choix entre :
    * Boutique (À venir plus tard)
    * Jouer qui contiendra des jeux comme :
        - [ ] Pile ou Face
        - [ ] Devine le nombre
        - [ ] Black Jack (Plus tard)
        - [ ] Jeux de la roulette
        - [ ] ...
    * Paramètres
        - [ ] Changer son pseudo
        - [ ] Réinitialiser le profil
        - [ ] ...
    * ...

```Faire un fichier qui ouvre une documentation HTML5, CSS3 ou une page dédié si interface WEB direct avec toutes les régles des jeux, les mentions, remerciements et d'autres choses comme des sources etc...```


## Exemple pour l'arborescence (pas la même si interface WEB HTML5 CSS3)

        casino/
        ├── main.py                  # Fichier principal : lance le menu
        ├── menu.py                  # affichage du menu pricipal avec choix (Boutique, Jouer, Paramètres etc..)
        ├── profil.py                # création / chargement / sauvegarde       du profil
        ├── README.md                # Présentation
        │
        ├── jeux/
        │   ├── roulette.py
        │   ├── pile_ou_face.py
        │   ├── blackjack.py
        │   ├── machine_a_sous.py
        │   ├── devine_le_nombre.py
        │
        ├── utils/
        │   └── cartes.py            # Paquet / Carte, partagé par      blackjack et autre jeu
        │
        └──  data/                    # sauvegardes (ignorées par Git)
            └── profil.json

# À compléter !

```By RouyouteDev, Alex., Wattgab, Maelyneagnrl```