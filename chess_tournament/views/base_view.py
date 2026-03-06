"""Base module for the view."""


class BaseView:
    """Base class containing common display methods."""

    @staticmethod
    def display_message(message):
        """Displays an information message."""
        print(f"\n[INFO] {message}")

    @staticmethod
    def display_error(message):
        """Displays an error message."""
        print(f"\n[ERROR] {message}")

    @staticmethod
    def get_user_input(prompt):
        """Prompts the user for input."""
        return input(prompt)

    @staticmethod
    def pause():
        """Pauses and waits for the user to press Enter."""
        input("\nPress Enter to continue...")

    @staticmethod
    def display_report_header(title):
        """Displays a report header."""
        print(f"\n=== {title} ===")
