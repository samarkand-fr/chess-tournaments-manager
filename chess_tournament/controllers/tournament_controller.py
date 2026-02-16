from datetime import datetime
import random
from ..models.tournament import Tournament
from ..models.round import Round
from ..models.match import Match
from .database import Database


class TournamentController:
    # Contrôleur pour la gestion des tournois.

    def __init__(self, view, player_controller):
        # Initialise le contrôleur de tournois.

        self.view = view
        self.player_controller = player_controller
        self.tournaments = []
        self.load_tournaments()

    def load_tournaments(self):
        # Charge tous les tournois depuis la base de données.
        data = Database.load_tournaments()
        # On vide la liste actuelle
        self.tournaments = []
        # Pour chaque dictionnaire de tournoi dans les données...
        for t in data:
            # ...on crée un objet Tournament
            tournament_obj = Tournament.from_dict(t)
            # ...et on l'ajoute à la liste
            self.tournaments.append(tournament_obj)

    def save_tournament(self, tournament: Tournament):
        # Sauvegarde un tournoi dans la base de données.

        Database.save_tournament(tournament.to_dict())

    def create_tournament(self):
        """Crée un nouveau tournoi via l'interaction utilisateur."""
        info = self.view.get_tournament_info()
        tournament = Tournament.from_dict(info)
        self.tournaments.append(tournament)
        self.save_tournament(tournament)
        self.view.display_message("Tournament created successfully!")

    def manage_tournament(self):
        # Permet de sélectionner et gérer un tournoi.
        self.view.display_tournaments(self.tournaments)
        choice = self.view.get_user_input("Select tournament ID to manage: ")
        try:
            index = int(choice) - 1
            if 0 <= index < len(self.tournaments):
                self.process_tournament(self.tournaments[index])
            else:
                self.view.display_error("Invalid selection")
        except ValueError:
            self.view.display_error("Invalid input")

    def get_tournament_status(self, tournament: Tournament):
        # Détermine l'état actuel du tournoi.

        # Tournament finished
        if tournament.current_round > tournament.num_rounds:
            return f"Finished ({tournament.num_rounds}/{tournament.num_rounds} rounds)"

        # No rounds yet
        if not tournament.rounds:
            player_count = len(tournament.players)
            if player_count < 8:
                return f"Waiting for players ({player_count}/8 minimum)"
            return f"Ready to start ({player_count} players)"

        # Check last round (Vérifier le dernier round)
        last_round = tournament.rounds[-1]
        
        # Compter les matchs non terminés (score 0 vs 0)
        unscored = 0
        for m in last_round.matches:
            if m.score1 == 0 and m.score2 == 0:
                unscored += 1

        round_num = tournament.current_round - 1
        if unscored > 0:
            return f"Round {round_num}/{tournament.num_rounds} - {unscored} match(es) pending"
        else:
            if tournament.current_round <= tournament.num_rounds:
                return f"Round {round_num}/{tournament.num_rounds} complete"
            return f"Finished ({tournament.num_rounds}/{tournament.num_rounds} rounds)"

    def process_tournament(self, tournament: Tournament):
        # Traite les actions sur un tournoi sélectionné.

        while True:
            status = self.get_tournament_status(tournament)
            choice = self.view.display_tournament_management_menu(
                tournament.name, status
            )
            if choice == "1":
                self.add_player_to_tournament(tournament)
            elif choice == "2":
                self.start_next_round(tournament)
            elif choice == "3":
                self.enter_scores(tournament)
            elif choice == "4":
                self.show_rankings(tournament)
            elif choice == "5":
                self.show_round_scores(tournament)
            elif choice.upper() == "Q":
                break
            else:
                self.view.display_error("Invalid choice")

    def add_player_to_tournament(self, tournament):
        # Ajoute un joueur au tournoi.

        # Validation: Cannot add players after rounds have started
        if tournament.rounds:
            self.view.display_error(
                "Cannot add players: Tournament has already started. "
                "Players can only be added before Round 1."
            )
            return

        self.player_controller.list_players()
        choice = self.view.get_user_input("Select player ID to add: ")
        try:
            index = int(choice) - 1
            player = self.player_controller.get_player_by_index(index)
            if player:
                # Check if player already in tournament by ID
                if not any(p.chess_id == player.chess_id for p in tournament.players):
                    tournament.add_player(player)
                    self.save_tournament(tournament)
                    self.view.display_message(f"Added {player}")
                else:
                    self.view.display_error("Player already in tournament.")
            else:
                self.view.display_error("Player not found")
        except ValueError:
            self.view.display_error("Invalid input")

    def start_next_round(self, tournament: Tournament):
        # Démarre le tour suivant du tournoi.

        # Validation 1: Check if tournament is finished
        if tournament.current_round > tournament.num_rounds:
            self.view.display_message("Tournament is already finished!")
            return

        # Validation 2: Check minimum number of players
        if len(tournament.players) < 8:
            self.view.display_error(
                "Cannot start round: Need at least 8 players in tournament. "
                "Add players first (option 1)."
            )
            return

        # Validation 3: Check if previous round is finished
        if tournament.rounds:
            last_round = tournament.rounds[-1]
            # Chercher les matchs non terminés
            unscored_matches = []
            for m in last_round.matches:
                if m.score1 == 0 and m.score2 == 0:
                    unscored_matches.append(m)
            
            if len(unscored_matches) > 0:
                self.view.display_error(
                    f"Cannot start next round: {len(unscored_matches)} match(es) "
                    f"in {last_round.name} not scored yet. "
                    "Score them first (option 3)."
                )
                return

        # Check for odd number of players
        players = tournament.players[:]
        if len(players) % 2 != 0:
            self.view.display_error(
                f"Cannot start round: Tournament has {len(players)} players "
                "(odd number). Add or remove 1 player to make it even."
            )
            return

        # Generate pairs
        if tournament.current_round == 1:
            random.shuffle(players)
            pairs = []
            for i in range(0, len(players), 2):
                pairs.append((players[i], players[i+1]))
        else:
            # Calculer les scores actuels
            scores = self.calculate_scores(tournament)
            
            # Trier les joueurs : d'abord par score (descendant), puis par ID
            # On utilise une fonction de tri personnalisée (lambda)
            # x[0] est le score, x[1] est l'ID
            players = sorted(
                tournament.players,
                key=lambda p: (scores.get(p.chess_id, 0), p.chess_id),
                reverse=True
            )

            pairs = self.generate_pairs(players, tournament)

        # Create matches (Créer les objets Match)
        matches = []
        for p1, p2 in pairs:
            # Score 0 pour commencer pour les deux joueurs
            new_match = Match(p1, 0, p2, 0)
            matches.append(new_match)

        # Create round
        new_round = Round(
            name=f"Round {tournament.current_round}",
            start_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            end_time="",
            matches=matches
        )
        tournament.add_round(new_round)
        tournament.current_round += 1
        self.save_tournament(tournament)
        self.view.display_message(
            f"{new_round.name} started with {len(matches)} matches.")

    def generate_pairs(self, sorted_players, tournament):
        # Génère les paires de joueurs pour un tour.

        pairs = []
        remaining_players = sorted_players[:]

        while remaining_players:
            p1 = remaining_players.pop(0)
            opponent = None

            # Look for the first compatible opponent
            for i, p2 in enumerate(remaining_players):
                if not self.has_played_together(p1, p2, tournament):
                    opponent = remaining_players.pop(i)
                    break

            # If no compatible opponent found (all played against), take the next best
            if not opponent:
                if remaining_players:
                    opponent = remaining_players.pop(0)

            if opponent:
                pairs.append((p1, opponent))
            else:
                # Should not happen if check strictly even number of players
                pass

        return pairs

    def has_played_together(self, p1, p2, tournament):
        # Vérifie si deux joueurs se sont déjà affrontés.

        # Obtenir les IDs des joueurs à vérifier
        p1_id = p1.chess_id if hasattr(p1, 'chess_id') else p1.get('chess_id')
        p2_id = p2.chess_id if hasattr(p2, 'chess_id') else p2.get('chess_id')

        # Parcourir tous les rounds passés
        for round_obj in tournament.rounds:
            # Parcourir tous les matchs du round
            for match in round_obj.matches:
                m1 = match.player1
                m2 = match.player2
                
                # Obtenir les IDs des joueurs du match
                m1_id = m1.chess_id if hasattr(m1, 'chess_id') else m1.get('chess_id')
                m2_id = m2.chess_id if hasattr(m2, 'chess_id') else m2.get('chess_id')

                # Vérifier si c'est le même match (A vs B ou B vs A)
                if m1_id == p1_id and m2_id == p2_id:
                    return True
                if m1_id == p2_id and m2_id == p1_id:
                    return True
        
        return False

    def show_round_scores(self, tournament: Tournament):
        # Affiche les scores d'un tour sélectionné.

        if not tournament.rounds:
            self.view.display_message("No rounds started.")
            return

        # If only one round, show it directly
        if len(tournament.rounds) == 1:
            self.view.display_matches_for_scoring(tournament.rounds[0].matches)
            self.view.pause()
            return

        # Multiple rounds - let user choose
        print("\n--- SELECT ROUND ---")
        for i, round_obj in enumerate(tournament.rounds, 1):
            unscored = sum(1 for m in round_obj.matches
                           if m.score1 == 0 and m.score2 == 0)
            status = "Complete" if unscored == 0 else f"{unscored} pending"
            print(f"{i}. {round_obj.name} - {status}")

        choice = self.view.get_user_input(
            "Select round number (or 'Q' to cancel): "
        )

        if choice.upper() == 'Q':
            return

        try:
            round_index = int(choice) - 1
            if 0 <= round_index < len(tournament.rounds):
                selected_round = tournament.rounds[round_index]
                self.view.display_matches_for_scoring(selected_round.matches)
                self.view.pause()
            else:
                self.view.display_error("Invalid round number")
        except ValueError:
            self.view.display_error("Invalid input")

    def enter_scores(self, tournament: Tournament):
        # Permet de saisir les scores des matchs du tour en cours.

        if not tournament.rounds:
            self.view.display_error(
                "No rounds started yet. Start Round 1 first (option 2)."
            )
            return

        last_round = tournament.rounds[-1]

        while True:
            self.view.display_matches_for_scoring(last_round.matches)
            choice = self.view.get_user_input(
                "\nSelect match number to score (or 'Q' to finish/back): "
            )

            if choice.upper() == 'Q':
                break

            try:
                index = int(choice) - 1
                if 0 <= index < len(last_round.matches):
                    self._score_match(last_round.matches[index])
                    self.save_tournament(tournament)
                else:
                    self.view.display_error("Invalid match number.")
            except ValueError:
                self.view.display_error("Invalid input.")

        # Check if all matches scored to mark end time
        if all(m.score1 + m.score2 > 0 for m in last_round.matches):
            if not last_round.end_time:
                last_round.end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_tournament(tournament)
                self.view.display_message("All matches scored. Round finished.")

    def _score_match(self, match):
        p1 = match.player1
        p2 = match.player2
        # Safely get last names whether player is object or dict
        p1_name = p1.last_name if hasattr(p1, 'last_name') else p1.get('last_name', 'Unknown')
        p2_name = p2.last_name if hasattr(p2, 'last_name') else p2.get('last_name', 'Unknown')

        print(f"\nScoring: {p1_name} vs {p2_name}")
        result = self.view.get_user_input(
            f"Result ([1] {p1_name} wins, "
            f"[2] {p2_name} wins, [0] Draw): "
        )
        if result == "1":
            match.score1 = 1.0
            match.score2 = 0.0
        elif result == "2":
            match.score1 = 0.0
            match.score2 = 1.0
        elif result == "0":
            match.score1 = 0.5
            match.score2 = 0.5
        else:
            self.view.display_error("Invalid result. Scores unchanged.")

    def calculate_scores(self, tournament):
        # Calcule les scores totaux de tous les joueurs.

        scores = {}
        # Initialiser le score de tout le monde à 0
        for p in tournament.players:
            scores[p.chess_id] = 0.0
            
        # Parcourir tous les matchs pour additionner les points
        for round_obj in tournament.rounds:
            for match in round_obj.matches:
                p1 = match.player1
                p2 = match.player2

                # Handle cases where player might be dict or object
                p1_id = p1.chess_id if hasattr(p1, 'chess_id') else p1.get('chess_id')
                p2_id = p2.chess_id if hasattr(p2, 'chess_id') else p2.get('chess_id')

                # Ajouter les scores si les joueurs sont dans le dictionnaire
                if p1_id in scores:
                    scores[p1_id] = scores[p1_id] + match.score1
                if p2_id in scores:
                    scores[p2_id] = scores[p2_id] + match.score2
        return scores

    def show_rankings(self, tournament):
        # Affiche le classement actuel du tournoi.

        scores = self.calculate_scores(tournament)
        sorted_players = sorted(tournament.players,
                                key=lambda p: (scores.get(p.chess_id, 0), p.chess_id),reverse=True)
        print(f"\n--- RANKINGS: {tournament.name} ---")
        for i, p in enumerate(sorted_players, 1):
            print(f"{i}. {p} - Score: {scores.get(p.chess_id, 0)}")
        self.view.get_user_input("Press Enter to continue...")
