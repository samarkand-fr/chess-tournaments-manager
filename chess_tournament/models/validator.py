import re
from datetime import date, datetime


class Validator:
    """Classe utilitaire pour la validation des données."""

    @staticmethod
    def is_valid_player_name(name):
        """Valide un prénom ou un nom de joueur."""
        pattern = re.compile(r"^[A-Za-zÀ-ÿ\s'\-]+$")
        return bool(name and pattern.match(name))

    @staticmethod
    def is_valid_chess_id(chess_id):
        """Valide un identifiant national d'échecs (ex: AB12345)."""
        pattern = re.compile(r'^[A-Z]{2}\d{5}$')
        return bool(chess_id and pattern.match(chess_id))

    @staticmethod
    def is_valid_date_format(date_str):
        """Vérifie si une date est au format JJ/MM/AAAA."""
        try:
            datetime.strptime(date_str, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    @staticmethod
    def is_valid_tournament_name(name):
        """Valide le nom d'un tournoi."""
        pattern = re.compile(r"^[A-Za-zÀ-ÿ0-9\s'\-\.]+$")
        return bool(name and pattern.match(name))

    @staticmethod
    def is_valid_location(location):
        """Valide un lieu."""
        return bool(location and location.strip())

    @staticmethod
    def is_valid_start_date(start_date_str):
        """Vérifie si la date de début est aujourd'hui ou dans le futur."""
        if not Validator.is_valid_date_format(start_date_str):
            return False
        start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
        return start_date >= date.today()

    @staticmethod
    def is_valid_end_date(start_date_str, end_date_str):
        """Vérifie si la date de fin est après ou égale à la date de début."""
        if not (Validator.is_valid_date_format(start_date_str) and Validator.is_valid_date_format(end_date_str)):
            return False
        start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
        end_date = datetime.strptime(end_date_str, "%d/%m/%Y").date()
        return end_date >= start_date

    @staticmethod
    def is_valid_num_rounds(num_rounds_str):
        """Vérifie si le nombre de tours est un entier positif."""
        try:
            val = int(num_rounds_str)
            return val >= 1
        except ValueError:
            return False
