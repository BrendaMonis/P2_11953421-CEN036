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

  # b. Identificação ORF("Open Reading Frame")

## Utilizando o modulo sys para ler o arquivo e identificar ORF
arquivo_fasta = sys.argv[2]

arquivo_fasta_ex = open(arquivo_fasta, "r") ## leitura do arquivo inserido 
print(arquivo_fasta_ex)

## Transformando em um dicionário
nome_seq = ''
desc_seq = ''
string_seq = ''
dict_seq = {}

for line in arquivo_fasta_ex:                   ## Fazer um loop no arquivo com o objetivo de deixar apenas a sequência de nucleotídeos
        line = line.rstrip()                    ## O lado direito com espaço em branco passa a ser um novo caracter

        if line.startswith('>'):
                line = line.lstrip('>')                 ## Remove o caracter de >
                info_seq = line.split(maxsplit=1)       ## Divide apenas no primeiro espaço

                if len(info_seq) > 1:
                        desc_seq = info_seq[1]

                else:
                        desc_seq = ''

                if len(string_seq) > 0:
                        dict_seq[nome_seq] = string_seq
                        string_seq = ''

                nome_seq = info_seq[0]

                if len(info_seq) > 1:
                        desc_seq = info_seq[1]
                else:
                        desc_seq = ''
        else:
                string_seq += line


if len(string_seq) > 0:
        dict_seq[nome_seq] = string_seq  ## Transforma o arquivo fasta em um dicionário

print(dict_seq) #Visualizando o dicionário
## Para verificar o funcionamento do script pode utilizar o arquivo: arquivo.fasta.2.txt

# Após retirar os espaços, sinal de maior e transformar o arquivo em um dicionário, é preciso delimitar o início e fim de cada sequência.

##Primeiramente, precisa trocar a letra T pela U caso seja necessário

dict_seq[nome_seq] = string_seq
dna = {}
rna = {}

for gene in dict_seq:
        dna = dict_seq[gene]
        rna = dna.replace('T','U')
        print(rna)

##Em seguida delimitar o início e o fim
import re

new_seq1 = re.search(r"AUG(.{3})*U[AG][AG]",rna[rna[0]])
new_seq2 = re.search(r"AUG(.{3})*U[AG][AG]",rna[rna[1]])
new_seq3 = re.search(r"AUG(.{3})*U[AG][AG]",rna[rna[2]])
new_seq4 = re.search(r"AUG(.{3})*U[AG][AG]",rna[rna[3]])
new_seq5 = re.search(r"AUG(.{3})*U[AG][AG]",rna[rna[4]])
new_seq6 = re.search(r"AUG(.{3})*U[AG][AG]",rna[rna[5]])
#OBS: Foi pensado em um códio capaz de localizar o início e o fim das 6 fases de leitura possíveis, conforme pedido no enunciado

# Após obter as novas sequências com início em AUG e fim em UAA, UAG ou UGA, será medido o seu comprimento
comp_seq1 = len(new_seq1)
comp_seq2 = len(new_seq2)
comp_seq3 = len(new_seq3)
comp_seq4 = len(new_seq4)
comp_seq5 = len(new_seq5)
comp_seq6 = len(new_seq6)

Print('Os comprimentos das sequências 1,2,3,4,5 e 6 são:', comp_seq1, ',',com_seq2, ',',com_seq3, ',',
com_seq4, ',', com_seq5, 'e', com_seq6, ',respectivamente.')

# Em seguida, deve-se verificar se são múltiplos de 3

mult3_1 = float((comp_seq1)/3)
print(mult3_1)

mult3_2 = float((comp_seq2)/3)
print(mult3_2)

mult3_3 = float((comp_seq3)/3)
print(mult3_3)

mult3_4 = float((comp_seq4)/3)
print(mult3_4)

mult3_5 = float((comp_seq5)/3)
print(mult3_5)

mult3_6 = float((comp_seq6)/3)
print(mult3_6)

