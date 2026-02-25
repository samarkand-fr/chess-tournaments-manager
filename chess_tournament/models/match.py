class Match:
    """Représente un match entre deux joueurs dans un tournoi.

    Un match oppose deux joueurs et enregistre leurs scores respectifs.
    Les scores peuvent être 1.0 (victoire), 0.5 (match nul), ou 0.0 (défaite).

    Attributes:
        player1: Premier joueur (objet Player ou dictionnaire).
        score1 (float): Score du premier joueur.
        player2: Deuxième joueur (objet Player ou dictionnaire).
        score2 (float): Score du deuxième joueur.
    """

    def __init__(self, player1, score1, player2, score2):
        """Initialise un nouveau match.

        Args:
            player1: Premier joueur (Player ou dict).
            score1 (float): Score du premier joueur.
            player2: Deuxième joueur (Player ou dict).
            score2 (float): Score du deuxième joueur.
        """
        self.player1 = player1
        self.score1 = score1
        self.player2 = player2
        self.score2 = score2

    def to_tuple(self):
        """Convertit le match en tuple pour la sérialisation.

        Returns:
            tuple: Tuple de deux listes [joueur, score].
        """
        return ([self.player1, self.score1], [self.player2, self.score2])

    @classmethod
    def from_tuple(cls, match_tuple):
        """Crée une instance de Match à partir d'un tuple.

        Args:
            match_tuple (tuple): Tuple contenant les données du match.

        Returns:
            Match: Nouvelle instance de Match.
        """
        p1_data, p2_data = match_tuple
        player1, score1 = p1_data
        player2, score2 = p2_data
        return cls(player1, score1, player2, score2)

    def __str__(self):
        """Retourne une représentation textuelle du match.

        Returns:
            str: Format "Joueur1 (score1) vs Joueur2 (score2)".
        """
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
