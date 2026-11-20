def page3(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    print("Prèfères tu pecher toute l'après-midi, pour pouvoir te faire un stock de nourriture, ou te reposer afin de reprendre des forces?")

    print("1 - Pêcher  2 - Repos")
    choix: str = input("> ")
    
    if choix == "1":
        gameState["faim"] += 20
        gameState["inventaire"].append("stock_poissons")
        print(f"Tu as bien mangé. Faim : {gameState['faim']} Et tu a maintenant du stock de poissons. A peine perceptible, tu vois au loin un bateau!!!")
        res = 5
    elif choix == "2":
        gameState["faim"] -= 5
        gameState["vie"] += 20
        print(f"Tu es maintetant en pleine forme. N'oublie pas de faire des choix pour prendre le tmeps de chercher à manger. Faim : {gameState['faim']}     Vie :{gameState['vie']} ")
        res = 6
    else:
        print("Choix invalide.")
        res = 3

    return res
