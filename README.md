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

# Portofolio Backend — API Django

Backend API REST pour un portfolio personnel, construit avec Django 5.2.2 et Django REST Framework.

Résumé rapide : gestion d'un modèle utilisateur personnalisé, gestion des projets, et formulaire de contact ; stockage des médias sur Cloudinary.

## Technologies

- Python 3.11+
- Django 5.2.2
- Django REST Framework
- Cloudinary (stockage média)
- Whitenoise (fichiers statiques)
- django-axes (protection brute-force)

## Installation (développement)

1. Cloner le dépôt et se placer dans le dossier projet :

```bash
git clone <URL_DU_REPO>
cd portofolio_backend
```

2. Créer et activer un environnement virtuel :

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Installer les dépendances :

```bash
pip install -r requirements.txt
```

4. Créer un fichier `.env` à la racine (exemple ci-dessous), puis appliquer les migrations :

```bash
python manage.py migrate
python manage.py createsuperuser  # optionnel
python manage.py runserver
```

## Exemple de fichier `.env` (minimale)

```
SECRET_KEY=change_me
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
CORS_ALLOWED_ORIGINS=http://localhost:3000
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=you@example.com
EMAIL_HOST_PASSWORD=yourpassword
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

Remplacez les valeurs par celles de votre environnement.

## Commandes utiles

- Lancer le serveur : `python manage.py runserver`
- Appliquer les migrations : `python manage.py migrate`
- Créer superutilisateur : `python manage.py createsuperuser`
- Exécuter les tests : `python manage.py test`
- Collecter les fichiers statiques : `python manage.py collectstatic --noinput`

## Configuration importante

- Le projet utilise le modèle utilisateur personnalisé `users.Utilisateur` (défini dans l'application `users`).
- En dev, la base de données par défaut est SQLite (`db.sqlite3`). Pour la production, configurez `DATABASES` via variables d'environnement.
- Les variables CORS et CSRF sont lues depuis les variables d'environnement (voir `portofolio_backend/settings.py`).

## Endpoints (quick start)

Le projet expose des endpoints via Django REST Framework. Pour obtenir la liste exacte des routes :

```bash
python manage.py show_urls  # si vous avez un utilitaire pour lister les routes
# ou naviguez vers l'API en local (DRF browsable API) : http://127.0.0.1:8000/
```

Souhaitez-vous que j'ajoute ici la liste détaillée des endpoints (ex: `/api/projets/`, `/api/users/`, `/api/contact/`)?

## Déploiement (points clés)

- Définir `DEBUG=False` et configurer `ALLOWED_HOSTS`.
- Configurer une base de données de production (Postgres, MariaDB, etc.).
- Configurer Cloudinary et les paramètres email en variables d'environnement.
- Utiliser Gunicorn (ou autre WSGI) derrière Nginx ; activer `collectstatic`.

## Contribution

Ouvrez une issue pour discuter d'un changement, puis envoyez une pull request. Respectez la structure des applications et ajoutez des tests pour des changements significatifs.

## Licence

Aucune licence fournie. Ajoutez un fichier `LICENSE` si vous souhaitez en déclarer une.

## Contact

Les templates d'email pour le contact se trouvent dans `templates/emails/`.

---

