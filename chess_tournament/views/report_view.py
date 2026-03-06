"""Module de la vue pour les rapports."""
from .base_view import BaseView


class ReportView(BaseView):
    """Classe pour la vue de génération des rapports."""

    @staticmethod
    def display_reports_menu():
        """Affiche le menu de génération de rapports."""
        print("\n--- REPORTS MENU ---")
        print("1. List All Players")
        print("2. List All Tournaments")
        print("3. Tournament Details")
        print("4. Tournament Players")
        print("5. Tournament Rounds & Matches")
        print("Q. Back to Main Menu")
        return input("Select an option: ")
