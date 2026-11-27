def page5(gameState: dict) -> int:
    res: int = -2
                         
    if "fusée de détresse" in gameState["inventaire"]:
        print("Le bateau est très loin, mais il pourrait bien te sauver. Veux tu utiliser la fusée de détresse pour signaler ta position?")
        choix: str = input("1 - Oui  2 - Non")
        if choix == "1":
            print("Tu as utilisé la fusée de détresse. Mais le bateau est trop loin et ne te voit pas. Tu as perdu ta fusée de détresse. Tu dois maintenant trouver un autre moyen de survie.")
            gameState["inventaire"].remove("fusée de détresse")
            res = 6
        elif choix == "2":
            print("Tu as choisi de ne pas utiliser la fusée de détresse. Tu dois continuer à survivre.")
            res = 6
        else:
            print("Choix invalide.")
            res = 5
    elif "fusée de détresse" not in gameState["inventaire"]:
        print("Malheureusement, tu n'as aucun moyen de signaler ta position, car tu n'a pas trouvé de fusée de détresse.Tu dois continuer à survivre.")
        res = 6

    return res