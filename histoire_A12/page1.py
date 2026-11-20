def page1(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    print(f"{gameState['nom']}, Tu est au milieu de la plage entouré de débris et de cadavre. Pour commencer ta survie que préfère tu faire")
    print("1 - Fouiller les bagages  2 - Fouiller les cadavres")
    choix: str = input("> ")

    if choix == "1":
        gameState["inventaire"].append("fusée de détresse")
        gameState["inventaire"].append("boites de conserves")
        gameState["inventaire"].append("chaussures")
        print("Tu enfiles les chaussures que tu as trouvé par chance et un manteau qui te protégera. Tu recupères des boites de conserve. Enfin, tu découvres une fusée de détresse")
        res = 2
    elif choix == "2":
        gameState["inventaire"].append("couteau")
        gameState["inventaire"].append("clé secrète")
        gameState["inventaire"].append("briquet")
        print("Tu trouves une mystérieuse clé dans la poche d'un cadavre, tu la ranges précieusement. Tu trouve egalement un couteau, et un briquet dont tu ignore s'il marche encore. ")
        res = 2
    else:
        print("Choix invalide.")
        res = 1                  # on reste sur cette page

    return res
