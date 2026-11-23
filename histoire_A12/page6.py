def page5(gameState: dict) -> int:
    res: int = -2

    print("Tu as beaucoup marché et tu t'es perdue. Soit tu coupes par la forêt pour rentrer au campement, soit tu rentres par la plage.")
    print("1 - Forêt  2 - Plage")
    choix: str = input("> ")
    
    if choix == "1":
        if "chaussures" in gameState["inventaire"]:
            print("Tu as choisi de couper par la forêt. Heureusement, tu as des chaussures qui t'ont protégé et tu arrives à rentrer au campement plus rapidement.")
        elif "chaussures" not in gameState["inventaire"]:
            print("Tu as choisi de couper par la forêt. Malheureusement, tu n'as pas de chaussures un serpent surgit des buissons et te mord.")
            gameState["vie"] -= 50
            print(f"Vie : {gameState['vie']}     Faim : {gameState['faim']}")
        res = 8
    elif choix == "2":
        res = 7
    else:
        print("Choix invalide.")
        res = 5

    return res