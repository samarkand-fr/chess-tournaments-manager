"""Report generation controller module."""
from ..models.tournament import Tournament
from ..models.player import Player
from ..views.report_view import ReportView
from ..views.player_view import PlayerView
from ..views.tournament_view import TournamentView


class ReportController:
    """Controller for report generation.

    Manages the display of various reports on players and tournaments.

    Attributes:
        view: View instance for display.
    """

    def __init__(self, db):
        """Initializes the report controller."""
        self.view = ReportView()
        self.db = db

    def run_reports(self):
        """Launches the report generation menu.

        Displays the report menu and processes choices until
        the user returns to the main menu.
        """
        while True:
            choice = self.view.display_reports_menu()
            if choice == "1":
                self.list_all_players()
            elif choice == "2":
                self.list_all_tournaments()
            elif choice == "3":
                self.tournament_details()
            elif choice == "4":
                self.tournament_players()
            elif choice == "5":
                self.tournament_rounds()
            elif choice.upper() == "Q":
                break
            else:
                self.view.display_error("Invalid choice")

    def list_all_players(self):
        """Displays the list of all players sorted alphabetically."""
        data = self.db.load_players()
        players = [Player.from_dict(p) for p in data]
        players.sort(key=lambda p: (p.last_name, p.first_name))

        PlayerView.display_players(players)
        self.view.pause()

    def list_all_tournaments(self):
        """Displays the list of all tournaments."""
        data = self.db.load_tournaments()
        tournaments = [Tournament.from_dict(t) for t in data]

        TournamentView.display_tournaments(tournaments)
        self.view.pause()

    def _select_tournament(self):
        """Allows the user to select a tournament.

        Returns:
            Tournament: The selected tournament, or None if invalid.
        """
        data = self.db.load_tournaments()
        tournaments = [Tournament.from_dict(t) for t in data]

        if not tournaments:
            self.view.display_message("No tournaments found.")
            return None

        TournamentView.display_tournaments(tournaments)
        choice = self.view.get_user_input("Select tournament ID: ")
        try:
            index = int(choice) - 1
            if 0 <= index < len(tournaments):
                return tournaments[index]
            else:
                self.view.display_error("Invalid selection")
        except ValueError:
            self.view.display_error("Invalid input")
        return None

    def tournament_details(self):
        """Displays the details of a selected tournament."""
        tournament = self._select_tournament()
        if tournament:
            self.view.display_report_header(f"DETAILS: {tournament.name}")
            TournamentView.display_tournament_details(tournament)
            self.view.pause()

    def tournament_players(self):
        """Displays the list of players for a selected tournament."""
        tournament = self._select_tournament()
        if tournament:
            self.view.display_report_header(f"PLAYERS: {tournament.name}")
            players = sorted(tournament.players, key=lambda p: (p.last_name, p.first_name))
            if not players:
                self.view.display_message("No players registered.")
            else:
                PlayerView.display_players(players)
            self.view.pause()

    def tournament_rounds(self):
        """Displays the rounds and matches of a selected tournament in a tabular format."""
        tournament = self._select_tournament()
        if tournament:
            self.view.display_report_header(f"ROUNDS & MATCHES: {tournament.name}")
            # Delegate tabular display to the view
            TournamentView.display_rounds_report(tournament.rounds)
            self.view.pause()
