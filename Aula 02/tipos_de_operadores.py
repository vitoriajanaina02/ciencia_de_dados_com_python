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


# OPERADORES DE COMPARAÇÃO

# O que são:
# São opradores utilizados para comparar dois valores.

# Igualdade
saldo = 450
saque = 200

print(saldo == saque) # false

# Diferença
saldo = 450
saque = 200

print(saldo != saque) # true

# Maior que / maior ou igual
saldo = 450
saque = 200

print(saldo > saque) # true
print(saldo >= saque) # true

# Menor que / maior ou igual
saldo = 450
saque = 200

print(saldo < saque) # false
print(saldo <= saque) # false


# OPERADORES DE ATRIBUIÇÃO

# Conhecendo os operadores de atribuição
# O que são:
# São operadores utilizados para definir o valor inicial ou sobrecresver o valor de uma variável.

# Atribuição simples
saldo = 500

print(saldo) # 500

# Atribuição com adição
saldo = 500
saldo += 200

print(saldo) # 700

# Atribuição com subtração
saldo = 500
saldo -= 100

print(saldo) # 400

# Atribuição com multiplicação
saldo = 500
saldo *= 2

print(saldo) # 1000

# Atribuição com divisão
saldo = 500
saldo /= 5

print(saldo) # 100.0

saldo = 500
saldo //= 5

print(saldo) # 100

# Atribuição com módulo
saldo = 500
saldo %= 480

print(saldo) # 20

# Atribuição com exponenciação
saldo = 80
saldo **= 2

print(saldo) # 6400


# OPERADORES LÓGICOS

# O que são:
# São operadores utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica. Quando um
# operador de comparação é utilizado, o resultado retornado é um booleano, dessa forma podemos combinar operadores de
# comparação com os operadores lógicos, exemplo: op_comparacao + op_logico + op_comparacao...N...

# EXEMPLO
saldo = 1000
saque = 200
limite = 100

saldo >= saque # true
saque <= limite # false

# Operador E
saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite # false

# Operador OU
saldo = 1000
saque = 200
limite = 100

saldo >= saque or saque <= limite # true

# Operador Negação
contatos_emergencia = []

not 1000 > 1500 # true

not contatos_emergencia # true

not "saque 1500;" # false

not "" # true

# Parênteses
saldo = 1000
saque = 250
limite = 200
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque # true

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) # true


# OPERADORES DE IDENTIDADE

# O que são:
# São operadores utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória.

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso # true

curso is not nome_curso # false

saldo is limite # true


# OPERADORES DE ASSOCIAÇÃO

# O que são:
# São operadores utilizados para verificar se um objeto está presente em uma sequência.

# EXEMPLO
curso = "Aprendizado de Máquina"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

"Aprendizado" in curso # true

"maça" not in frutas # true

200 in saques # false