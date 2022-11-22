#1
myTable=[1,2,3,4]
def permuter(tab,indice1,indice2):
    var_tempo=tab[indice1]
    tab[indice1]=tab[indice2]
    tab[indice2]=var_tempo
    return myTable

print(permuter(myTable,2,1))