"""Report view module."""
from .base_view import BaseView


class ReportView(BaseView):
    """Class for the report generation view."""

    @staticmethod
    def display_reports_menu():
        """Displays the report generation menu."""
        print("\n--- REPORTS MENU ---")
        print("1. List All Players")
        print("2. List All Tournaments")
        print("3. Tournament Details")
        print("4. Tournament Players")
        print("5. Tournament Rounds & Matches")
        print("Q. Back to Main Menu")
        return input("Select an option: ")
