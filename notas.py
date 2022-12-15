#!/usr/bin/env python3

import sys

TOTAL = 0
contador_notas = 0

#Realizando o controle de inserção do usuário
n = int(input("Informe a quantidade de alunos na turma: "))
cont = 1
notas = []

for i in range(n):
        notas += input("Informe a nota do aluno x%d: " % (i+1))

vetor_original = notas

print(f"Vetor Original {vetor_original}")
