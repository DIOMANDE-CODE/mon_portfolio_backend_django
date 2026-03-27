# Portofolio Backend

Backend Django pour un portfolio personnel — API REST pour gérer les utilisateurs, projets et contacts.

---

## Description

Ce projet est une API backend construite avec Django 5.2.2 et Django REST Framework. Il fournit des endpoints pour gérer :
- utilisateurs (modèle personnalisé `Utilisateur`)
- projets
- formulaire de contact

Il utilise SQLite en développement et Cloudinary pour le stockage des médias.

## Fonctionnalités principales

- API REST avec `djangorestframework`
- Gestion des utilisateurs personnalisée (`users`)
- Gestion des projets (`projets`)
- Formulaire de contact (`contact`)
- Stockage média sur Cloudinary
- Protection contre les attaques par force brute via `django-axes`

## Prérequis

- Python 3.11+
- git

## Installation locale

1. Cloner le dépôt :

   git clone https://github.com/DIOMANDE-CODE/mon_portfolio_backend_django.git
   cd portofolio_backend

2. Créer et activer un environnement virtuel :

   python -m venv .venv
   # Windows (PowerShell)
   .\.venv\Scripts\Activate.ps1

3. Installer les dépendances :

   pip install -r requirements.txt

4. Créer un fichier `.env` à la racine (voir `Configuration` ci-dessous).

5. Appliquer les migrations :

   python manage.py migrate

6. (Optionnel) Créer un superutilisateur :

   python manage.py createsuperuser

7. Lancer le serveur en développement :

   python manage.py runserver

## Variables d'environnement importantes

Le projet charge un fichier `.env`. Variables courantes à définir :

- `SECRET_KEY` — clé secrète Django
- `DEBUG` — `True` ou `False`
- `ALLOWED_HOSTS` — hôtes autorisés (séparés par des virgules)
- `CORS_ALLOWED_ORIGINS` — origines autorisées pour CORS (séparées par des virgules)
- `CSRF_TRUSTED_ORIGINS`
- `EMAIL_BACKEND`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_USE_TLS`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`
- `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`

## Base de données

Par défaut en développement, le projet utilise SQLite (`db.sqlite3`). Pour la production, configurez `DATABASES` via `dj-database-url` ou une autre solution et définissez les variables d'environnement appropriées.

## Collecte des fichiers statiques

Avant de déployer en production :

   python manage.py collectstatic --noinput

Le projet utilise `whitenoise` pour servir les fichiers statiques en production.

## Tests

Lancer la suite de tests :

   python manage.py test

## Structure du projet (sélection)

- `portofolio_backend/` — configuration Django (settings, urls, wsgi, asgi)
- `users/` — application utilisateur (modèle personnalisé)
- `projets/` — application gestion des projets
- `contact/` — gestion du formulaire de contact
- `templates/` — templates et emails
- `staticfiles/` — fichiers collectés

## Déploiement

Points à considérer pour la production :
- Définir `DEBUG=False` et `ALLOWED_HOSTS`
- Configurer la base de données de production
- Configurer les variables Cloudinary et email
- Utiliser un serveur WSGI (ex : Gunicorn) et un reverse-proxy (ex : Nginx)

## Contribution

Contributions bienvenues. Ouvrez une issue ou un pull request pour proposer des changements.

## Licence

Pas de licence fournie dans le dépôt. Ajouter un fichier `LICENSE` si vous souhaitez en déclarer une.

## Contact

diomandedroh79@gmail.com

---
