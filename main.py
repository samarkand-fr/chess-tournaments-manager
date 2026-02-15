from chess_tournament.views.view import View
from chess_tournament.controllers.player_controller import PlayerController

def debug_create_player():
    # 1. On initialise la vue
    view = View()
    
    # 2. On initialise le contrôleur (il chargera les joueurs existants auto)
    player_ctrl = PlayerController(view)
    
    print("--- DEBUG : CRÉATION DE JOUEUR ---")
    
    # 3. On lance la méthode de création
    # Cette méthode va :
    # - Appeler view.get_player_info()
    # - Créer l'objet Player
    # - Sauvegarder dans data/players.json
    player_ctrl.create_player()
    
    # 4. On vérifie en affichant la liste
    print("\n--- VÉRIFICATION DE LA LISTE ---")
    player_ctrl.list_players()

if __name__ == "__main__":
    try:
        debug_create_player()
    except KeyboardInterrupt:
        print("\nTest interrompu.")