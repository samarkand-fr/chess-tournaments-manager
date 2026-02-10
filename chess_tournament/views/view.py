"""Module de la vue (interface utilisateur en console)."""
from tabulate import tabulate


class View:
    #Classe de vue pour l'affichage et la saisie utilisateur.

    @staticmethod
    def display_main_menu():
        #Affiche le menu principal et retourne le choix utilisateur.
        print("\n--- CHESS TOURNAMENT MANAGER ---")
        print("1. Manage Players")
        print("2. Manage Tournaments")
        print("3. Generate Reports")
        print("Q. Exit")
        return input("Select an option: ")

    @staticmethod
    def display_player_menu():
        print("\n--- PLAYER MENU ---")
        print("1. Create Player")
        print("2. List Players")
        print("Q. Back to Main Menu")
        return input("Select an option: ")

    @staticmethod
    def display_tournament_menu():
        print("\n--- TOURNAMENT MENU ---")
        print("1. Create Tournament")
        print("2. List Tournaments")
        print("3. Load/Manage Tournament")
        print("Q. Back to Main Menu")
        return input("Select an option: ")

    @staticmethod
    def display_tournament_management_menu(tournament_name, status_info=""):
        #Affiche le menu de gestion d'un tournoi.

        print(f"\n--- MANAGING: {tournament_name} ---")
        if status_info:
            print(f"Status: {status_info}")
        print("1. Add Player to Tournament")
        print("2. Start Next Round")
        print("3. Enter Round Scores")
        print("4. Show Rankings")
        print("5. Show Round Scores")
        print("Q. Back to Tournament List")
        return input("Select an option: ")

    @staticmethod
    def get_player_info():
        # Demande les informations d'un nouveau joueur.

        import re

        while True:
            print("\n--- NEW PLAYER ---")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            birth_date = input("Birth Date (YYYY-MM-DD): ")

            # Créer un modèle (pattern) pour vérifier l'ID
            # ^ : Début de la chaîne
            # [A-Z]{2} : Exactement 2 lettres majuscules (ex: AB)
            # \d{5} : Exactement 5 chiffres (ex: 12345)
            # $ : Fin de la chaîne
            chess_id_pattern = re.compile(r'^[A-Z]{2}\d{5}$')
            while True:
                chess_id = input(
                    "Chess ID (format: AB12345 - 2 letters + 5 digits): "
                ).upper()
                # Vérifier si l'ID correspond au modèle
                if chess_id_pattern.match(chess_id):
                    break
                else:
                    print(
                        "[ERROR] Invalid format! Chess ID must be "
                        "2 uppercase letters followed by 5 digits (e.g., AB12345)"
                    )
            
            # Confirmation
            print("\n--- CONFIRMATION ---")
            print(f"First Name: {first_name}")
            print(f"Last Name: {last_name}")
            print(f"Birth Date: {birth_date}")
            print(f"Chess ID: {chess_id}")
            confirm = input("Is this information correct? (y/n): ")
            if confirm.lower() == 'y':
                break

        return {
            "first_name": first_name,
            "last_name": last_name,
            "birth_date": birth_date,
            "chess_id": chess_id
        }

    @staticmethod
    def get_tournament_info():
        while True:
            print("\n--- NEW TOURNAMENT ---")
            name = input("Name: ")
            location = input("Location: ")
            start_date = input("Start Date (YYYY-MM-DD): ")
            end_date = input("End Date (YYYY-MM-DD): ")
            description = input("Description: ")
            try:
                num_rounds = int(input("Number of Rounds (default 4): ") or 4)
            except ValueError:
                num_rounds = 4

            # Confirmation
            print("\n--- CONFIRMATION ---")
            print(f"Name: {name}")
            print(f"Location: {location}")
            print(f"Start Date: {start_date}")
            print(f"End Date: {end_date}")
            print(f"Description: {description}")
            print(f"Number of Rounds: {num_rounds}")
            
            confirm = input("Is this information correct? (y/n): ")
            if confirm.lower() == 'y':
                break

        return {
            "name": name,
            "location": location,
            "start_date": start_date,
            "end_date": end_date,
            "description": description,
            "num_rounds": num_rounds
        }

    @staticmethod
    def display_players(players):
        # Affiche une liste de joueurs sous forme de tableau.
    
        print("\n--- PLAYERS LIST ---")
        if not players:
            print("No players found.")
            return

        table_data = []
        # 'enumerate(players, 1)' nous donne l'index (commençant à 1) et le joueur
        for i, player in enumerate(players, 1):
            table_data.append([
                i, player.first_name, player.last_name,
                player.birth_date, player.chess_id
            ])

        print(tabulate(
            table_data,
            headers=["#", "First Name", "Last Name", "Birth Date", "ID"],
            tablefmt="fancy_grid"
        ))

    @staticmethod
    def display_tournaments(tournaments):
        # Affiche une liste de tournois sous forme de tableau.

        print("\n--- TOURNAMENTS LIST ---")
        if not tournaments:
            print("No tournaments found.")
            return

        table_data = []
        for i, t in enumerate(tournaments, 1):
            table_data.append([
                i, t.name, t.location, t.start_date,
                t.end_date, t.current_round, t.num_rounds
            ])

        print(tabulate(
            table_data,
            headers=["#", "Name", "Location", "Start", "End", "Rnd", "Max"],
            tablefmt="fancy_grid"
        ))

    @staticmethod
    def display_message(message):
        # Affiche un message d'information.

        print(f"\n[INFO] {message}")

    @staticmethod
    def display_error(message):
        # Affiche un message d'erreur.

        print(f"\n[ERROR] {message}")

    @staticmethod
    def get_user_input(prompt):
        # Demande une entrée à l'utilisateur.
        return input(prompt)

    @staticmethod
    def display_matches_for_scoring(matches):
        # Affiche les matchs d'un tour pour la saisie des scores.

        print("\n--- CURRENT ROUND MATCHES ---")
        if not matches:
            print("No matches in this round.")
            return

        table_data = []
        for i, match in enumerate(matches, 1):
            p1 = match.player1
            p2 = match.player2

            p1_name = p1.last_name if hasattr(p1, 'last_name') else p1.get('last_name', 'Unknown')
            p2_name = p2.last_name if hasattr(p2, 'last_name') else p2.get('last_name', 'Unknown')

            score_text = f"{match.score1} - {match.score2}"
            status = "Finished" if match.score1 + match.score2 > 0 else "Pending"

            table_data.append([i, f"{p1_name} vs {p2_name}", score_text, status])

        print(tabulate(
            table_data,
            headers=["#", "Match", "Score", "Status"],
            tablefmt="fancy_grid"
        ))

    @staticmethod
    def display_reports_menu():
        print("\n--- REPORTS MENU ---")
        print("1. List All Players")
        print("2. List All Tournaments")
        print("3. Tournament Details")
        print("4. Tournament Players")
        print("5. Tournament Rounds & Matches")
        print("Q. Back to Main Menu")
        return input("Select an option: ")

    @staticmethod
    def display_report_header(title):
        print(f"\n=== {title} ===")

    @staticmethod
    def pause():
        """Met en pause et attend que l'utilisateur appuie sur Entrée."""
        input("\nPress Enter to continue...")
