def page2(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    print("Après avoir recuperé des objets, tu te demande maintenat ce que tu va pouvoir faire des debris en bois de ton ancien bateau.")

    print("1 - Construire un abri  2 - Faire une canne à peche")
    choix: str = input("> ")
    
    if choix == "1":
        gameState["inventaire"].append("abri")
        gameState["faim"]=60
        print(f"Tu as maintenant un bel abri, mais tu as perdu de l'énergie. Faim : {gameState['faim']}")
        res = 2
    elif choix == "2":
        gameState["inventaire"].append("canne à peche")
        gameState["faim"]=100
        print(f"Tu pourra maintetant te nourrir à ta faim, quand tui prendra le temps d'aller pecher. D'ailleurs tu viens d'en attraper un. Faim : {gameState['faim']}")
        res = 2
    else:
        print("Choix invalide.")
        res = 2

    return res
