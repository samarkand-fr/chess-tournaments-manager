"""Module définissant la classe Round pour les tours de tournoi."""
from typing import List
from .match import Match


class Round:
    """Représente un tour dans un tournoi d'échecs.

    Un tour contient plusieurs matchs joués simultanément et enregistre
    les heures de début et de fin.

    Attributes:
        name (str): Nom du tour (ex: "Round 1").
        start_time (str): Heure de début au format "YYYY-MM-DD HH:MM:SS".
        end_time (str): Heure de fin au format "YYYY-MM-DD HH:MM:SS".
        matches (List[Match]): Liste des matchs du tour.
    """

    def __init__(self, name, start_time="", end_time="",
                 matches: List[Match] = None):
        """Initialise un nouveau tour.

        Args:
            name (str): Nom du tour.
            start_time (str, optional): Heure de début. Par défaut "".
            end_time (str, optional): Heure de fin. Par défaut "".
            matches (List[Match], optional): Liste de matchs. Par défaut None.
        """
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.matches = matches if matches else []

    def add_match(self, match: Match):
        """Ajoute un match au tour.

        Args:
            match (Match): Match à ajouter.
        """
        self.matches.append(match)

    def to_dict(self):
        """Convertit le tour en dictionnaire pour la sérialisation.

        Les matchs sont sérialisés sous forme de tuples.

        Returns:
            dict: Dictionnaire contenant toutes les données du tour.
        """
        serialized_matches = []
        for match in self.matches:
            p1, s1 = match.player1, match.score1
            p2, s2 = match.player2, match.score2

            # Si p1/p2 sont des objets Player, convertir en dict
            p1_data = p1.to_dict() if hasattr(p1, 'to_dict') else p1
            p2_data = p2.to_dict() if hasattr(p2, 'to_dict') else p2

            serialized_matches.append(([p1_data, s1], [p2_data, s2]))

        return {
            "name": self.name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "matches": serialized_matches
        }

    @staticmethod
    def from_dict(data):
        """Crée une instance de Round à partir d'un dictionnaire.

        Args:
            data (dict): Dictionnaire contenant les données du tour.

        Returns:
            Round: Nouvelle instance de Round.
        """
        matches_data = data.get("matches", [])
        matches = []
        for m_tuple in matches_data:
            matches.append(Match.from_tuple(m_tuple))

        # On utilise explicitement 'Round'
        return Round(
            name=data["name"],
            start_time=data["start_time"],
            end_time=data["end_time"],
            matches=matches
        )
