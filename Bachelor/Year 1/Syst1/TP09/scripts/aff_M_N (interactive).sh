#!/bin/zsh

read "M?Entrez la valeur de M (début) : "
read "N?Entrez la valeur de N (fin) : "
read "P?Entrez la valeur de P (multiplicateur) : "

DIVISOR=$(( P * M ))

for (( i = M; i <= N; i++ )); do
    if (( DIVISOR == 0 )); then
        echo $i
    elif (( i % DIVISOR != 0 )); then
        echo $i
    fi
done
