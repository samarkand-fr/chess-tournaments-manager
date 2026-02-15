from ..models.player import Player
from .database import Database


class PlayerController:
    # Contrôleur pour la gestion des joueurs.

    def __init__(self, view):
        # Initialise le contrôleur de joueurs.

        self.view = view
        self.players = []
        self.load_players()

    def load_players(self):
        # Charge tous les joueurs depuis la base de données.
        data = Database.load_players()
        # On vide la liste actuelle
        self.players = []
        # Pour chaque dictionnaire de joueur...
        for p in data:
            # ...on crée un objet Player
            player_obj = Player.from_dict(p)
            self.players.append(player_obj)

    def save_players(self):
        # Sauvegarde tous les joueurs dans la base de données.
        data = []
        # Convertir chaque joueur en dictionnaire
        for p in self.players:
            data.append(p.to_dict())
        Database.save_players(data)

    def create_player(self):
        # rée un nouveau joueur via l'interaction utilisateur.

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
        # Affiche la liste de tous les joueurs.
        self.view.display_players(self.players)
        self.view.get_user_input("Press Enter to continue...")

    def get_player_by_index(self, index):
        # Récupère un joueur par son index dans la liste.

        if 0 <= index < len(self.players):
            return self.players[index]
        return None
