##Partie 1 : Tri à bulles
#1
myTable=[12,58,3,5,7,4]


def permuter(tab,indice1,indice2):
    var_tempo=tab[indice1]              #on stocke la variable pour la perdre
    tab[indice1]=tab[indice2]           #puis on permute
    tab[indice2]=var_tempo              #et on recupere la variable qu'on avait stocké
    return myTable                      

"""print(permuter(myTable,2,1))"""

#2
for i in range (len(myTable)-1):        #on fait une boucle de la taille du tableau -1, pour ne pas créer d'erreurs vu qu'on utilise un +1 dans le programme.
    if myTable[i]>myTable[i+1]:         #Ici on test si l'élément de gauche est plus grand que celui a sa droite. Si c'est le cas, alors on les permute entre eux
        permuter(myTable,i,i+1)

"""print(myTable)"""

