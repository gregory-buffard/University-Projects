#!/bin/bash



function demander () {
    message=$1
    echo "Souhaitez-vous configurer $message. Attention, cela écrasera l’ancien fichier"
    read -p "oui/[non]> " reponse
    if [ "A$reponse" = "Aoui" ]
    then
        return 0 # True
    else
        return 1 # False
    fi
}



function sauvegarder_fichier() {
    SAUVEGARDE="$HOME/.sauvegarde_upinfo/"
    temps=$(date +"%F-%H-%M-%S")
    fichier_origine=$1
    fichier_destination=$(basename $1 | sed "s/^\./POINT/" | sed "s/$/-$temps/")
    if [ -e $fichier_origine ]
    then
        mkdir -p $SAUVEGARDE
        echo -e "\nOn fait une sauvegarde de $fichier_origine dans le dossier $SAUVEGARDE"
        cp $fichier_origine $SAUVEGARDE/$fichier_destination
    fi

}




function usage() {
    echo "$0 [--maj-emacs]\n\n"
    echo -e "Sans paramètre demande pour faire la configuration de Zsh, Bash et Emacs\n"
    echo -e "avec l’option --maj-emacs met à jour les bibliothèques GNU/Emacs (sans toucher au .emacs)\n"
    exit 1
}


MAJ_EMACS="Faux"
if [ $# -gt 1 ]
then
    usage
elif [ $# -eq 1 ]
then
   [ $1 = "--maj-emacs" ] &&  MAJ_EMACS="Vrai" || usage
fi



function telecharger_remplacer () {
    SOURCE=$1
    DESTINATION=$(echo $1 | sed 's/^POINT\(.*\)...$/.\1/')
    sauvegarder_fichier ~/$DESTINATION

    echo -e "On télécharge le fichier"
    wget --no-check-certificate -q https://upinfo.univ-cotedazur.fr/~obaldellon/conf/$SOURCE -O $REP/$DESTINATION

    echo -e "On l’installe\n"
    mv $REP/$DESTINATION ~/$DESTINATION
}


function mettre_a_jour_bibliotheque_emacs() {
    wget --no-check-certificate -q https://upinfo.univ-cotedazur.fr/~obaldellon/conf/upinfo.zip -O $REP/upinfo.zip
    unzip -q $REP/upinfo.zip -d $REP
    mkdir -p ~/.emacs.d/
    rm -rf ~/.emacs.d/upinfo
    mv -f $REP/upinfo -t ~/.emacs.d/
}

REP=$(mktemp -d)

if [ $MAJ_EMACS = "Vrai" ]
then
    mettre_a_jour_bibliotheque_emacs
    rm -rf $REP
    exit 0
fi

demander "Zsh"  && telecharger_remplacer POINTzshrc.sh || echo -e "On ne touche pas à Zsh\n"
demander "Bash" && telecharger_remplacer POINTbashrc.sh|| echo -e "On ne touche pas à Bash\n"


if demander "GNU/Emacs"
then
    telecharger_remplacer POINTemacs.el
    mettre_a_jour_bibliotheque_emacs
else
    echo -e "On ne touche pas à Emacs\n"
fi

rm -rf $REP
