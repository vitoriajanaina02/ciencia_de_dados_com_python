# LISTAS: CRIAÇÃO DE ACESSO AOS DADOS
#
# Listas em Python podem armazenar de maneira sequencial qualquer tipo de objeto.
# Podemos criar listas utilizando o construtor list, a função range ou colocando
# valores separador por vírgula dentro de colchetes. Listas são objetos mutáveis,
# portanto podemos alterar seus valores após a criação.
#
# Exemplo 1
frutas = ["laranja", "maca", "uva"]

frutas = []

letras = list("python")

numeros = list(range(10))

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]

# Exemplo 2
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

matriz[0] # [1, "a", 2]
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # "c"

# Exemplo 3
lista = ["p", "y", "t", "h", "o", "n"]

lista[2:] # ["t", "h", "o", "n"]
lista[:2] # ["p", "y"]
lista[1:3] # ["y", "t"]
lista[0:3:2] # ["p", "y"]
lista[::] # ["p", "y", "t", "h", "o", "n"]
lista[::1] # ["n", "o", "h", "t", "y", "p"]

# Exemplo 4
carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carros}")


# Compreensão de Listas
#
# A compreensão de lista oferece uma sintaxe mais curta quando você deseja: criar
# uma nova lista com base nos valores de uma lista existente(filtro) ou gerar uma
# nova lista aplicando alguma modificação nos elementos de uma lista existente.
#
# Filtro Versão 1
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# Filtro Versão 2
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

# Modificando Valores Versão 1
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

# Modificando Valores Versão 1
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numeros ** 2 for numero in numeros]