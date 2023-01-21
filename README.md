# Tasky, Projet NSI

## Installation

### 1. Cloner le répertoire

Pour cloner le répertoire, télécharger git bash, et effectuer la commande suivante:
`git clone https://github.com/LAMBERTBrian/trello-like`

### 2. Lancer l'API Flask

1. Installer Python 3.
2. Installer les dépendences avec les commandes suivantes
   `pip install flask`
   `pip install flask_cors`
3. Dans un terminal, aller dans le dossier de l'API.
   `cd backend/api`

4. Effectuer la commande suivante
   `flask run`

### 3. Lancer l'application web

1. Installer NodeJS
2. Dans un terminal, aller dans le dossier de l'App.
   `cd frontend/app`

3. Installer les dépendences avec la commandes
   `npm install`

4. Lancer l'application en développement
   `npm run dev`

# Comment cela fonctionne ?

## Fonctionnement

Le but de Tasky est de manager des tâches dans une équipe.

On peut créer un compte et se connecter sur l'Application avec un email et un mot de passe.

On peut ensuite accéder au Dashboard et ajouter des taches dans des listes que l'on peut nommer comme l'on souhaite. Il est possible d'assigner des tâches à des membres du sites. De supprimer des tâches, de déplacer des tâches etc...

Voici la maquette de l'app https://www.figma.com/file/0Ytx9RQZAXJEwhZr7052kh/Tasky?node-id=0%3A1&t=HEQDwLrgbsphhDat-1
