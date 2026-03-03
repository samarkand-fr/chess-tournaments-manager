"""Module de la vue (interface utilisateur en console)."""
import re
from datetime import date, datetime
from tabulate import tabulate


class View:
    """Classe de vue pour l'affichage et la saisie utilisateur.

    Gère toutes les interactions avec l'utilisateur via la console,
    incluant l'affichage de menus, de données, et la capture d'entrées.
    """
    @staticmethod
    def display_main_menu():
        """Affiche le menu principal et retourne le choix utilisateur.

        Returns:
            str: Le choix de l'utilisateur.
        """
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
        """Affiche le menu de gestion d'un tournoi.

        Args:
            tournament_name (str): Nom du tournoi.
            status_info (str): Information sur l'état actuel du tournoi.

        Returns:
            str: Le choix de l'utilisateur.
        """
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
        """Demande les informations d'un nouveau joueur avec validation.

        Valide :
        - Prénom et nom : uniquement lettres, espaces, tirets, apostrophes.
        - Date de naissance : format YYYY-MM-DD valide.
        - Chess ID : format AB12345 (2 lettres + 5 chiffres).

        Returns:
            dict: Dictionnaire contenant les données du joueur.
        """
        # Modèle pour les noms (lettres accentuées acceptées)
        name_pattern = re.compile(r"^[A-Za-zÀ-ÿ\s'\-]+$")
        # Modèle pour l'identifiant national d'échecs
        chess_id_pattern = re.compile(r'^[A-Z]{2}\d{5}$')

        while True:
            print("\n--- NEW PLAYER ---")

            # --- Validation du prénom ---
            while True:
                first_name = input("First Name: ").strip()
                if not first_name:
                    print("[ERROR] First name cannot be empty.")
                elif not name_pattern.match(first_name):
                    print(
                        "[ERROR] First name must contain only letters, "
                        "spaces, hyphens or apostrophes."
                    )
                else:
                    break

            # --- Validation du nom de famille ---
            while True:
                last_name = input("Last Name: ").strip()
                if not last_name:
                    print("[ERROR] Last name cannot be empty.")
                elif not name_pattern.match(last_name):
                    print(
                        "[ERROR] Last name must contain only letters, "
                        "spaces, hyphens or apostrophes."
                    )
                else:
                    break

            # --- Validation de la date de naissance ---
            while True:
                birth_date = input("Birth Date (DD/MM/YYYY): ").strip()
                try:
                    datetime.strptime(birth_date, "%d/%m/%Y")
                    break
                except ValueError:
                    print("[ERROR] Invalid date format. Please use DD/MM/YYYY.")

            # --- Validation de l'identifiant national d'échecs ---
            while True:
                chess_id = input(
                    "Chess ID (format: AB12345 - 2 letters + 5 digits): "
                ).upper().strip()
                if chess_id_pattern.match(chess_id):
                    break
                else:
                    print(
                        "[ERROR] Invalid format! Chess ID must be "
                        "2 uppercase letters followed by 5 digits (e.g., AB12345)."
                    )

            # --- Confirmation ---
            print("\n--- CONFIRMATION ---")
            print(f"First Name : {first_name}")
            print(f"Last Name  : {last_name}")
            print(f"Birth Date : {birth_date}")
            print(f"Chess ID   : {chess_id}")
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
        """Demande les informations d'un nouveau tournoi avec validation.

        Valide :
        - Nom et lieu : non vides, uniquement texte.
        - start_date : format DD/MM/YYYY et >= date d'aujourd'hui.
        - end_date   : format DD/MM/YYYY et >= start_date.
        - num_rounds : entier positif (défaut 4).

        Returns:
            dict: Dictionnaire contenant les données du tournoi.
        """
        # Modèle pour un texte non numérique (noms / lieux)
        name_pattern = re.compile(r"^[A-Za-zÀ-ÿ0-9\s'\-\.]+$")
        today = date.today()
        # Format d'affichage de la date du jour pour les invites
        today_str = today.strftime("%d/%m/%Y")

        while True:
            print("\n--- NEW TOURNAMENT ---")

            # --- Validation du nom du tournoi ---
            while True:
                name = input("Name: ").strip()
                if not name:
                    print("[ERROR] Tournament name cannot be empty.")
                elif not name_pattern.match(name):
                    print("[ERROR] Tournament name contains invalid characters.")
                else:
                    break

            # --- Validation du lieu ---
            while True:
                location = input("Location: ").strip()
                if not location:
                    print("[ERROR] Location cannot be empty.")
                else:
                    break

            # --- Validation de la date de début (>= aujourd'hui) ---
            while True:
                start_date_str = input(
                    f"Start Date (DD/MM/YYYY, >= {today_str}): "
                ).strip()
                try:
                    start_dt = datetime.strptime(start_date_str, "%d/%m/%Y").date()
                    if start_dt < today:
                        print(
                            f"[ERROR] Start date must be today ({today_str}) "
                            "or in the future."
                        )
                    else:
                        break
                except ValueError:
                    print("[ERROR] Invalid date format. Please use DD/MM/YYYY.")

            # --- Validation de la date de fin (>= start_date) ---
            while True:
                end_date_str = input(
                    f"End Date (DD/MM/YYYY, >= {start_date_str}): "
                ).strip()
                try:
                    end_dt = datetime.strptime(end_date_str, "%d/%m/%Y").date()
                    if end_dt < start_dt:
                        print(
                            "[ERROR] End date must be on or after "
                            f"the start date ({start_date_str})."
                        )
                    else:
                        break
                except ValueError:
                    print("[ERROR] Invalid date format. Please use DD/MM/YYYY.")

            # --- Description libre (optionnelle) ---
            description = input("Description (optional): ").strip()

            # --- Nombre de rounds ---
            while True:
                raw = input("Number of Rounds (default 4): ").strip() or "4"
                try:
                    num_rounds = int(raw)
                    if num_rounds < 1:
                        print("[ERROR] Number of rounds must be at least 1.")
                    else:
                        break
                except ValueError:
                    print("[ERROR] Please enter a valid integer.")

            # --- Confirmation ---
            print("\n--- CONFIRMATION ---")
            print(f"Name           : {name}")
            print(f"Location       : {location}")
            print(f"Start Date     : {start_date_str}")
            print(f"End Date       : {end_date_str}")
            print(f"Description    : {description}")
            print(f"Number of Rnds : {num_rounds}")

            confirm = input("Is this information correct? (y/n): ")
            if confirm.lower() == 'y':
                break

        return {
            "name": name,
            "location": location,
            "start_date": start_date_str,
            "end_date": end_date_str,
            "description": description,
            "num_rounds": num_rounds
        }

    @staticmethod
    def display_players(players):
        """Affiche une liste de joueurs sous forme de tableau.

        Args:
            players (list): Liste d'objets Player à afficher.
        """
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
        """Affiche une liste de tournois sous forme de tableau.

        Args:
            tournaments (list): Liste d'objets Tournament à afficher.
        """
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
        """Affiche un message d'information.

        Args:
            message (str): Message à afficher.
        """
        print(f"\n[INFO] {message}")

    @staticmethod
    def display_error(message):
        """Affiche un message d'erreur.

        Args:
            message (str): Message d'erreur à afficher.
        """
        print(f"\n[ERROR] {message}")

    @staticmethod
    def get_user_input(prompt):
        """Demande une entrée à l'utilisateur.

        Args:
            prompt (str): Message d'invite.

        Returns:
            str: L'entrée de l'utilisateur.
        """
        return input(prompt)

    @staticmethod
    def display_matches_for_scoring(matches):
        """Affiche les matchs d'un tour pour la saisie des scores.

        Args:
            matches (list): Liste d'objets Match à afficher.
        """
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
    def display_rankings(sorted_players, scores, tournament_name):
        """Affiche le classement des joueurs sous forme de tableau tabulaire.

        Args:
            sorted_players (list): Joueurs triés par score décroissant.
            scores (dict): Dictionnaire {chess_id: score}.
            tournament_name (str): Nom du tournoi.
        """
        print(f"\n--- CLASSEMENT : {tournament_name} ---")
        if not sorted_players:
            print("Aucun joueur inscrit.")
            return

        table_data = []
        for i, p in enumerate(sorted_players, 1):
            table_data.append([
                i,
                f"{p.first_name} {p.last_name}",
                p.chess_id,
                scores.get(p.chess_id, 0)
            ])

        print(tabulate(
            table_data,
            headers=["#", "Joueur", "ID", "Score"],
            tablefmt="fancy_grid"
        ))

    @staticmethod
    def display_rounds_report(rounds):
        """Affiche les rounds et matchs d'un tournoi sous forme tabulaire.

        Args:
            rounds (list): Liste d'objets Round à afficher.
        """
        if not rounds:
            print("Aucun round joué.")
            return

        for round_obj in rounds:
            print(f"\n  {round_obj.name}")
            print(f"  Début : {round_obj.start_time}  |  Fin : {round_obj.end_time or 'en cours'}")

            if not round_obj.matches:
                print("  (Aucun match dans ce round.)")
                continue

            table_data = []
            for i, match in enumerate(round_obj.matches, 1):
                p1 = match.player1
                p2 = match.player2
                p1_name = (
                    p1.last_name if hasattr(p1, 'last_name')
                    else p1.get('last_name', 'Unknown')
                )
                p2_name = (
                    p2.last_name if hasattr(p2, 'last_name')
                    else p2.get('last_name', 'Unknown')
                )
                score_txt = f"{match.score1} - {match.score2}"
                status = "Terminé" if match.score1 + match.score2 > 0 else "En attente"
                table_data.append([i, f"{p1_name} vs {p2_name}", score_txt, status])

            print(tabulate(
                table_data,
                headers=["#", "Match", "Score", "Statut"],
                tablefmt="fancy_grid"
            ))

    @staticmethod
    def display_tournament_details(tournament):
        """Affiche les détails d'un tournoi sous forme de tableau.

        Args:
            tournament (Tournament): Le tournoi à afficher.
        """
        table_data = [
            ["Nom", tournament.name],
            ["Lieu", tournament.location],
            ["Dates", f"Du {tournament.start_date} au {tournament.end_date}"],
            ["Tours", tournament.num_rounds],
            ["Description", tournament.description or "N/A"]
        ]

        print(tabulate(
            table_data,
            headers=["Attribut", "Valeur"],
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
    def display_round_selection(rounds):
        """Affiche la liste des rounds pour permettre une sélection.

        Args:
            rounds (list): Liste d'objets Round à afficher.
        """
        print("\n--- SELECT ROUND ---")
        for i, round_obj in enumerate(rounds, 1):
            unscored = sum(
                1 for m in round_obj.matches
                if m.score1 == 0 and m.score2 == 0
            )
            status = "Complete" if unscored == 0 else f"{unscored} pending"
            print(f"{i}. {round_obj.name} - {status}")

    @staticmethod
    def display_scoring_prompt(p1_name, p2_name):
        """Affiche le titre du match sur le point d'être scoré.

        Args:
            p1_name (str): Nom du premier joueur.
            p2_name (str): Nom du deuxième joueur.
        """
        print(f"\nScoring: {p1_name} vs {p2_name}")

    @staticmethod
    def display_report_header(title):
        print(f"\n=== {title} ===")

    @staticmethod
    def pause():
        """Met en pause et attend que l'utilisateur appuie sur Entrée."""
        input("\nPress Enter to continue...")
