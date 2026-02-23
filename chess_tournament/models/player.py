class Player:
    """Représente un joueur de tournoi d'échecs.

    Cette classe modélise un joueur avec ses informations personnelles
    et son identifiant national d'échecs unique.

    Attributes:
        first_name (str): Prénom du joueur.
        last_name (str): Nom de famille du joueur.
        birth_date (str): Date de naissance au format YYYY-MM-DD.
        chess_id (str): Identifiant national d'échecs unique.
    """

    def __init__(self, first_name, last_name, birth_date, chess_id):
        """Initialise un nouveau joueur.

        Args:
            first_name (str): Prénom du joueur.
            last_name (str): Nom de famille du joueur.
            birth_date (str): Date de naissance (YYYY-MM-DD).
            chess_id (str): Identifiant national d'échecs.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.chess_id = chess_id

    def to_dict(self):
        """Convertit le joueur en dictionnaire pour la sérialisation.

        Returns:
            dict: Dictionnaire contenant toutes les données du joueur.
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "chess_id": self.chess_id
        }

    @staticmethod
    def from_dict(data):
        """Crée une instance de Player à partir d'un dictionnaire.

        Args:
            data (dict): Dictionnaire contenant les données du joueur.

        Returns:
            Player: Nouvelle instance de Player.
        """
        # On utilise directement le nom de la classe 'Player'
        return Player(
            first_name=data["first_name"],
            last_name=data["last_name"],
            birth_date=data["birth_date"],
            chess_id=data["chess_id"]
        )

    def __str__(self):
        """Retourne une représentation textuelle du joueur.

        Returns:
            str: Format "Prénom Nom (ID)".
        """
        return f"{self.first_name} {self.last_name} ({self.chess_id})"
