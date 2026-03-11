import csv

#
#   LECTURE CSV, delimiteur ";"  :
#
def chargeFichierCsv(nomFichier) -> list[list[str]] :
    # Liste pour stocker les lignes
    lignes: list[list[str]] = []
    # ouverture
    fichier = open(nomFichier, "r", encoding="utf-8-sig")
    # lecture
    reader = csv.reader(fichier,delimiter=";")
    for ligne in reader:
        lignes.append(ligne)  # Ajouter chaque ligne à la liste
    fichier.close()    #fermeture.
    print(f"Chargement du fichier {nomFichier}")
    return lignes


#
#   ECRITURE CSV : delimiteur ";"  :
#
def ecritFichierCsv (nomFichier,data : list[list[str]]) -> None :
    # utf-8-sig facilite l'ouverture du fichier sur un tableur plus tard.
    fichier = open(nomFichier, "w", encoding="utf-8-sig", newline="") # Ouverture
    writer = csv.writer(fichier,delimiter=";")
    for ligne in data:
        writer.writerow(ligne)
    fichier.close()                # Fermeture
    print(f"Ecriture du fichier {nomFichier}")

if __name__ == "__main__":
    data = chargeFichierCsv("../Data_csv/Liste_1789_etudiants.csv") # a list of data[row][column][string] (list[list[str]])

    # Question 2:
    print(f"Le fichier contient {len(data) - 1} lignes, sans compter l'entete.")
    
    # Question 3:
    ecritFichierCsv("../Sortie_csv/votre_fichier.csv", data)