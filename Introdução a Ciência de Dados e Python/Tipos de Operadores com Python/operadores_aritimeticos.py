# OPERADORES ARITMÉTICOS
# Conhecendo os operadores aritméticos

# O que são:
# Os operadores aritméticos executam operações matemáticas, como adição, subtração com operandos.

# EXEMPLOS:

# Adição
print(1 + 1) # 2

# Subtração
print(10 - 2) # 8

# Multiplicação
print(4 * 3) # 12

# Divisão
print(12 / 3) # 4.0

# Divisão inteira
print(12 // 2) # 6

# Módulo - resto da divisão
print(10 % 3) # 1

# Exponenciação 
print(2 ** 3) # 8

# Precedência de operadores 

# Na matemática:
# Na matemática existe uma regra que indica quais operações devem ser executadas primeiro. Isso é útil
# pois ao analisar uma expressão, a depender da ordem das operações o valor pode ser diferente:
x = 10 - 5 * 2
# x é igual a 10 ou 0?

# A definição indica a seguinte ordem como a correta:
# Parentêses
# Expoêntes
# Multiplicações e divisões (da esquerda para a direita)
# Somas e subtrações (da esquerda para a direita)

# EXEMPLOS
print(10 - 5 * 2) # 0

print((10 - 5) * 2) # 10

print(10 ** 2 * 2) # 200

print(10 ** (2 * 2)) # 10000

print(10 / 2 * 4) # 20.0

# Pratica
produto_1 = 10
produto_2 = 20

print(produto_1 + produto_2)
print(produto_1 * produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 * produto_2)
print(produto_1 % produto_2)
print(produto_1 ** produto_2)