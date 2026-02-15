import os
from chess_tournament.controllers.database import Database

def debug_database():
    print("--- DEBUG DATABASE START ---")
    # if os.path.exists("data"):
    # 1. Test de création des dossiers
    Database.ensure_data_dirs()
    if os.path.exists("data/tournaments"):
        print("[OK] Dossiers de données créés.")

    # 2. Test des Joueurs (Save & Load)
    mock_players = [
        {"first_name": "Magnus", "last_name": "Carlsen", "chess_id": "NO12345"},
        {"first_name": "Alireza", "last_name": "Firouzja", "chess_id": "FR67890"}
    ]
    
    print("Sauvegarde des joueurs...")
    Database.save_players(mock_players)
    
    print("Chargement des joueurs...")
    loaded_players = Database.load_players()
    print(f"Joueurs récupérés : {len(loaded_players)}")
    if loaded_players == mock_players:
        print("[OK] Sauvegarde/Chargement des joueurs réussi.")

    # 3. Test des Tournois (Fichiers individuels)
    mock_tournament = {
        "name": "Grand Prix Special",
        "location": "Paris",
        "players": [],
        "rounds": []
    }
    
    print(f"Sauvegarde du tournoi : {mock_tournament['name']}...")
    Database.save_tournament(mock_tournament)
    
    print("Chargement de tous les tournois...")
    all_tournaments = Database.load_tournaments()
    print(f"Nombre de tournois trouvés : {len(all_tournaments)}")
    
    found = any(t['name'] == "Grand Prix Special" for t in all_tournaments)
    if found:
        print("[OK] Le tournoi a bien été créé et relu.")

    print("\n--- DEBUG DATABASE FINISHED ---")
    print("Vérifie ton dossier 'data/' pour voir les fichiers JSON générés.")

if __name__ == "__main__":
    debug_database()