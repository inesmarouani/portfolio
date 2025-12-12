# Back-end — WildAIprint

## Présentation

Ce dossier contient la partie **back-end** de l'application WildAIprint.  
Elle comprend l'API Flask, le modèle de reconnaissance d’empreintes, et la base de données.

## Sommaire

- [Back-end — WildAIprint](#back-end--wildaiprint)
  - [Présentation](#présentation)
  - [Sommaire](#sommaire)
  - [Structure](#structure)
  - [Technologies utilisées](#technologies-utilisées)
  - [Tests](#tests)
  - [Lancer l'application avec Docker](#lancer-lapplication-avec-docker)
    - [Prérequis](#prérequis)
    - [Démarrage](#démarrage)
    - [Accès](#accès)
    - [Arrêter les conteneurs](#arrêter-les-conteneurs)

## Structure

```
│       ├── app.py                      ← back-end FastAPI
│       ├── best_model.h5               ← modèle IA
│       ├── infos_complementaires.db    ← base de données SQLite
```

## Technologies utilisées

- fastapi==0.116.1
- numpy==2.3.3
- Pillow==11.3.0
- SQLAlchemy==2.0.43
- tensorflow==2.20.0
- SQLite
- Docker

## Tests

Les tests sont dans le dossier `tests/`.  
Pour les exécuter :

```bash
pytest
```

## Lancer l'application avec Docker

Ce projet est conçu pour être exécuté via Docker et Docker Compose afin de lancer à la fois le back et le front.  
Toutes ces commandes doivent être lancées dans un terminal (Invite de commandes ou Anaconda Prompt) depuis la racine du projet.

### Prérequis
- [Docker Desktop](https://www.docker.com/) installé et lancé
- [Docker Compose](https://docs.docker.com/compose/) installé
- Aucun conteneur en cours d’exécution sur les mêmes ports

### Démarrage

```bash
docker-compose build
docker-compose up
```

Cela va construire et démarrer tous les services (API, front, etc.).

### Accès

- API (back-end) : [http://localhost:5000](http://localhost:5000)
- Interface web (front-end) : [http://localhost:3000](http://localhost:3000)

### Arrêter les conteneurs

```bash
docker-compose down
```

> L’application back est lancée depuis `app.py`.
