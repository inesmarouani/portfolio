# Front-end — WildAIprint

## Présentation

Ce README présente la partie **front-end** de l'application WildAIprint.  
Elle permet aux utilisateurs d'interagir avec l'application (interface, navigation, visualisation des informations sur les animaux).

## Sommaire

- [Front-end — WildAIprint](#front-end--wildaiprint)
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
│       ├── static/             ← CSS, JS, images, uploads utilisateurs
│       │   ├── images/
│       │   │   ├── accueil/
│       │   │   ├── exploration/
│       │   │   ├── fiche_animal/
│       │   │   ├── header_footer/
│       │   │   ├── scan/
│       │   │   └── favicon-32x32.png
│       │   │
│       │   ├── js/
│       │   │   ├── camera.js
│       │   │   ├── decor-dot.js
│       │   │   ├── footer.js
│       │   │   └── header.js
│       │   │
│       │   ├── styles/
│       │   │   ├── exploration.css
│       │   │   ├── fiche_animal.css
│       │   │   ├── header_footer.css
│       │   │   ├── index.css
│       │   │   ├── mentions.css
│       │   │   ├── scan.css
│       │   │   └── styles.css
```

## Technologies utilisées

- HTML5 / CSS3
- JavaScript Vanilla

## Tests

- Accessibilité via Google Lighthouse et W3C Validator
- Compatibilité multi-navigateurs (Chrome, Firefox, Safari, Edge)
- Tests utilisateurs pour l'ergonomie et l'expérience utilisateur
- Tests responsive design sur différents appareils (desktop, tablette, mobile)

## Lancer l'application avec Docker

L'application complète (front + back) peut être lancée facilement grâce à Docker et Docker Compose.  
Toutes ces commandes doivent être lancées dans un terminal (Invite de commandes ou Anaconda Prompt) depuis la racine du projet.

### Prérequis
- [Docker Desktop](https://www.docker.com/) installé et lancé
- [Docker Compose](https://docs.docker.com/compose/) installé (inclus par défaut avec Docker Desktop)
- Aucun conteneur en cours d’exécution sur les mêmes ports

### Démarrage

```bash
docker-compose build
docker-compose up
```

### Accès

- Front-end : [http://localhost:3000](http://localhost:3000)
- Back-end (API) : [http://localhost:5000](http://localhost:5000)

### Arrêter les conteneurs

```bash
docker-compose down
```