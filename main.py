from typing import List
from chess_tournament.models.player import Player
from chess_tournament.models.match import Match
from chess_tournament.models.round import Round
from chess_tournament.models.tournament import Tournament

def display_welcome():
    """Affiche le message de bienvenue."""
    welcome_text = """
    ==========================================
    |                                        |
    |      CHESS TOURNAMENT MANAGER          |
    |                                        |
    ==========================================
    
    Welcome, Tournament Director!
    
    ------------------------------------------
    """
    print(welcome_text)

def debug_round():
    print("\n--- DEBUG ROUND ---")
    p1 = Player("Magnus", "Carlsen", "1990-11-30", "NOR001")
    p2 = Player("Alireza", "Firouzja", "2003-06-18", "FRA001")
    
    match1 = Match(p1, 1.0, p2, 0.0)
    
    round1 = Round("Round 1", start_time="2026-02-07 14:00")
    round1.add_match(match1)
    
    print(f"Round: {round1.name}")
    print(f"Matches: {round1.matches}")
    print(f"Serialized: {round1.to_dict()}")

def debug_tournament():
    print("\n--- DEBUG TOURNAMENT ---")
    p1 = Player("Magnus", "Carlsen", "1990-11-30", "NOR001")
    p2 = Player("Alireza", "Firouzja", "2003-06-18", "FRA001")

    match1 = Match(p1, 1.0, p2, 0.0)
    round1 = Round("Round 1", start_time="2026-02-07 14:00")
    round1.add_match(match1)

    my_tournament = Tournament(
        name="Grand Chess Tour", 
        location="Paris", 
        start_date="2026-02-07",
        end_date="2026-02-09",
        description="Championnat annuel"
    )
    
    my_tournament.add_player(p1)
    my_tournament.add_player(p2)
    my_tournament.add_round(round1)

    print(f"Tournament: {my_tournament.name} à {my_tournament.location}")
    print(f"Serialized JSON: {my_tournament.to_dict()}")

def main():
    display_welcome()
    print("Initializing system...")

    # Utilisation du type List pour les joueurs
    players: List[Player] = []

    player1 = Player("Magnum", "Carl", "1990-11-30", "NO42001")
    player2 = Player("Ali", "Firouz", "2003-06-18", "FR65001")

    players.append(player1)
    players.append(player2)

    print(f"Successfully registered {len(players)} players.")
    
    # Création d'un match pour test
    current_match = Match(player1=player1, score1=0.5, player2=player2, score2=0.5)
    print(f"Match status: {current_match}")
    print(f"Serialized match: {current_match.to_tuple()}")

if __name__ == "__main__":
    # On lance les debugs puis le main
    debug_round()
    debug_tournament()
    main()