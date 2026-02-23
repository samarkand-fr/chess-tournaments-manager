"""Module du contrôleur de gestion des joueurs."""
from ..models.player import Player
from .database import Database


class PlayerController:
    """Contrôleur pour la gestion des joueurs.

    Gère la création, le chargement et l'affichage des joueurs.

    Attributes:
        view: Instance de la vue pour l'affichage.
        players (list): Liste des joueurs chargés.
    """

    def __init__(self, view):
        """Initialise le contrôleur de joueurs.

        Args:
            view: Instance de la vue pour l'interaction utilisateur.
        """
        self.view = view
        self.players = []
        self.load_players()

    def load_players(self):
        """Charge tous les joueurs depuis la base de données."""
        data = Database.load_players()
        # On vide la liste actuelle
        self.players = []
        # Pour chaque dictionnaire de joueur...
        for p in data:
            # ...on crée un objet Player
            player_obj = Player.from_dict(p)
            self.players.append(player_obj)

    def save_players(self):
        """Sauvegarde tous les joueurs dans la base de données."""
        data = []
        # Convertir chaque joueur en dictionnaire
        for p in self.players:
            data.append(p.to_dict())
        Database.save_players(data)

    def create_player(self):
        """Crée un nouveau joueur via l'interaction utilisateur.

        Demande les informations du joueur à l'utilisateur, crée l'instance,
        l'ajoute à la liste et sauvegarde.
        """
        player_info = self.view.get_player_info()

        # Check if chess_id already exists
        if any(p.chess_id == player_info['chess_id'] for p in self.players):
            self.view.display_error(
                f"Chess ID {player_info['chess_id']} already exists! "
                "Each player must have a unique chess ID."
            )
            return

        player = Player.from_dict(player_info)
        self.players.append(player)
        self.save_players()
        self.view.display_message(
            f"Player {player.first_name} {player.last_name} "
            f"({player.chess_id}) created successfully!"
        )

    def list_players(self):
        """Affiche la liste de tous les joueurs."""
        self.view.display_players(self.players)
        self.view.get_user_input("Press Enter to continue...")

    def get_player_by_index(self, index):
        """Récupère un joueur par son index dans la liste.

        Args:
            index (int): Index du joueur (0-based).

        Returns:
            Player: Le joueur à l'index spécifié, ou None si invalide.
        """
        if 0 <= index < len(self.players):
            return self.players[index]
        return None
