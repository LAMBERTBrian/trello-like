# Trello-like, Projet NSI

## Installation

### 1. Cloner le répertoire
Pour cloner le répertoire, télécharger git bash, et effectuer la commande suivante:

git clone https://github.com/LAMBERTBrian/trello-like



### 2. Lancer le serveur backend
1. Installer Python 3. 
2. Installer les dépendences suivantes: Flask
3. Dans un terminal, aller dans le dossier 

backend/api


4. Effectuer la commande suivante 

flask --app run main



### 3. Lancer l'application web
1. Installer NodeJS
2. Dans un terminal, aller dans le dossier 

frontend/app


3. Installer les dépendences avec la commandes 

npm install


4. Lancer l'application en développement 

npm run dev

﻿

# Comment cela fonctionne ?

## Fonctionnement

### 1. Se créer un compte

Il faut une adresse e-mail, ensuite un nom d'utilisateur, puis un mot de passe

### 2. Les bases de données

Elles se caractérisent par les tables Comment, List, Member, Task, Team, User, et sqlite_sequence

### 3. L'utilisation de l'application

Lorsque l'utilisateur crée un mot de passe sur l'application, il doit contenir au moins plus de huit caractères, une majuscule, ainsi qu'un caractère spécial. Les tâches sont attribuées aux personnes de l'équipe, avec plusieurs états ou graphique, pour savoir si cela a été fait ou non. Les utilisateurs ont différents rôles, membre ou administrateur, ils peuvent modifier une tâche et la supprimer. Grâce aux commentaires, on peut communiquer entre les différents membres du groupe. C'est un site web qui sert à gérer les projets.
