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

#---------------------------------------------------------------------------------------------------------------------------------------------------------#
#Partie 2 : Tic tac toe

#1
tableau_jeu=[   [None,None,None],
                [None,None,None],
                [None,None,None]    ]

#2
def placement_signe(tableau_jeu):
    signe=str(input("Vous jouez les X ou les O ?"))                 #on regarde quel signe joue le joueur

    print("Où voulez vous jouer ?")                                 #on veut savoir où il va jouer et on stock ses réponses
    print('    A      B    C')  
    print('1',tableau_jeu[0])
    print('2',tableau_jeu[1])
    print('3',tableau_jeu[2])
    emplt_colonne=str(input("Quelle colonne ? A, B ou C ?"))
    emplt_ligne=int(input("Quelle ligne ? 1, 2 ou 3 ?"))

    #on remplace les lettre par des chiffres, plus faciles a manipuler
    if emplt_colonne == 'A':
        emplt_colonne = 0
    if emplt_colonne == 'B':
        emplt_colonne = 1
    if emplt_colonne == 'C':
        emplt_colonne = 2
    tableau_jeu[emplt_ligne-1][emplt_colonne] = signe           #Ici on met le signe a l'emplacement choisi par le joueur
    return tableau_jeu



#3
def verification(tableau_jeu,signe_tester):         #désolé, c'est très long
    #lignes
    if tableau_jeu[0][0]==signe_tester and tableau_jeu[0][1]==signe_tester and tableau_jeu[0][2]==signe_tester:
        return True
    if tableau_jeu[1][0]==signe_tester and tableau_jeu[1][1]==signe_tester and tableau_jeu[1][2]==signe_tester:
        return True
    if tableau_jeu[2][0]==signe_tester and tableau_jeu[2][1]==signe_tester and tableau_jeu[2][2]==signe_tester:
        return True
    
    #colonnes
    if tableau_jeu[0][0]==signe_tester and tableau_jeu[1][0]==signe_tester and tableau_jeu[2][0]==signe_tester:
        return True
    if tableau_jeu[0][1]==signe_tester and tableau_jeu[1][1]==signe_tester and tableau_jeu[2][1]==signe_tester:
        return True
    if tableau_jeu[0][2]==signe_tester and tableau_jeu[1][2]==signe_tester and tableau_jeu[2][2]==signe_tester:
        return True
    
    #diagonales
    if tableau_jeu[0][0]==signe_tester and tableau_jeu[1][1]==signe_tester and tableau_jeu[2][2]==signe_tester:
        return True
    if tableau_jeu[2][0]==signe_tester and tableau_jeu[1][1]==signe_tester and tableau_jeu[0][2]==signe_tester:
        return True
    return False



#4
def tableau_rempli(tableau_jeu):            #renvoie True si le tableau est pleins
    for i in range(0,3):
        for j in range(0,3):
            if tableau_jeu[i][j] == None:
                return False
    return True



def Tic_tac_toe():
    while tableau_rempli(tableau_jeu) == False :        #condition d'arret pour le jeu, si tous les emplacements sont remplies
        placement_signe(tableau_jeu)

        if verification(tableau_jeu,'X') == True:
            print("Le joueur aux X a gagné :")
            break
        if verification(tableau_jeu,'O') == True:
            print("Le joueur aux O a gagné !")
            break

    if tableau_rempli(tableau_jeu) == True :
        print("Personne n'a gagné ; Egalité ! ")

print(Tic_tac_toe())

#6
""" Pour le Puissance 4, il faudra déjà, agrandir le tableau de jeu, rajouter des tests de vérifications si 4 couleurs sont
    alignées. Et surtout, il faudra surtout rendre le programme optimisé (pas comme le miens).
    Le Puissance 4 et le Tic tac toe se ressemblent beaucoup, la seule différence étant le nombre de symboles ou couleurs à
    alligner et la taille du plateau de jeu.
"""