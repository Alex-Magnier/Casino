# Cahier des charges UI/UX — Roulex's Casino

**Projet :** Roulex's Casino  
**Version :** 1.0 — Proposition initiale  
**Type :** Plateforme web de jeux de casino fictifs  
**Référence :** https://github.com/Alex-Magnier/casino

## 1. Présentation du projet

Roulex's Casino est un projet collaboratif étudiant ayant pour objectif de développer une plateforme de jeux de casino en ligne fonctionnant exclusivement avec une monnaie virtuelle.

Le projet est réalisé dans un objectif pédagogique, afin de mettre en pratique le développement frontend, le développement backend et le design d'interface.

Aucun dépôt, retrait ou pari en argent réel ne sera possible.

### Répartition des responsabilités

- **Frontend :** intégration HTML5, CSS3 et JavaScript.
- **Backend :** Python avec Flask, gestion des utilisateurs, des profils et des mécaniques des jeux.
- **UI/UX Design :** création des maquettes, de l'identité graphique et des composants visuels grâce à Figma.

## 2. Objectifs du design

L'interface devra proposer une expérience visuelle moderne et immersive, inspirée des plateformes de jeux et de l'univers graphique des casinos.
<!-- INFORMATION : Cette page est temporraire elle sera remplacé par le design final version actuelle v0.1 -->
Les principales émotions recherchées sont :

- Le divertissement et l'amusement.
- L'enthousiasme lors des parties.
- Le prestige associé à l'univers des casinos.
- La satisfaction liée à la progression et aux récompenses virtuelles.
- L'addiction à la plateforme pour permettre de faire rester l'utilisateur.

Le design devra rester clair, accessible et facile à utiliser.

## 3. Direction artistique

**Style recherché :** Dark Mode, Neon, Casino moderne. (Voir exemple tout en bas)

L'interface doit privilégier un arrière-plan sombre mais agréable pour les yeux, des surfaces légèrement contrastées, des accents violets et des éléments dorés, ne pas hesiter a s'inspirer des modéles joints.

### Palette indicative 
Au choix ceci est un simple exemple

| Couleur | Code HEX | Utilisation |
|---|---|---|
| Noir | #0D0D10 | Fond principal |
| Gris sombre | #19191F | Surfaces et cartes |
| Violet | #9146FF | Identité et actions principales |
| Or | #F5C451 | Jetons, monnaie virtuelle |
| Vert | #32D49D | Gains |
| Rouge | #FF5964 | Pertes et alertes |
| Blanc | #F8F8FA | Texte principal |
| Gris clair | #A1A1AA | Texte secondaire |

La palette pourra être affinée par le designer, tout en conservant une identité cohérente avec le logo qui sera crée.

### Typographies

Utiliser deux familles de polices au maximum :

- **Sora :** titres, chiffres importants et éléments de marque.
- **Inter :** navigation, boutons, descriptions et formulaires.

Les typographies devront être disponibles sur Google Fonts.

## 4. Architecture des pages

### Page d'accueil

L'accueil devra contenir :

- Une barre de navigation ou une sidebar.
- Le logo et le nom du site.
- Un accès aux jeux.
- Le solde virtuel du joueur connecté.
- Une section présentant les jeux disponibles.
- Une section présentant les jeux à venir.
- Un aperçu du classement.
- Un accès à la documentation et au profil.

### Connexion et inscription

Création de deux interfaces de formulaires comprenant :

- Nom d'utilisateur.
- Mot de passe.
- Confirmation du mot de passe pour l'inscription.
- Boutons de validation.
- Messages d'erreur ou de confirmation.

### Catalogue des jeux

Présentation des différents jeux sous forme de cartes :

- Pile ou Face.
- Devine le nombre.
- Roulette.
- Blackjack (à venir).
- Machines à sous (évolution possible).

Chaque carte devra disposer d'un titre, d'une illustration, d'une brève description et d'un indicateur de disponibilité. Comme une vraie carte.

### Interface de jeu

Une structure commune devra être prévue pour les jeux :

- Titre du jeu.
- Solde virtuel.
- Zone de jeu principale.
- Sélection de la mise virtuelle.
- Bouton pour lancer une partie.
- Affichage des résultats.
- Indication des gains ou pertes.
- Accès aux règles.

### Profil

