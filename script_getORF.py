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
    line = line.rstrip()                        ## O lado direito com espaço em branco passa a ser um novo caracter

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

print(dict_seq)
## Para verificar o funcionamento do script pode utilizar o arquivo: arquivo.fasta.2.txt

# Após retirar os espaços, sinal de maior e transformar o arquivo em um dicionário, é preciso delimitar o início e fim de cada sequência.

##Primeiro precisa trocar a letra T pela U caso seja necessário
dict_rna = dict_seq.replace('T','U')
