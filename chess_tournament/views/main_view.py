"""Module de la vue principale."""
from .base_view import BaseView


class MainView(BaseView):
    """Classe pour la vue du menu principal."""

    @staticmethod
    def display_main_menu():
        """Affiche le menu principal et retourne le choix utilisateur."""
        print("\n--- CHESS TOURNAMENT MANAGER ---")
        print("1. Manage Players")
        print("2. Manage Tournaments")
        print("3. Generate Reports")
        print("Q. Exit")
        return input("Select an option: ")
