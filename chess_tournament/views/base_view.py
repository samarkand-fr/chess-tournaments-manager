"""Module de base pour la vue."""


class BaseView:
    """Classe de base contenant les méthodes d'affichage communes."""

    @staticmethod
    def display_message(message):
        """Affiche un message d'information."""
        print(f"\n[INFO] {message}")

    @staticmethod
    def display_error(message):
        """Affiche un message d'erreur."""
        print(f"\n[ERROR] {message}")

    @staticmethod
    def get_user_input(prompt):
        """Demande une entrée à l'utilisateur."""
        return input(prompt)

    @staticmethod
    def pause():
        """Met en pause et attend que l'utilisateur appuie sur Entrée."""
        input("\nPress Enter to continue...")

    @staticmethod
    def display_report_header(title):
        """Affiche un en-tête de rapport."""
        print(f"\n=== {title} ===")
