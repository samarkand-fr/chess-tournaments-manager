# Chess Tournament Management

[🇫🇷 Version française](README_fr.md)

Python application for offline chess tournament management.

## 📋 Description

This application allows you to manage chess tournaments in console mode, including:
- Player management (creation, listing)
- Tournament creation and management
- Swiss pairing system with rematch avoidance
- Interactive score entry
- Detailed report generation
- JSON data persistence

## 🏗️ Architecture

The project follows the **MVC (Model-View-Controller)** design pattern for a clear separation of concerns:

```
gestion-de-tournement/
├── chess_tournament/
│   ├── models/          # Data entities
│   │   ├── player.py    # Player Model
│   │   ├── tournament.py # Tournament Model
│   │   ├── round.py     # Round Model
│   │   └── match.py     # Match Model
│   ├── views/           # User interface
│   │   └── view.py      # Console display and input
│   └── controllers/     # Business logic
│       ├── main_controller.py      # Main controller
│       ├── player_controller.py    # Player management
│       ├── tournament_controller.py # Tournament management
│       ├── report_controller.py    # Report generation
│       └── database.py             # JSON persistence
├── data/                # Persisted data
│   ├── players.json     # Player database
│   └── tournaments/     # Individual tournament files
├── main.py              # Entry point
└── requirements.txt     # Dependencies
└── .gitignore     # Excluded  files
└── .flake8    # Verification 
```

### Models

- **Player**: Represents a player with first name, last name, birth date, and national chess ID
- **Tournament**: Contains tournament information (name, location, dates, description, number of rounds)
- **Round**: Represents a round with its matches and timestamps
- **Match**: Pits two players against each other with their respective scores

### Views

- **View**: Handles displaying menus, tables (via `tabulate`), and capturing user input

### Controllers

- **MainController**: Orchestrates the application and manages the main menu
- **PlayerController**: Manages player creation and display
- **TournamentController**: Implements tournament logic (pairings, scores, rankings)
- **ReportController**: Generates various reports
- **Database**: Handles JSON persistence

## ⚙️ Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Steps

1. **Clone the repository** (or download the project)
   ```bash
   git clone https://github.com/samarkand-fr/chess-tournaments-manager.git
   ```
 
  ```bash
  cd ./chess-tournaments-manager/
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv .venv
   ```

3. **Activate the virtual environment**
   - **macOS/Linux**:
     ```bash
     source .venv/bin/activate
     ```
   - **Windows**:
     ```bash
     .venv\Scripts\activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### Run the application

```bash
python main.py
```

### Navigation

The application uses numbered menus. Use **Q** to go back to the previous menu or exit.

### Typical Workflow

1. **Create players**
   - Main Menu → 1. Manage Players → 1. Create Player
   - Enter: first name, last name, birth date (YYYY-MM-DD), chess ID

2. **Create a tournament**
   - Main Menu → 2. Manage Tournaments → 1. Create Tournament
   - Enter: name, location, dates, description, number of rounds (default: 4)

3. **Add players to the tournament**
   - Main Menu → 2. Manage Tournaments → 3. Load/Manage Tournament
   - Select the tournament → 1. Add Player to Tournament

4. **Start a round**
   - In the tournament management menu → 2. Start Next Round
   - Pairings are automatically generated according to the Swiss system

5. **Enter scores**
   - Management menu → 3. Enter Round Scores
   - Select a match by its number
   - Enter the result: [1] Player 1 wins, [2] Player 2 wins, [0] Draw

6. **View rankings**
   - Management menu → 4. Show Rankings

7. **Generate reports**
   - Main Menu → 3. Generate Reports
   - Choose from: list of players, list of tournaments, tournament details, etc.

## 📊 Features

### Swiss Pairing System

- **Round 1**: Random pairings
- **Subsequent rounds**: 
  - Players sorted by descending score
  - Pairing of players with similar standings
  - Rematch avoidance (a player never meets the same opponent twice)

### Scoring System

- **Win**: 1.0 point
- **Draw**: 0.5 point
- **Loss**: 0.0 point

### Data Persistence

- **Players**: Saved in `data/players.json`
- **Tournaments**: Each tournament in `data/tournaments/<tournament_name>.json`
- Automatic saving after each modification

### Improved Interface

- Formatted tables with `tabulate` for better readability
- Intuitive navigation with "Q" option to go back
- Interactive score entry by match selection

## 🧪 Code Quality

### PEP 8 Compliance

The project respects PEP 8 standards. To verify:

```bash
flake8
```

### HTML Flake8 Report Generation

```bash
flake8 --format=html --htmldir=flake8_rapport
```

The report will be available in `flake8_rapport/index.html`.

### Documentation

All classes and methods are documented with PEP 257 compliant docstrings.

## 📦 Dependencies

- **tabulate** (2.0.2): Console table formatting
- **flake8** (7.1.1): Code quality checking
- **flake8-html** (0.4.3): HTML report generation

## 🔧 Configuration

The `.flake8` file configures the linting rules:
- Maximum line length: 119 characters
- Exclusions: `.venv`, `__pycache__`, `.git`

## 📝 Technical Notes

- **National Chess ID**: Each player must have a unique identifier
- **Date Format**: DD/MM/YYYY
- **Number of Players**: Must be even for pairings (the application handles odd numbers by leaving one player without an opponent)
- **Timestamps**: Rounds automatically record their start and end times in DD/MM/YYYY HH:MM format


## 📄 License

Educational project - OpenClassrooms

## 🔗 Resources

- [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [PEP 257 - Docstring Conventions](https://peps.python.org/pep-0257/)
