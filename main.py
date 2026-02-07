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
    # Your main menu or application logic starts here
    print("Initializing system... Please select an option from the menu.")

if __name__ == "__main__":
    main()