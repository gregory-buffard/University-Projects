#!/bin/zsh
M=$1
N=$2
resultat=1

for (( i=0; i<N; i++ ))
do
    resultat=$((resultat * M))
done

echo $resultat
