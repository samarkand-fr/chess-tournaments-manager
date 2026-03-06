class Match:
    """Represents a match between two players in a tournament.

    A match faces two players and records their respective scores.
    Scores can be 1.0 (win), 0.5 (draw), or 0.0 (loss).

    Attributes:
        player1: First player (Player object or dictionary).
        score1 (float): First player's score.
        player2: Second player (Player object or dictionary).
        score2 (float): Second player's score.
    """

    def __init__(self, player1, score1, player2, score2):
        """Initializes a new match.

        Args:
            player1: First player (Player or dict).
            score1 (float): First player's score.
            player2: Second player (Player or dict).
            score2 (float): Second player's score.
        """
        self.player1 = player1
        self.score1 = score1
        self.player2 = player2
        self.score2 = score2

    def to_tuple(self):
        """Converts the match to a tuple for serialization.

        Returns:
            tuple: Tuple of two lists [player, score].
        """
        return ([self.player1, self.score1], [self.player2, self.score2])

    @classmethod
    def from_tuple(cls, match_tuple):
        """Creates a Match instance from a tuple.

        Args:
            match_tuple (tuple): Tuple containing match data.

        Returns:
            Match: New Match instance.
        """
        p1_data, p2_data = match_tuple
        player1, score1 = p1_data
        player2, score2 = p2_data
        return cls(player1, score1, player2, score2)

    def __str__(self):
        """Returns a string representation of the match.

        Returns:
            str: Format "Player1 (score1) vs Player2 (score2)".
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
