def validateIntSize(size, lowLim, upLim):
    while (size < lowLim or size > upLim):
        print("La taille du mot de passe doit etre comprise entre ", lowLim, " et ", upLim)
        size=input("Veuillez entrer avec la taille : ")