#!/usr/bin/env python3

import sys

TOTAL = 0
contador_notas = 0

#Realizando o controle de inserção do usuário
n = int(input("Digite a quantidade de células da sua lista: "))
cont = 1
notas = []

for i in range(n):
        notas += input("Informe o valor de x%d: " % (i+1))

vetor_original = notas

print(f"Vetor Original {vetor_original}")
