# On indique la somme deposé en euro 
somme_depose_bit = 71.7
somme_depose_xpr = 80.1
somme_depose_eth = 58.5156
somme_depose_doge = 150

#valeur des crypto au moment des achat 
valeur_bit = 19690.6
valeur_xpr = 0.2777
valeur_eth = 915.24
valeur_doge = 0.076

#nb de crypto acheté
valeur_eur_bit = round(somme_depose_bit/valeur_bit, 2)
valeur_eur_xpr = round(somme_depose_xpr/valeur_xpr, 2)
valeur_eur_eth = round(somme_depose_eth/valeur_eth, 2)
valeur_eur_doge = round(somme_depose_doge/valeur_doge, 2)
print("vous avez actuellement:")
print("BTC: "+str(valeur_eur_bit))
print("XRP: "+str(valeur_eur_xpr))
print("ETH: "+str(valeur_eur_eth))
print("DOGE: "+str(valeur_eur_doge))


valeur_bit_actuelle = float(input("Notez la valeur actuelle du BTC  "))
valeur_xpr_actuelle = float(input("Notez la valeur actuelle du XRP  "))
valeur_eth_actuelle = float(input("Notez la valeur actuelle du ETH  "))
valeur_doge_actuelle = float(input("Notez la valeur actuelle du DOGE    "))

calcul_pourcentage_bit = round(((valeur_bit_actuelle/valeur_bit) - 1) * 100, 2)
calcul_pourcentage_xpr = round(((valeur_xpr_actuelle/valeur_xpr) - 1) * 100, 2)
calcul_pourcentage_eth = round(((valeur_eth_actuelle/valeur_eth) - 1) * 100, 2)
calcul_pourcentage_doge = round(((valeur_doge_actuelle/valeur_doge) - 1) * 100, 2)



benef_bit = (valeur_eur_bit*valeur_bit_actuelle) - somme_depose_bit
benef_xpr = (valeur_eur_xpr*valeur_xpr_actuelle) - somme_depose_xpr
benef_eth = (valeur_eur_eth*valeur_eth_actuelle) - somme_depose_eth
benef_doge = (valeur_eur_doge*valeur_doge_actuelle) - somme_depose_doge

benefname=["BTC", "XRP" , "ETH", "DOGE"]
benef=[benef_bit, benef_xpr, benef_eth, benef_doge]

benef_total = round((benef_doge+benef_eth+benef_xpr+benef_bit), 2)


for x in range(0, len(benef)-1):
    
    if x > 0 :
        print("La valeur du "+ benefname[x] + " à évolué de " + str(benef[x]) + " %")
    elif x == 0:
        print("La valeur du "+benefname[x] + " est resté la meme")
    else:
        print("La valeur du "+benefname[x] +" à baissé de " + str(benef[x]) + " %")



if benef_total > 0 :
    print("Votre benefice est " + str(benef_total)+ " euros")
elif benef_total == 0:
    print("Votre benefice est nulle ")
else :
    print("Votre perte est " + str(benef_total)+ " euros")
