"""Tournament view module."""
from tabulate import tabulate
from .base_view import BaseView
from ..models.validator import Validator
from datetime import date


class TournamentView(BaseView):
    """Class for the tournament management view."""

    @staticmethod
    def display_tournament_menu():
        """Displays the tournament management menu."""
        print("\n--- TOURNAMENT MENU ---")
        print("1. Create Tournament")
        print("2. List Tournaments")
        print("3. Load/Manage Tournament")
        print("Q. Back to Main Menu")
        return input("Select an option: ")

    @staticmethod
    def display_tournament_management_menu(tournament_name, status_info=""):
        """Displays the management menu for a tournament."""
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
    def get_tournament_info():
        """Prompts for new tournament information with validation."""
        today_str = date.today().strftime("%d/%m/%Y")

        while True:
            print("\n--- NEW TOURNAMENT ---")

            while True:
                name = input("Name: ").strip()
                if not Validator.is_valid_tournament_name(name):
                    print("[ERROR] Tournament name cannot be empty or contain invalid characters.")
                else:
                    break

            while True:
                location = input("Location: ").strip()
                if not Validator.is_valid_location(location):
                    print("[ERROR] Location cannot be empty.")
                else:
                    break

            while True:
                start_date_str = input(f"Start Date (DD/MM/YYYY, >= {today_str}): ").strip()
                if not Validator.is_valid_start_date(start_date_str):
                    print(
                        f"[ERROR] Start date must be today ({today_str}) "
                        "or in the future and formatted DD/MM/YYYY."
                    )
                else:
                    break

            while True:
                end_date_str = input(f"End Date (DD/MM/YYYY, >= {start_date_str}): ").strip()
                if not Validator.is_valid_end_date(start_date_str, end_date_str):
                    print(
                        "[ERROR] End date must be on or after the start date "
                        f"({start_date_str}) and formatted DD/MM/YYYY."
                    )
                else:
                    break

            description = input("Description (optional): ").strip()

            while True:
                raw = input("Number of Rounds (default 4): ").strip() or "4"
                if not Validator.is_valid_num_rounds(raw):
                    print("[ERROR] Number of rounds must be a positive integer (at least 1).")
                else:
                    num_rounds = int(raw)
                    break

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
    def display_tournaments(tournaments):
        """Displays a list of tournaments in a table format."""
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
    def display_matches_for_scoring(matches):
        """Displays round matches for score entry."""
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
        """Displays player rankings in a table format."""
        print(f"\n--- RANKING: {tournament_name} ---")
        if not sorted_players:
            print("No registered players.")
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
            headers=["#", "Player", "ID", "Score"],
            tablefmt="fancy_grid"
        ))

    @staticmethod
    def display_rounds_report(rounds):
        """Displays a tournament's rounds and matches in a table format."""
        if not rounds:
            print("No rounds played.")
            return

        for round_obj in rounds:
            print(f"\n  {round_obj.name}")
            print(f"  Start: {round_obj.start_time}  |  End: {round_obj.end_time or 'in progress'}")

            if not round_obj.matches:
                print("  (No matches in this round.)")
                continue

            table_data = []
            for i, match in enumerate(round_obj.matches, 1):
                p1 = match.player1
                p2 = match.player2
                p1_name = p1.last_name if hasattr(p1, 'last_name') else p1.get('last_name', 'Unknown')
                p2_name = p2.last_name if hasattr(p2, 'last_name') else p2.get('last_name', 'Unknown')
                score_txt = f"{match.score1} - {match.score2}"
                status = "Finished" if match.score1 + match.score2 > 0 else "Pending"
                table_data.append([i, f"{p1_name} vs {p2_name}", score_txt, status])

            print(tabulate(
                table_data,
                headers=["#", "Match", "Score", "Status"],
                tablefmt="fancy_grid"
            ))

    @staticmethod
    def display_tournament_details(tournament):
        """Displays tournament details in a table format."""
        table_data = [
            ["Name", tournament.name],
            ["Location", tournament.location],
            ["Dates", f"From {tournament.start_date} to {tournament.end_date}"],
            ["Rounds", tournament.num_rounds],
            ["Description", tournament.description or "N/A"]
        ]

        print(tabulate(
            table_data,
            headers=["Attribute", "Value"],
            tablefmt="fancy_grid"
        ))

    @staticmethod
    def display_round_selection(rounds):
        """Displays the list of rounds for selection."""
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
        """Displays the title of the match about to be scored."""
        print(f"\nScoring: {p1_name} vs {p2_name}")
