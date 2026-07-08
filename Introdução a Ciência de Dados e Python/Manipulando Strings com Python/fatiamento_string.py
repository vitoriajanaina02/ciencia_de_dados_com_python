# FATIAMENTO DE STRING
#
# Fatiamento de string é uma técnica utilizada para retornar substrings (partes da string original),
# informando inicio (start), fim (stop) e passo (step):[start:stop[, step]].
#
# Fatiamento
nome = "Vitoria Janaina da Silva Nicolau"

print(nome[0])       # V

print(nome[:7])      # Vitoria

print(nome[16:])     # da Silva Nicolau

print(nome[8:15])    # Janaina

print(nome[8:15:2])  # Jnia

print(nome[:]) # Vitoria Janaina da Silva Nicolau

print(nome[::-1]) # ualociN avliS ad anianaJ airotiV