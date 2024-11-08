# GestionGarage
Cette application est une API de gestion de garage développée en Django. Elle permet de suivre les informations de chaque voiture, notamment l'immatriculation, la marque, le modèle et l'état des réparations. Cette API facilite les opérations d'ajout, de consultation, de mise à jour et de suppression des informations des véhicules dans une base de données.

# Prérequis
Avant de lancer le projet, il est nécessaire d'avoir installé Python et Django sur votre machine. Django REST Framework est également requis pour gérer les opérations de l'API.

# Configuration de la Base de Données
Ce projet utilise MySQL comme base de données. Une fois MySQL installé, créez une base de données et configurez le fichier settings.py pour y ajouter les informations de connexion. Assurez-vous de définir le nom de la base de données, l'utilisateur et le mot de passe corrects.

# Étapes pour Exécuter le Projet
Créez la base de données MySQL et connectez-vous en modifiant les paramètres dans settings.py.
Appliquez les migrations pour générer les tables dans la base de données.
Lancez le serveur de développement pour exécuter l'API.

# Fonctionnalités de l'API
L'API prend en charge les fonctionnalités de gestion des informations des voitures :

Ajouter une nouvelle voiture
Consulter la liste de toutes les voitures
Mettre à jour les informations d'une voiture spécifique
Supprimer une voiture de la base de données
