import sys
sys.path.insert(0, './Fonctions_support')

import gestionFichier


def permute(i: int, j: int, L: list[list[str]]) -> None:
    L[i], L[j] = L[j], L[i]
    
def est_avant_bool(nom1: str, nom2: str) -> bool:
    strs = [nom1, nom2]
    score = [0, 0]
    for i in range(len(strs) - 1):
        if len(strs[i]) > 1:
            for j in range(len(strs[i]) - 1):
                score[i] += ord(strs[i][j])
        else:
            score[i] += ord(strs[i])
    return strs[0] <= strs[1]

def extraitPays(data: list[list[str]]) -> set:
    pays = set()
    for i in range(1, len(data) - 1): pays.add(data[i][2])
    return pays

def definitDicoVide(ensembleCle: set) -> dict:
    output = dict()
    for i in ensembleCle: output[i] = []
    return output

def remplitDico(dico: dict, data: list[list[str]]) -> None:
    for i in range(1, len(data) - 1):
        dico[data[i][2]].append([data[i][0], data[i][1]])

def tribulle(data : list[list[str]]) -> None :    
    for k in range(len(data) - 1):
        for pos in range(len(data) - 1):           
            if est_avant_bool((data[pos+1][0] + data[pos+1][1]), (data[pos][0] + data[pos][1])):
                permute(pos+1, pos, data)


if __name__ == "__main__":
    # Question 5:
    Liste=[ ['a','b','c'] , ['d','e','f'] ]
    print(f"Avant : {Liste}")
    permute(i = 0 , j = 1 , L=Liste )
    print(f"Apres: {Liste}")
    assert Liste[1]==['a','b','c']
    
    # Question 6:
    assert est_avant_bool("A","B")
    assert est_avant_bool("Z","A") == False
    assert est_avant_bool("B","B")
    assert est_avant_bool("TOTO","TOTO")
    assert est_avant_bool("TOTO","TOTOTO")
    assert est_avant_bool("TOTOTOTOTO","TO")== False
    assert est_avant_bool("Z","AA")== False
    assert est_avant_bool("ZZ","A")== False
    
    data = gestionFichier.chargeFichierCsv("./Data_csv/Liste_1789_etudiants.csv")
    
    # Question 7:
    E = extraitPays(data)
    print(f"Le fichier contient {len(E)} pays.")
    print(E)
    assert len(E) == 7
    
    # Question 8:
    dico = definitDicoVide(E)
    assert len(dico) == 7
    assert len(dico['France']) == 0
    
    # Question 9:
    remplitDico(dico, data)
    for pays in dico.keys():
        liste = dico[pays]
        print(f"Il y a {len(liste)} etudiants invites du pays: {pays}")
        
    # Question 11:
    L4 = [["NOËL", "NEVEU"], ["MARC", "MARTIN"], ["JULIETTE", "BOYER"], ["RENÉ", "SCHNEIDER"]]
    print(f"Avant tri, liste des Francais {L4}")
    tribulle(L4)
    print(f"Apres tri, liste des Francais {L4}")