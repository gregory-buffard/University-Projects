#!/bin/bash

UPINFO="/users/personnel/u/upinfo/configurations/"
PASSAGE=.passage
REP=$(pwd)

# Pour afficher une succession de point suivis de [OK]
# Ça ne sert pas à grand chose mais c’est plutôt classe.
function affichage_ligne() {
    l=$(echo $1 | wc -m)  # longueur de l'argument
    n=$(echo 80 - $l | bc)
    echo -n $1 ""
    for i in $(seq $n)
    do
	echo -n "."
	sleep .03
    done
    echo " [OK]"
}


# Lors du premier appel du script, lance la fonction précédente après
# avoir affiché des messages.
function premier_passage() {
    affichage_ligne "Configuration de GNU/Emacs"
    affichage_ligne "Configuration de ZSH"
    affichage_ligne "Désactivation des programmes espions de la CIA"
    affichage_ligne "Installation des programmes espions d’UniCA"
    affichage_ligne "On patiente encore un peu, je fais une pause café"
    affichage_ligne "Vérification du pass sanitaire"
    affichage_ligne "Vérification du pass vaccinale"
    $UPINFO/scripts/upinfo-configurer.sh --force
    touch $PASSAGE
}

# Si on ré-appelle le script, on demande à l’étudiant de continuer.
function second_passage() {
    affichage_ligne "configuration de GNU/Emacs"
    echo -n "configuration de ZSH"
    for i in $(seq 30)
    do
	echo -n "."
	sleep .03
    done
    sleep 1
    echo " euh "
    echo
    sleep .5
    echo "Oh et puis zut, je l'ai déjà fait !"
    sleep 1
    echo "Allez, au boulot !"
    echo
    echo >> $PASSAGE
}

# Si on ré-ré-appelle le script, on ordonne à l’étudiant de continuer.
function troisième_passage() {
    echo "On passe à la question suivante !"
}

# Pour déterminer si le script est appelé pour la première fois ou non,
# lors du premier passage on créé un fichier vide .passage
# lors du second on ajoute une ligne à ce fichier
if [ ! -f "$PASSAGE" ]
then
    premier_passage
else
    n=$(cat "$PASSAGE" | wc -l)
    if [ $n -eq 0 ]
    then
	second_passage
    else
	troisième_passage
    fi
fi
