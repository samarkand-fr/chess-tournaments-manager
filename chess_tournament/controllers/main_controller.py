"""Module du contrôleur principal de l'application."""
from ..views.main_view import MainView
from .player_controller import PlayerController
from .tournament_controller import TournamentController
from .report_controller import ReportController
from .database import Database


class MainController:
    """Contrôleur principal de l'application.

    Orchestre les différents contrôleurs et gère le menu principal.

    Attributes:
        view (MainView): Instance de la vue principale.
        player_controller (PlayerController): Contrôleur des joueurs.
        tournament_controller (TournamentController): Contrôleur des tournois.
        report_controller (ReportController): Contrôleur des rapports.
        db (Database): Instance de la base de données.
    """

    def __init__(self):
        """Initialise le contrôleur principal et tous les sous-contrôleurs."""
        self.view = MainView()
        self.db = Database()
        self.player_controller = PlayerController(self.db)
        self.tournament_controller = TournamentController(
            self.player_controller, self.db
        )
        self.report_controller = ReportController(self.db)

    def run(self):
        """Lance la boucle principale de l'application.

        Affiche le menu principal et traite les choix de l'utilisateur
        jusqu'à ce qu'il choisisse de quitter.
        """
        while True:
            choice = self.view.display_main_menu()
            if choice == "1":
                self.manage_players()
            elif choice == "2":
                self.manage_tournaments()
            elif choice == "3":
                self.generate_reports()
            elif choice.upper() == "Q":
                self.view.display_message("See you Next tournament!")
                break
            else:
                self.view.display_error("Invalid selection")

    def manage_players(self):
        """Gère le menu des joueurs.

        Affiche le menu de gestion des joueurs et traite les choix
        jusqu'à ce que l'utilisateur retourne au menu principal.
        """
        while True:
            choice = self.player_controller.view.display_player_menu()
            if choice == "1":
                self.player_controller.create_player()
            elif choice == "2":
                self.player_controller.list_players()
            elif choice.upper() == "Q":
                break
            else:
                self.view.display_error("Invalid selection")

    def manage_tournaments(self):
        """Gère le menu des tournois.

        Affiche le menu de gestion des tournois et traite les choix
        jusqu'à ce que l'utilisateur retourne au menu principal.
        """
        while True:
            choice = self.tournament_controller.view.display_tournament_menu()
            if choice == "1":
                self.tournament_controller.create_tournament()
            elif choice == "2":
                self.tournament_controller.view.display_tournaments(
                    self.tournament_controller.tournaments
                )
            elif choice == "3":
                self.tournament_controller.manage_tournament()
            elif choice.upper() == "Q":
                break
            else:
                self.view.display_error("Invalid selection")

    def generate_reports(self):
        """Lance le module de génération de rapports."""
        self.report_controller.run_reports()
