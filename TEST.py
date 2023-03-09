def main():
    # creation d'une variable usernam ayant pour valeur le mot abdel
    usernam = " abdel"
    # creation d'une variable age ayant pour valeur 19
    age =  19
    print("salam" +  str( usernam) + " tu as " + str( age) + " ans")
    # le porte monnaie d'une personne
    wallet = 125.7
    print("Mon compte bancaire est de  " + str(wallet) + " euros")
    # Je vais acheter des bonbons d'une valeur de 3e
    bonbons = 3
    print("bonbons -"  + str(bonbons ) + "euros " )
    wallet = (wallet- bonbons)
    print("Votre solde est de " + str(wallet))
    print(bonbons < 2)


    print("Mon compte bancaire est de  " + str(wallet)  + " euros")
    # Maintenant abdel jvai te montrer que je sais faire des moyennes
    valeur1 = int(input("Entrer la valeur 1"))
    valeur2 = int(input("Entrer la valeur 2"))
    valeur3 = int(input("Entrer la valeur 3"))
    valeur4 = int(input("Entrer la valeur 4"))
    resultat = (valeur1 + valeur2 + valeur3 + valeur4) / 4
    print("La moyenne est de " + str(resultat))


if __name__ == '__main__':
    main()




