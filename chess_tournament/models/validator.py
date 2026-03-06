import re
from datetime import date, datetime


class Validator:
    """Utility class for data validation."""

    @staticmethod
    def is_valid_player_name(name):
        """Validates a player's first or last name."""
        pattern = re.compile(r"^[A-Za-zÀ-ÿ\s'\-]+$")
        return bool(name and pattern.match(name))

    @staticmethod
    def is_valid_chess_id(chess_id):
        """Validates a national chess identifier (e.g., AB12345)."""
        pattern = re.compile(r'^[A-Z]{2}\d{5}$')
        return bool(chess_id and pattern.match(chess_id))

    @staticmethod
    def is_valid_date_format(date_str):
        """Checks if a date is in DD/MM/YYYY format."""
        try:
            datetime.strptime(date_str, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    @staticmethod
    def is_valid_tournament_name(name):
        """Validates a tournament name."""
        pattern = re.compile(r"^[A-Za-zÀ-ÿ0-9\s'\-\.]+$")
        return bool(name and pattern.match(name))

    @staticmethod
    def is_valid_location(location):
        """Validates a location."""
        return bool(location and location.strip())

    @staticmethod
    def is_valid_start_date(start_date_str):
        """Checks if the start date is today or in the future."""
        if not Validator.is_valid_date_format(start_date_str):
            return False
        start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
        return start_date >= date.today()

    @staticmethod
    def is_valid_end_date(start_date_str, end_date_str):
        """Checks if the end date is after or equal to the start date."""
        if not (Validator.is_valid_date_format(start_date_str) and Validator.is_valid_date_format(end_date_str)):
            return False
        start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
        end_date = datetime.strptime(end_date_str, "%d/%m/%Y").date()
        return end_date >= start_date

    @staticmethod
    def is_valid_num_rounds(num_rounds_str):
        """Checks if the number of rounds is a positive integer."""
        try:
            val = int(num_rounds_str)
            return val >= 1
        except ValueError:
            return False
