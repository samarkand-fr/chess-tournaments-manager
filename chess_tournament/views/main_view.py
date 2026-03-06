"""Main view module."""
from .base_view import BaseView


class MainView(BaseView):
    """Class for the main menu view."""

    @staticmethod
    def display_main_menu():
        """Displays the main menu and returns the user's choice."""
        print("\n--- CHESS TOURNAMENT MANAGER ---")
        print("1. Manage Players")
        print("2. Manage Tournaments")
        print("3. Generate Reports")
        print("Q. Exit")
        return input("Select an option: ")
