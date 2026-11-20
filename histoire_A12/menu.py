def menu() -> dict:
    """Création du personnage : retourne le dictionnaire gameState."""
    print("=== CRÉATION DU PERSONNAGE ===")
    nom: str = input("Quel est votre nom ? ")
    gameState: dict = {
        "nom": nom,
        "faim": 70,
        "vie": 60,
        "inventaire": [],
    }
    print(f"Bienvenue, {nom} ! Tu viens de t'échouer sur cette île déserte. Tu es faible et tu n'as pas mangé depuis longtemps Faim : {gameState['faim']}, Vie : {gameState['vie']}\n")
    return gameState
