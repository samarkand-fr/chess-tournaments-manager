from chess_tournament.views.view import View
from chess_tournament.controllers.player_controller import PlayerController
from chess_tournament.controllers.tournament_controller import TournamentController

def test_tournament_logic():
    view = View()
    p_ctrl = PlayerController(view)
    t_ctrl = TournamentController(view, p_ctrl)

    print("\n--- STEP 1: Création du Tournoi ---")
    # Cette méthode va te demander le nom, lieu, etc.
    t_ctrl.create_tournament() 
    
    # On récupère l'objet tournoi qu'on vient de créer (le dernier de la liste)
    mon_tournoi = t_ctrl.tournaments[-1]

    print("\n--- STEP 2: Ajout automatique de 8 joueurs ---")
    # On vérifie d'abord si on a assez de joueurs dans la base globale
    if len(p_ctrl.players) < 8:
        print(f"[ERREUR] Tu n'as que {len(p_ctrl.players)} joueurs en base.")
        print("Crée d'abord 8 joueurs avec le PlayerController avant de lancer ce test.")
        return

    # On ajoute les 8 premiers joueurs trouvés en base au tournoi
    for i in range(8):
        player = p_ctrl.get_player_by_index(i)
        if player:
            # On vérifie si le joueur n'est pas déjà dans le tournoi
            if not any(p.chess_id == player.chess_id for p in mon_tournoi.players):
                mon_tournoi.add_player(player)
                print(f"Joueur {i+1} ajouté : {player.last_name}")

    # Sauvegarde de l'état du tournoi avec ses 8 joueurs
    t_ctrl.save_tournament(mon_tournoi)
    print(f"[OK] Tournoi '{mon_tournoi.name}' prêt avec {len(mon_tournoi.players)} joueurs.")

    print("\n--- STEP 3: Lancement Round 1 ---")
    # Maintenant la condition len(players) < 8 devrait passer !
    t_ctrl.start_next_round(mon_tournoi)

    print("\n--- STEP 4: Vérification de l'affichage du Round ---")
    # On affiche les matchs créés pour vérifier que les paires sont là
    if mon_tournoi.rounds:
        t_ctrl.show_round_scores(mon_tournoi)
    else:
        print("[ERREUR] Le Round 1 n'a pas été créé.")

if __name__ == "__main__":
    test_tournament_logic()