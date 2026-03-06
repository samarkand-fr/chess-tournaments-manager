"""Player management controller module."""
from ..models.player import Player
from ..views.player_view import PlayerView


class PlayerController:
    """Controller for player management.

    Manages the creation, loading, and display of players.

    Attributes:
        view: View instance for display.
        players (list): List of loaded players.
    """

    def __init__(self, db):
        """Initializes the player controller."""
        self.view = PlayerView()
        self.db = db
        self.players = []
        self.load_players()

    def load_players(self):
        """Loads all players from the database."""
        data = self.db.load_players()
        # Clear current list
        self.players = []
        # For each player dictionary...
        for p in data:
            # ...create a Player object
            player_obj = Player.from_dict(p)
            self.players.append(player_obj)

    def save_players(self):
        """Saves all players to the database."""
        data = []
        # Convert each player to dictionary
        for p in self.players:
            data.append(p.to_dict())
        self.db.save_players(data)

    def create_player(self):
        """Creates a new player via user interaction.

        Prompts user for player info, creates instance,
        adds to list, and saves.
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
        """Displays the list of all players."""
        self.view.display_players(self.players)
        self.view.get_user_input("Press Enter to continue...")

    def get_player_by_index(self, index):
        """Retrieves a player by their index in the list.

        Args:
            index (int): Player index (0-based).

        Returns:
            Player: The player at the specified index, or None if invalid.
        """
        if 0 <= index < len(self.players):
            return self.players[index]
        return None
