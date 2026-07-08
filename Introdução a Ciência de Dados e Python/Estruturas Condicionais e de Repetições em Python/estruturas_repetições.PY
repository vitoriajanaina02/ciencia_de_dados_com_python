# ESTRUTURAS DE REPETIÇÕES
#
# O que são estruturas de repetição:
# São estruturas utilizadas para repetir um trecho de código um determinado número de vezes.
# Este número pode ser conhecido previamente ou determinado através de uma expressão lógica.
#
# Exemplo sem repetição
# Receba um número de teclado e exiba os 2 números seguintes
a = int((input("Informe um número inteiro: ")))
print(a)

a += 1
print(a)

a += 1
print(a)

# Exemplo com repetição
# Receba um número de teclado e exiba os 2 números seguintes
a = int((input("Informe um número inteiro: ")))
print(a)

a += 1
print(a)

# COMANDO FOR
# O comando for é usado para percorrer um objeto iterável. Faz sentido usar for quando sabemos
# o número exato de vezes que nosso bloco de código deve ser executado, ou quando queremos
# percorrer um objeto iterável.
#
# for
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print() # adiciona uma quebra de linha

# FUNÇÃO RANGE
# Range é uma função built-in do Python, ela é usada para produzir uma sequência de números
# inteiros a partir de um ínicio(inclusivo) para um fim(exclusivo). Se usarmos range(i,j)
# será produzido:
# i, i+1, i+2, i+3, ..., j+1.
# Ela recebe 3 argumentos: stop(obrigatório), start(opcional) e step opcional.
#
# range
# range(stop) -> range object
# range(start, stop[, step]) -> range object

list(range(4)) # [0, 1, 2, 3]

# Utiizando range com for
for numero in range (0, 11):
    print(numero, end="")

# exibindo a tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end="")

# COMANDO WHILE
# O comando while é usado para repetir um bloco de código várias vezes. Faz sentido usar
# while quando NÃO sabemos o número exato de vezes que nosso bloco de código deve ser executado.
#
# while
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")

# while/else
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")