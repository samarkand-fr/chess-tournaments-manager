from chess_tournament.views.view import View
from types import SimpleNamespace

def run_view_debug():
    """Fonction isolée pour tester les composants visuels."""
    view = View()
    # crée  un petit mock rapide pour vérifier que tabulate fonctionne
    mock_p = SimpleNamespace(first_name="Test", last_name="User", birth_date="2000", chess_id="AA12345")
    
    view.display_message("Mode Debug : Test des Vues")
    view.display_players([mock_p])
    view.get_player_info() 

def main():
    #  on lance le debug
    run_view_debug()

if __name__ == "__main__":
    main()