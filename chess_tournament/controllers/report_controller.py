"""Module du contrôleur de génération de rapports."""
from ..models.tournament import Tournament
from ..models.player import Player
from ..views.report_view import ReportView
from ..views.player_view import PlayerView
from ..views.tournament_view import TournamentView


class ReportController:
    """Contrôleur pour la génération de rapports.

    Gère l'affichage de différents rapports sur les joueurs et tournois.

    Attributes:
        view: Instance de la vue pour l'affichage.
    """

    def __init__(self, db):
        """Initialise le contrôleur de rapports."""
        self.view = ReportView()
        self.db = db

    def run_reports(self):
        """Lance le menu de génération de rapports.

        Affiche le menu des rapports et traite les choix jusqu'à
        ce que l'utilisateur retourne au menu principal.
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
        """Affiche la liste de tous les joueurs triés alphabétiquement."""
        data = self.db.load_players()
        players = [Player.from_dict(p) for p in data]
        players.sort(key=lambda p: (p.last_name, p.first_name))

        PlayerView.display_players(players)
        self.view.pause()

    def list_all_tournaments(self):
        """Affiche la liste de tous les tournois."""
        data = self.db.load_tournaments()
        tournaments = [Tournament.from_dict(t) for t in data]

        TournamentView.display_tournaments(tournaments)
        self.view.pause()

    def _select_tournament(self):
        """Permet à l'utilisateur de sélectionner un tournoi.

        Returns:
            Tournament: Le tournoi sélectionné, ou None si invalide.
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
        """Affiche les détails d'un tournoi sélectionné."""
        tournament = self._select_tournament()
        if tournament:
            self.view.display_report_header(f"DETAILS: {tournament.name}")
            TournamentView.display_tournament_details(tournament)
            self.view.pause()

    def tournament_players(self):
        """Affiche la liste des joueurs d'un tournoi sélectionné."""
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
        """Affiche les tours et matchs d'un tournoi sélectionné sous forme tabulaire."""
        tournament = self._select_tournament()
        if tournament:
            self.view.display_report_header(f"ROUNDS & MATCHES: {tournament.name}")
            # Déléguer l'affichage tabulaire à la vue
            TournamentView.display_rounds_report(tournament.rounds)
            self.view.pause()
