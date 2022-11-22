##Partie 1 : Tri à bulles

myTable=[12,58,3,5,7,4]

#pour tester avec 1000 :
"""import random
myTable=[]
for i in range(1000):
    myTable.append(random.randint(0,1000))
print(myTable)"""

#1/
def permuter(tab,indice1,indice2):
    var_tempo=tab[indice1]              #on stocke la variable pour la perdre
    tab[indice1]=tab[indice2]           #puis on permute
    tab[indice2]=var_tempo              #et on recupere la variable qu'on avait stocké
    return myTable                      

"""print(permuter(myTable,2,1))"""

#2/
for i in range (len(myTable)-1):        #on fait une boucle de la taille du tableau -1, pour ne pas créer d'erreurs vu qu'on utilise un +1 dans le programme.
    if myTable[i]>myTable[i+1]:         #Ici on test si l'élément de gauche est plus grand que celui a sa droite. Si c'est le cas, alors on les permute entre eux
        permuter(myTable,i,i+1)

"""print(myTable)"""

#3/
import random
def Tri_a_bulle(tab):
    for y in range(len(tab)):               #cela permet de parcourir toute la boucle plusieurs fois
        for i in range (len(myTable)-1):    #pareillement que le 2/
            if myTable[i]>myTable[i+1]:     
                permuter(myTable,i,i+1)
    return myTable

print(Tri_a_bulle(myTable))

#4/
"""Le tri a bulle est considéré comme très lent car celui ci parcours plusieurs fois le tableau entièrement.
    Le fait de permuter a chaque fois 2 éléments le rend lent, d'autant plus que le premier passage ne le tri pas entierement.
    On doit faire plusieurs passages de afin de refaire des permutations.
    Je sais qu'il existe une fonction permettant de mettre un timer afin de chronometrer un passage de notre programme mais je ne
    connais plus le nom et je ne pense pas que ce soit la reponse attendu.
    Cependant, le temps d'éxécution de ce programme est proportionelle par rapport au nombre de valeure présente dans le tableau.
    J'ai testé avec 1000 valeur, ça a mis 1 seconde voir 2. Après, plus on il y a de valeurs, plus on parcours le tableau pour permuter la boucle.
"""

#Partie 2 : Tic tac toe

#1