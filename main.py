"""Point d'entrée principal de l'application de gestion de tournois d'échecs.

Ce module initialise et lance l'application en créant une instance du
contrôleur principal et en démarrant la boucle d'interaction utilisateur.
"""
from chess_tournament.controllers.main_controller import MainController


def main():
    """Lance l'application de gestion de tournois d'échecs."""
    app = MainController()
    app.run()


if __name__ == "__main__":
    main()
