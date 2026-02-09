from typing import List
from chess_tournament.models.player import Player
from chess_tournament.models.match import Match
from chess_tournament.models.round import Round

def display_welcome():
    """Displays a welcoming message to the user."""
    welcome_text = """
    ==========================================
    |                                        |
    |      CHESS TOURNAMENT MANAGER          |     |
    |                                        |
    ==========================================
    
    Welcome, Tournament Director!
    
    Use this system to:
    * Register players and their ELO ratings.
    * Generate match pairings (Swiss system).
    * Record results and update rankings.
    * Export tournament reports.
    
    ------------------------------------------
    """
    print(welcome_text)

def main():
    display_welcome()
  
    print("Initializing system... Please select an option from the menu.")

   # Requirement: Using List to store our Player objects
    players: List[Player] = []

    # Creating instances using your __init__ structure
    player1 = Player("Magnum", "Carl", "1990-11-30", "NO42001")
    player2 = Player("Ali", "Firouz", "2003-06-18", "FR65001")

    # Adding to our list
    players.append(player1)
    players.append(player2)
    print(f"Successfully registered {len(players)} players: ")
    for p in players:
        # This uses the first_name and last_name from your __init__
        print(f"- {p.first_name} {p.last_name} (ID: {p.chess_id})")

    # 2. Create a Match between two players
    current_match = Match(player1=player1, score1=0.5, player2=player2, score2=0.5)

    # 3. Display the match
    print(current_match)  # This will use the __repr__ method of Match to display a nice format

    # 4. Show the tuple format 

    print(f"Serialized format: {current_match.to_tuple()}")
    def debug_round():
        p1 = Player("Magnus", "Carlsen", "1990-11-30", "NOR001")
        p2 = Player("Alireza", "Firouzja", "2003-06-18", "FRA001")
        
        match1 = Match(p1, 1.0, p2, 0.0)
        
        # Create the round
        round1 = Round("Round 1", start_time="2026-02-07 14:00")
        round1.add_match(match1)
        
        print(f"--- {round1.name} ---")
        print(f"Matches: {round1.matches}") # Will use the __repr__ of Match for display
        print(f"Serialized JSON: {round1.to_dict()}")
    debug_round()
if __name__ == "__main__":
    main()