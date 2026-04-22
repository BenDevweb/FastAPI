# FastAPI — Gestionnaire d'issues

![CI](https://github.com/BenDevweb/FastAPI/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

Résumé
------
Ce projet est une API REST minimale développée avec FastAPI pour gérer des "issues" (tickets). Il fournit des routes CRUD pour créer, lire, mettre à jour et supprimer des issues, ainsi qu'un stockage simple basé sur un fichier JSON. Le code est structuré pour être clair et maintenable : séparation des schémas, du stockage, des routes et des middlewares.

Points clés
----------
- Framework : FastAPI
- Persist. légère : fichier JSON (data/issues.json)
- Middlewares : mesure du temps de requête (app/middleware/timer.py)
- Structure claire : routes, schémas et logique de stockage séparés

Arborescence principale
-----------------------
- [main.py](main.py)
- [requirements.txt](requirements.txt)
- [app/schemas.py](app/schemas.py)
- [app/storage.py](app/storage.py)
- [app/middleware/timer.py](app/middleware/timer.py)
- [routes/issues.py](routes/issues.py)
- [data/issues.json](data/issues.json)

Prérequis
---------
- Python 3.10+ recommandé
- Virtualenv ou venv pour isoler l'environnement

Installation
------------
1. Créez et activez un environnement virtuel :

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Installez les dépendances :

```powershell
pip install -r requirements.txt
```

Exécution
---------
Démarrer l'API en mode développement avec uvicorn :

```powershell
uvicorn main:app --reload
```

L'API sera accessible par défaut sur http://127.0.0.1:8000

Endpoints (détaillés)
---------------------
Base path: `/api/v1/issues`

- GET  `/api/v1/issues/` — Récupère la liste complète des issues.
	- Response: `200 OK`, liste de `IssueOut`.

- POST `/api/v1/issues/` — Crée une nouvelle issue.
	- Request body: `IssueCreate` (title, description, priority).
	- Response: `201 Created`, `IssueOut` (id, title, description, priority, status).

- GET  `/api/v1/issues/{issue_id}` — Récupère une issue par identifiant.
	- Path param: `issue_id: str`.
	- Response: `200 OK` `IssueOut` ou `404 Not Found` si introuvable.

- PUT  `/api/v1/issues/{issue_id}` — Met à jour une issue existante.
	- Path param: `issue_id: str`.
	- Request body: `IssueUpdate` (tous les champs optionnels : title, description, priority, status).
	- Response: `200 OK` `IssueOut` ou `404 Not Found`.

- DELETE `/api/v1/issues/{issue_id}` — Supprime une issue.
	- Path param: `issue_id: str`.
	- Response: `204 No Content` ou `404 Not Found`.

Consultez la documentation interactive générée par FastAPI à `/docs` pour les schémas Pydantic détaillés et des exemples de payloads.

Stockage
--------
Les données sont persistées dans [data/issues.json](data/issues.json). Le module `app/storage.py` contient la logique de lecture/écriture et les opérations atomiques nécessaires pour garder le fichier cohérent.

Middleware
----------
Le middleware `app/middleware/timer.py` enregistre la durée des requêtes et peut être utilisé pour du monitoring léger et des logs de performance.

Schémas
-------
Les entrées et sorties (validation) sont définies dans `app/schemas.py` via Pydantic. Cela permet d'avoir une API fortement typée et des réponses prévisibles.

Bonne pratique et maintenance
----------------------------
- Versionner `data/issues.json` uniquement si cela est voulu ; sinon, l'ajouter à `.gitignore` pour éviter les collisions entre environnements.
- Ajouter des tests unitaires pour `app/storage.py` et `routes/issues.py` afin d'assurer la stabilité des opérations CRUD.
- Prévoir une migration vers une base de données (SQLite/Postgres) si le volume ou la concurrence augmente.

Développement & Contribution
----------------------------
- Forkez le dépôt et ouvrez une branche par fonctionnalité ou correction de bug.
- Ouvrez une Pull Request décrivant les changements et les motivations.
- Respectez les formats de commit et ajoutez des tests lorsque c'est applicable.

Licence
-------
Ce projet est distribué sous la licence MIT. Voir le fichier [LICENSE](LICENSE) pour le texte complet.

Contact
-------
Pour toute question ou demande d'amélioration, contactez le mainteneur du projet ou ouvrez une issue dans le dépôt.

---

Faites-moi savoir si vous voulez :
- Ajouter des badges (CI, coverage)
- Générer un fichier `LICENSE`
- Compléter automatiquement la section Endpoints avec les détails exacts extraits de `routes/issues.py` (je peux analyser le fichier pour ajouter la documentation exacte)


Lien render: https://fastapi-9rcm.onrender.com/api/v1/issues/, c'est une api opensource
