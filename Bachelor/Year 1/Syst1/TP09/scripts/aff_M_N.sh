#!/bin/zsh
M=$1
N=$2
P=$3

DIVISOR=$(( P * M ))

for (( i = M; i <= N; i++ )); do
    if (( DIVISOR == 0 )); then
        echo $i
    elif (( i % DIVISOR != 0 )); then
        echo $i
    fi
done
