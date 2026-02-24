# Gestion de Tournoi d'Échecs

[🇬🇧 English version](README.md)
Application Python de gestion de tournois d'échecs hors-ligne.

## 📋 Description

Cette application permet de gérer des tournois d'échecs en mode console, incluant:

- La gestion des joueurs (création, liste)
- La création et gestion de tournois
- Le système de pairing suisse avec évitement des rematches
- La saisie interactive des scores
- La génération de rapports détaillés
- La persistance des données en JSON

## 🏗️ Architecture

Le projet suit le patron de conception **MVC (Model-View-Controller)** pour une séparation claire des responsabilités:

``` bash
gestion-de-tournement/
├── chess_tournament/
│   ├── models/          # Entités de données
│   │   ├── player.py    # Modèle Joueur
│   │   ├── tournament.py # Modèle Tournoi
│   │   ├── round.py     # Modèle Tour
│   │   └── match.py     # Modèle Match
│   ├── views/           # Interface utilisateur
│   │   └── view.py      # Affichage console et saisie
│   └── controllers/     # Logique métier
│       ├── main_controller.py      # Contrôleur principal
│       ├── player_controller.py    # Gestion des joueurs
│       ├── tournament_controller.py # Gestion des tournois
│       ├── report_controller.py    # Génération de rapports
│       └── database.py             # Persistance JSON
├── data/                # Données persistées
│   ├── players.json     # Base de joueurs
│   └── tournaments/     # Fichiers de tournois individuels
├── main.py              # Point d'entrée
└── requirements.txt     # Dépendances
└── .gitignore     # Exclut fichiers
└── .flake8    # Vérification
```

### Modèles (Models)

- **Player**: Représente un joueur avec prénom, nom, date de naissance et identifiant national d'échecs
- **Tournament**: Contient les informations du tournoi (nom, lieu, dates, description, nombre de tours)
- **Round**: Représente un tour avec ses matchs et horodatages
- **Match**: Oppose deux joueurs avec leurs scores respectifs

### Vues (Views)

- **View**: Gère l'affichage des menus, des tableaux (via `tabulate`), et la capture des entrées utilisateur

### Contrôleurs (Controllers)

- **MainController**: Orchestre l'application et gère le menu principal
- **PlayerController**: Gère la création et l'affichage des joueurs
- **TournamentController**: Implémente la logique des tournois (pairings, scores, classements)
- **ReportController**: Génère les différents rapports
- **Database**: Gère la persistance en JSON

## ⚙️ Installation

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes

1. **Cloner le dépôt** (ou télécharger le projet)

 ```bash
   git clone https://github.com/samarkand-fr/chess-tournaments-manager.git
   ```

   ```bash
  cd ./chess-tournaments-manager/
   ```

1. **Créer un environnement virtuel**

   ```bash
   python3 -m venv .venv
   ```

2. **Activer l'environnement virtuel**
   - **macOS/Linux**:

     ```bash
     source .venv/bin/activate
     ```

   - **Windows**:

     ```bash
     .venv\Scripts\activate
     ```

3. **Installer les dépendances**

   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Utilisation

### Lancer l'application

```bash
python main.py
```

### Navigation

L'application utilise des menus numérotés. Utilisez **Q** pour revenir au menu précédent ou quitter.

### Workflow typique

1. **Créer des joueurs**
   - Menu Principal → 1. Manage Players → 1. Create Player
   - Saisir: prénom, nom, date de naissance (DD/MM/YYYY), identifiant d'échecs

2. **Créer un tournoi**
   - Menu Principal → 2. Manage Tournaments → 1. Create Tournament
   - Saisir: nom, lieu, dates, description, nombre de tours (défaut: 4)

3. **Ajouter des joueurs au tournoi**
   - Menu Principal → 2. Manage Tournaments → 3. Load/Manage Tournament
   - Sélectionner le tournoi → 1. Add Player to Tournament

4. **Démarrer un tour**
   - Dans le menu de gestion du tournoi → 2. Start Next Round
   - Les pairings sont générés automatiquement selon le système suisse

5. **Saisir les scores**
   - Menu de gestion → 3. Enter Round Scores
   - Sélectionner un match par son numéro
   - Saisir le résultat: [1] Joueur 1 gagne, [2] Joueur 2 gagne, [0] Match nul

6. **Consulter les classements**
   - Menu de gestion → 4. Show Rankings

7. **Générer des rapports**
   - Menu Principal → 3. Generate Reports
   - Choisir parmi: liste des joueurs, liste des tournois, détails d'un tournoi, etc.

## 📊 Fonctionnalités

### Système de Pairing Suisse

- **Tour 1**: Pairings aléatoires
- **Tours suivants**:
  - Joueurs triés par score décroissant
  - Pairing des joueurs de niveaux similaires
  - Évitement des rematches (un joueur ne rencontre jamais deux fois le même adversaire)

### Système de Scores

- **Victoire**: 1.0 point
- **Match nul**: 0.5 point
- **Défaite**: 0.0 point

### Persistance des Données

- **Joueurs**: Sauvegardés dans `data/players.json`
- **Tournois**: Chaque tournoi dans `data/tournaments/<nom_tournoi>.json`
- Sauvegarde automatique après chaque modification

### Interface Améliorée

- Tableaux formatés avec `tabulate` pour une meilleure lisibilité
- Navigation intuitive avec option "Q" pour revenir en arrière
- Saisie de scores interactive par sélection de match

## 🧪 Qualité du Code

### Conformité PEP 8

Le projet respecte les standards PEP 8. Pour vérifier:

```bash
flake8
```

### Génération du Rapport Flake8 HTML

```bash
flake8 --format=html --htmldir=flake8_rapport
```

Le rapport sera disponible dans `flake8_rapport/index.html`.

### Documentation

Toutes les classes et méthodes sont documentées avec des docstrings conformes à PEP 257.

## 📦 Dépendances

- **tabulate** (2.0.2): Formatage de tableaux en console
- **flake8** (7.1.1): Vérification de la qualité du code
- **flake8-html** (0.4.3): Génération de rapports HTML

## 🔧 Configuration

Le fichier `.flake8` configure les règles de linting:

- Longueur maximale de ligne: 119 caractères
- Exclusions: `.venv`, `__pycache__`, `.git`

## 📝 Notes Techniques

- **Identifiant National d'Échecs**: Chaque joueur doit avoir un identifiant unique
- **Format de Date**: DD/MM/YYYY
- **Nombre de Joueurs**: Doit être pair pour les pairings
- **Horodatage**: Les tours enregistrent automatiquement leurs heures de début et de fin au format DD/MM/YYYY HH:MM

## 📄 Licence

Projet éducatif - OpenClassrooms

## 🔗 Ressources

- [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [PEP 257 - Docstring Conventions](https://peps.python.org/pep-0257/)
