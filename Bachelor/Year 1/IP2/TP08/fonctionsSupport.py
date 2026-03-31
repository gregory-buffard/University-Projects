import csv
import matplotlib.pyplot as plt
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

def traceCourbe(X, Y, Yb, titre, fichier=None):
    
    fig, ax = plt.subplots()  # création explicite
    
    styleDuGraphe = 'b-'
    if Y != []:
        ax.plot(X, Y, styleDuGraphe, linewidth=1, label="y = f(x)")
        ax.legend()
    
    #ax.plot(X, Yb, styleDuGraphe)
    
    styleDuGraphe = 'r-'
    if Yb != []:
        ax.plot(X, Yb, styleDuGraphe, linewidth=1, label="y = f(x)")
        ax.legend()
    
    ax.set_xlabel('x - axe des abscisses')
    ax.set_ylabel('y - axe des ordonnées')
    ax.set_title(titre)
    ax.grid()
    
    ax.set_xlim(0, 10)
    ax.set_ylim(-5, 15)
    
    if fichier is not None:
        plt.savefig(fichier)
        fig.savefig(
            fichier,
            dpi=300,
            bbox_inches="tight",
            pad_inches=0)

    plt.show()
    return fig, ax 