def page4(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    print("Tu as construi un super abri mais c'etait un peu fatiguant. Prefères tu te reposer ou as tu envie d'aller explorer l'île?")

    print("1 -Repos  2 - Exploration")
    choix: str = input("> ")
    
    if choix == "1":
        gameState["faim"] -= 5
        gameState["vie"] += 20
        print(f"Tu es maintetant en pleine forme. Faim : {gameState['faim']}     Vie :{gameState['vie']} ")
        res = 6
    elif choix == "2":
        print(f"Tu as choisi de t'aventurer sur l'ile à tes risques et périls.")
        res = 7
    else:
        print("Choix invalide.")
        res = 4
    
    return res