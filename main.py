"""Main entry point for the chess tournament management application.

This module initializes and launches the application by creating an instance of the
main controller and starting the user interaction loop.
"""
from chess_tournament.controllers.main_controller import MainController


def main():
    """Launches the chess tournament management application."""
    app = MainController()
    app.run()


if __name__ == "__main__":
    main()
