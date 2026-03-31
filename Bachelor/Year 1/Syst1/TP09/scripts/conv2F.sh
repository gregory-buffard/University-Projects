#!/bin/zsh

calcul_C2F() {
    local C=$1
    local F=$((C * 9 / 5 + 32))
    echo "$F"
}

read "temp_C?Donner la température en degrés Celsius à convertir : "
temp_F=$(calcul_C2F $temp_C)

echo "$temp_C °C = $temp_F °F"
