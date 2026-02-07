from typing import List
from chess_tournament.models.player import Player
from chess_tournament.models.match import Match

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
    print(current_match)  # Uses your __str__ method

    # 4. Show the tuple format 

    print(f"Serialized format: {current_match.to_tuple()}")
  

if __name__ == "__main__":
    main()