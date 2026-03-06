"""Player view module."""
from tabulate import tabulate
from .base_view import BaseView
from ..models.validator import Validator


class PlayerView(BaseView):
    """Class for the player management view."""

    @staticmethod
    def display_player_menu():
        """Displays the player menu."""
        print("\n--- PLAYER MENU ---")
        print("1. Create Player")
        print("2. List Players")
        print("Q. Back to Main Menu")
        return input("Select an option: ")

    @staticmethod
    def get_player_info():
        """Prompts for new player information with validation."""
        while True:
            print("\n--- NEW PLAYER ---")

            while True:
                first_name = input("First Name: ").strip()
                if not Validator.is_valid_player_name(first_name):
                    print(
                        "[ERROR] First name must contain only letters, "
                        "spaces, hyphens or apostrophes and cannot be empty."
                    )
                else:
                    break

            while True:
                last_name = input("Last Name: ").strip()
                if not Validator.is_valid_player_name(last_name):
                    print(
                        "[ERROR] Last name must contain only letters, "
                        "spaces, hyphens or apostrophes and cannot be empty."
                    )
                else:
                    break

            while True:
                birth_date = input("Birth Date (DD/MM/YYYY): ").strip()
                if not Validator.is_valid_date_format(birth_date):
                    print("[ERROR] Invalid date format. Please use DD/MM/YYYY.")
                else:
                    break

            while True:
                chess_id = input("Chess ID (format: AB12345 - 2 letters + 5 digits): ").upper().strip()
                if not Validator.is_valid_chess_id(chess_id):
                    print(
                        "[ERROR] Invalid format! Chess ID must be 2 uppercase "
                        "letters followed by 5 digits (e.g., AB12345)."
                    )
                else:
                    break

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
    def display_players(players):
        """Displays a list of players in a table format."""
        print("\n--- PLAYERS LIST ---")
        if not players:
            print("No players found.")
            return

        table_data = []
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
