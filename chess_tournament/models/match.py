class Match:
    # Représente un match entre deux joueurs dans un tournoi.

    def __init__(self, player1, score1, player2, score2):
        # Initialise un nouveau match.

        self.player1 = player1
        self.score1 = score1
        self.player2 = player2
        self.score2 = score2

    def to_tuple(self):
        #Convertit le match en tuple pour la sérialisation.

        return ([self.player1, self.score1], [self.player2, self.score2])

    @staticmethod
    def from_tuple(match_tuple):
        # Crée une instance de Match à partir d'un tuple.

        p1_data, p2_data = match_tuple
        player1, score1 = p1_data
        player2, score2 = p2_data
       
        return Match(player1, score1, player2, score2)

    def __repr__(self):
        # Retourne une représentation textuelle du match.for debugging purposes.

        p1 = self.player1
        p2 = self.player2

        p1_name = (
            f"{p1['first_name']} {p1['last_name']} ({p1['chess_id']})"
            if isinstance(p1, dict) else str(p1)
        )
        
        p2_name = (
            f"{p2['first_name']} {p2['last_name']} ({p2['chess_id']})"
            if isinstance(p2, dict) else str(p2)
        )

        return f"{p1_name} ({self.score1}) vs {p2_name} ({self.score2})"
