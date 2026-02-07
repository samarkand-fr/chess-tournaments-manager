class Player:
    # Représente un joueur de tournoi d'échecs.

    def __init__(self, first_name, last_name, birth_date, chess_id):

        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.chess_id = chess_id

    def to_dict(self):
        #Convertit le joueur en dictionnaire pour la sérialisation.
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "chess_id": self.chess_id
        }

    @staticmethod
    def from_dict(data):
        #Crée une instance de Player à partir d'un dictionnaire.
        return Player(
            first_name=data["first_name"],
            last_name=data["last_name"],
            birth_date=data["birth_date"],
            chess_id=data["chess_id"]
        )
        
    def __str__(self):
        #Retourne une représentation textuelle du joueur.

        return f"{self.first_name} {self.last_name} ({self.chess_id})"    
