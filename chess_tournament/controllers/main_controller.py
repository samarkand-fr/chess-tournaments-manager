"""Main application controller module."""
from ..views.main_view import MainView
from .player_controller import PlayerController
from .tournament_controller import TournamentController
from .report_controller import ReportController
from .database import Database


class MainController:
    """Main application controller.

    Orchestrates the different controllers and manages the main menu.

    Attributes:
        view (MainView): Main view instance.
        player_controller (PlayerController): Player controller.
        tournament_controller (TournamentController): Tournament controller.
        report_controller (ReportController): Report controller.
        db (Database): Database instance.
    """

    def __init__(self):
        """Initializes the main controller and all sub-controllers."""
        self.view = MainView()
        self.db = Database()
        self.player_controller = PlayerController(self.db)
        self.tournament_controller = TournamentController(
            self.player_controller, self.db
        )
        self.report_controller = ReportController(self.db)

    def run(self):
        """Starts the main application loop.

        Displays the main menu and processes user choices
        until they choose to exit.
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
        """Manages the player menu.

        Displays the player management menu and processes choices
        until the user returns to the main menu.
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
        """Manages the tournament menu.

        Displays the tournament management menu and processes choices
        until the user returns to the main menu.
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
        """Launches the report generation module."""
        self.report_controller.run_reports()
