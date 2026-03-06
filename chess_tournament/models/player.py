class Player:
    """Represents a chess tournament player.

    This class models a player with their personal information
    and their unique national chess identifier.

    Attributes:
        first_name (str): The player's first name.
        last_name (str): The player's last name.
        birth_date (str): The player's birth date in YYYY-MM-DD format.
        chess_id (str): Unique national chess identifier.
    """

    def __init__(self, first_name, last_name, birth_date, chess_id):
        """Initializes a new player.

        Args:
            first_name (str): The player's first name.
            last_name (str): The player's last name.
            birth_date (str): Date of birth (YYYY-MM-DD).
            chess_id (str): National chess identifier.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.chess_id = chess_id

    def to_dict(self):
        """Converts the player to a dictionary for serialization.

        Returns:
            dict: Dictionary containing all player data.
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "chess_id": self.chess_id
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Player instance from a dictionary.

        Args:
            data (dict): Dictionary containing player data.

        Returns:
            Player: New Player instance.
        """
        return cls(
            first_name=data["first_name"],
            last_name=data["last_name"],
            birth_date=data["birth_date"],
            chess_id=data["chess_id"]
        )

    def __str__(self):
        """Returns a string representation of the player.

        Returns:
            str: Format "First_Name Last_Name (ID)".
        """
        return f"{self.first_name} {self.last_name} ({self.chess_id})"
