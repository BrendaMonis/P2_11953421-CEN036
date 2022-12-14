#!/usr/bin/env python3

import sys

# a. Leitura de um arquivo multifasta

## Exemplo de arquivo fasta:
SEQ_fasta_exemplo = open("arquivo.fasta.txt","r")
print(SEQ_fasta_exemplo)

for line1 in SEQ_fasta_exemplo: # lendo as linhas do arquivo
  print(line1)

## Utilizando o modulo sys para ler o arquivo multifasta através da linha de comando
arquivo_fasta = sys.argv[1]

fasta_sys = open(sys.argv[1],"r")
print(fasta_sys)

for line2 in fasta_sys: # lendo as linhas do arquivo
  print(line2)
