"""Module defining the Round class for tournament rounds."""
from typing import List
from .match import Match


class Round:
    """Represents a round in a chess tournament.

    A round contains several matches played simultaneously and records
    the start and end times.

    Attributes:
        name (str): Name of the round (e.g., "Round 1").
        start_time (str): Start time in "DD/MM/YYYY HH:MM" format.
        end_time (str): End time in "DD/MM/YYYY HH:MM" format.
        matches (List[Match]): List of matches in the round.
    """

    def __init__(self, name, start_time="", end_time="",
                 matches: List[Match] = None):
        """Initializes a new round.

        Args:
            name (str): Name of the round.
            start_time (str, optional): Start time. Defaults to "".
            end_time (str, optional): End time. Defaults to "".
            matches (List[Match], optional): List of matches. Defaults to None.
        """
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.matches = matches if matches else []

    def add_match(self, match: Match):
        """Adds a match to the round.

        Args:
            match (Match): Match to add.
        """
        self.matches.append(match)

    def to_dict(self):
        """Converts the round to a dictionary for serialization.

        Matches are serialized as tuples.

        Returns:
            dict: Dictionary containing all round data.
        """
        serialized_matches = []
        for match in self.matches:
            p1, s1 = match.player1, match.score1
            p2, s2 = match.player2, match.score2

            # If p1/p2 are Player objects, convert to dict
            p1_data = p1.to_dict() if hasattr(p1, 'to_dict') else p1
            p2_data = p2.to_dict() if hasattr(p2, 'to_dict') else p2

            serialized_matches.append(([p1_data, s1], [p2_data, s2]))

        return {
            "name": self.name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "matches": serialized_matches
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Round instance from a dictionary.

        Args:
            data (dict): Dictionary containing round data.

        Returns:
            Round: New Round instance.
        """
        matches_data = data.get("matches", [])
        matches = []
        for m_tuple in matches_data:
            matches.append(Match.from_tuple(m_tuple))

        return cls(
            name=data["name"],
            start_time=data["start_time"],
            end_time=data["end_time"],
            matches=matches
        )
