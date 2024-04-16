# Utilisez l'image Python officielle comme image de base
FROM python:3.9

# Installation de Flask
RUN pip install Flask

# Copie du fichier Flask de vos exercices précédents
COPY script.py /app/script.py

# Définition du répertoire de travail
WORKDIR /app

# Commande pour exécuter votre application Flask
CMD ["python", "script.py"]
