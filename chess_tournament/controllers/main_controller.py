from ..views.view import View
from .player_controller import PlayerController
from .tournament_controller import TournamentController
from .report_controller import ReportController


class MainController:
    # Contrôleur principal de l'application.


    def __init__(self):
        # Initialise le contrôleur principal et tous les sous-contrôleurs.
        self.view = View()
        self.player_controller = PlayerController(self.view)
        self.tournament_controller = TournamentController(
            self.view, self.player_controller
        )
        self.report_controller = ReportController(self.view)

    def run(self):
        # Lance la boucle principale de l'application.

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
        # Gère le menu des joueurs.

        
        while True:
            choice = self.view.display_player_menu()
            if choice == "1":
                self.player_controller.create_player()
            elif choice == "2":
                self.player_controller.list_players()
            elif choice.upper() == "Q":
                break
            else:
                self.view.display_error("Invalid selection")

    def manage_tournaments(self):
        # Gère le menu des tournois.

        while True:
            choice = self.view.display_tournament_menu()
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