- Pseudonyme.
- Avatar ou icône.
- Solde virtuel.
- Nombre de parties jouées.
- Nombre de victoires et défaites.
- Statistiques personnelles.

### Leaderboard

- Classement des joueurs.
- Pseudonyme.
- Solde ou score virtuel.
- Position du joueur connecté.

### Paramètres et documentation

- Modification des informations du profil.
- Préférences d'interface.
- Règles des jeux.
- Informations sur le projet.
- Crédits et contributeurs.
- Mentions précisant l'absence d'argent réel.

## 5. Composants graphiques à concevoir

Le designer devra créer des composants cohérents et réutilisables :

- Boutons primaires, secondaires et désactivés.
- Champs de formulaire.
- Cartes de jeux.
- Cartes de statistiques.
- Sidebar et navigation.
- Fenêtres modales.
- Notifications.
- Tableau de classement.
- Badges de statut.
- Jetons virtuels.
- Écrans de résultat : victoire, défaite et égalité.

Prévoir les états normal, survol, focus, actif et désactivé lorsque nécessaire. (Optionnel mais si possible c'est mieux)

## 6. Responsive design

Le site devra être pensé en priorité pour ordinateur, une version pour écrans mobiles sera à venir pour plustard

Maquettes demandées :

- Desktop : 1440 px.

L'interface doit rester lisible sans que les éléments soient les uns sur les autres et fonctionnelle quelle que soit la taille de l'écran.

## 7. Animations et interactions

Le design pourra prévoir :

- Des transitions légères au survol des boutons.
- Des animations de cartes.
- Des animations de résultat de partie.
- Des effets visuels discrets autour de la monnaie virtuelle.

Les animations devront rester sobres et respecter une éventuelle préférence utilisateur de réduction des animations.

## 8. Contraintes techniques

Le frontend sera réalisé principalement en HTML5 et CSS3, puis enrichi avec JavaScript.

Le backend utilisera Python et Flask.

La maquette devra donc pouvoir être réalisable avec ces langages, si un il y a un doute ne pas hesiter a demander

## 9. Livrables attendus

Le designer devra fournir :

1. Un fichier Figma organisé.
2. Un design system comprenant couleurs, typographies, espacements et composants.
3. Une maquette de page d'accueil.
4. Une maquette de page de jeu.
5. Une maquette de connexion et d'inscription.
6. Une maquette de profil.
7. Une maquette de leaderboard.
8. Les icônes et illustrations originales ou libres d'utilisation.
9. Les spécifications utiles à l'intégration HTML/CSS.

## 10. Critères de validation

Une maquette sera considérée comme validée lorsque :

- L'identité visuelle est cohérente sur toutes les pages.
- Les utilisateurs comprennent facilement la navigation.
- Les informations importantes sont bien hiérarchisées.
- Les composants peuvent être réutilisés.
- Les contrastes assurent une bonne lisibilité.
- Les fonctionnalités prévues peuvent être développées avec la stack retenue.
- La plateforme indique clairement que les crédits sont fictifs.

## 11. Inspirations

La référence principale est le template casino fourni par l'équipe.

Il sert d'inspiration pour la disposition des éléments, les cartes de jeux, la navigation et l'ambiance graphique.

L'objectif reste de créer une identité originale pour Roulex's Casino.

![Description](https://cdn.discordapp.com/attachments/1549197233092825119/1564729493921206362/image.png?ex=6ae25366&is=6ae101e6&hm=bbff8c9312947e86e260eaccf7f57d8ce83ebf745f39ee7d075055efc6e38d84&)

![Description] (https://www.behance.net/gallery/251954225/Casino-Website-Gambling-Platform)


![Description](https://cdn.discordapp.com/attachments/1549197233092825119/1564729753393561773/image.png?ex=6ae253a4&is=6ae10224&hm=e39d24677e57a3d0f0089b213ae7ddfb2c19df017c545171a603b5ed0681b6f3&)

![Description](https://cdn.discordapp.com/attachments/1549197233092825119/1564730277207744523/1000_F_1935630961_zZx4dnRGaWcL6yPRnz3L2Ka3JAzzkZA5.png?ex=6ae25421&is=6ae102a1&hm=75cf502484f602bcb9ca51b9443485e2f8e7b2f3a5742a2859c4fc3556b7cde0&)
