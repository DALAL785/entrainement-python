
# On indique la somme deposé
somme_depose = 100
valeur_bit = 19500

valeur_eur =(somme_depose/valeur_bit)
print("solde de depart " + str(valeur_eur)+ " bitcoin")

valeur_bit_actuelle = float(input("Notez la valeur actuelle du Bitcoin"))

print(valeur_bit_actuelle)

calcul_pourcentage = ((valeur_bit_actuelle/valeur_bit) - 1) * 100

if calcul_pourcentage > 0 :
    print("La valeur du BTC à évolué de " + str(calcul_pourcentage) + "%")
else:
    print("La valeur du BTC à baissé de " + str(calcul_pourcentage) + "%")


