#!/usr/bin/env python3

import sys

TOTAL = 0
contador_notas = 0

#Realizando o controle de inserção do usuário
n = int(input("Informe a quantidade de nota: "))
cont = 1
notas = []

for i in range(n):
        notas += input("Informe cada nota x%d: " % (i+1))

vetor_original = notas

print(f"Vetor Original {vetor_original}")

#Realizando a contagem das notas

while contador_notas <= n:
        contador_notas = contador_notas + 1
        print(contador_notas)
        TOTAL = TOTAL + notas #Somando as notas ao total
        print(TOTAL)

#Média da disciplina

média = TOTAL/10
print('a média da disciplina é:', média)

