# WildAIprint

## Présentation

WildAIprint est une application développée dans le cadre de notre formation "Developpeur IA" à Simplon AURA. L'objectif est de développer une application pour l'association française **WildAIprint**, engagée dans la protection animale dans les régions sauvages.  L'objectif de cette application est de reconnaître les empreintes de mammifères sauvages à partir de photos prises par les promeneurs en forêt. Par ce projet, l'association aimerait sensibiliser le grand public et collecter des données sur les espèces animales rencontrées en forêt.

## Problématique

> Comment permettre aux associations de sensibiliser les promeneurs de manière ludique, et de recueillir des informations sur les espèces, dans le but de préserver la faune ?

## Objectifs du projet

- Créer un modèle performant capable de reconnaître les empreintes de 13 mammifères sauvages
- Recueillir des données pour suivre l’évolution des espèces
- Sensibiliser le grand public de manière ludique
- Fournir un rendu complet et propre des livrables exigés

## Arborescence générale

```
wildaiprint-project/
├── app/
│   └── API/
│       ├── static/             ← ressources front (CSS, JS, images, uploads)
│       ├── templates/          ← pages HTML
│       ├── app.py               ← back-end FastAPI
│       ├── best_model.h5        ← modèle IA
│       ├── infos_complementaires.db
│       ├── requirements.txt
│       ├── README_front.md
│       └── README_back.md
├── docs/                        ← documentation technique
├── livrables/                   ← notebooks, MCD/MLD/MPD
├── monitoring/                  ← scripts de monitoring
├── tests/                       ← tests unitaires, d’intégration, etc.
├── conftest.py                  ← Pour que pytest trouve les modules    
└── README.md                    ← README principal du projet
```


## Livrables attendus

- Notebook ETL et modélisation
- Application (back et front)
- MCD / MLD / MPD
- Base de données
- Documentation technique
- Configuration Docker du back-end

## Documentation

- [README du Front-end](./app/API/README_front.md)
- [README du Back-end](./app/API/README_back.md)
- [Documentation technique](./docs/)

## Équipe

- Salomé Souque
- Ina Levankova
- Ines Marouani
- Mina Guinchard

