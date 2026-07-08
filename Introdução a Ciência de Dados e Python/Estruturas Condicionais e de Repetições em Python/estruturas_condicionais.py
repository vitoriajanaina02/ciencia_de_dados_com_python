# ESTRUTURAS CONDICIONAIS
#
# O que são:
# A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.
#
# IF
# Para criar uma estrtura condicional simples, composta por um único desvio, podemos utilizar a palavra
# reservada if. O comando irá testar a expressão lógica, e em caso de retorno verdadeiro as ações presentes
# no bloco de código do if serão executadas.
#
# EXEMPLO
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

if saldo <= saque:
    print("Saldo insuficiente!")


# IF/ELSE
# Para criar uma estrutura condicional com dois desvios, podemos utilizar as palavras reservadas if e else. 
# Como sabemos se a expressão lógica testada no if for verdadeira, então o bloco de código do if será executado.
# Caso contrário o bloco de código do else será executado.
#
# EXEMPLO
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

else:
    print("Saldo insuficiente!")

# IF/ELIF/ELSE
# Em alguns cenários queremos mais de dois desvios, para isso podemos utilizar a palavra reservada elif. O elif
# é composto por uma nova expressão lógica, que será testada e caso retorne verdadeiro o bloco de código do elif
# será executado. Não existe um número máximo de elifs que podemos utilizar, porém evite criar grandes estruturas
# condicionais, pois elas aumentam a complexidade do código.
#
# EXEMPLO
import sys

opcao = int(input("Infome uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))

elif opcao == 2:
    print("Exibindo o extrato...")
else:
    sys.exit("Opção inválida")

# Exemplo if
MAIOR_IDADE = 18
IDADE_ESPECIAL = 17
idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade <= MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")

# Exemplo else
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

else:
    print("Ainda não pode tirar a CNH.")

# Exemplo elif
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

elif idade == IDADE_ESPECIAL:
    print("Pode fazer as aulas teóricas, mas não pode fazer as aulas práticas.")

else:
    print("Ainda não pode tirar a CNH.")

# IF ANINHADO
# Podemos criar estruturas condicionais aninhadas, para isso basta adicionar estruturas if/elif/else
# dentro do bloco de código de estruturas if/elif/else.
#
# EXEMPLO
saldo_conta_normal = 1300
saldo_conta_universitaria = 700
saque = float(input("Digite o valor do saque: "))
cheque_especial = 1300

tipo_conta = input("Tipo de conta (normal/universitaria): ")
conta_normal = tipo_conta == "normal"
conta_universitaria = tipo_conta == "universitaria"

if conta_normal:
    saldo = saldo_conta_normal
elif conta_universitaria:
    saldo = saldo_conta_universitaria

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")

elif conta_universitaria:
    if saldo_conta_universitaria >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")


# IF TERNÁRIO
# O if ternário permite escrever uma condição em uma única linha. Ele é composto por três partes,
# a primeira parte é o retorno caso a expressão retorne verdadeiro, a segunda parte é a expressão
# lógica e a terceira parte é o retorno caso a expressão não seja atendida.
#
# EXEMPLO
status = "Sucesso" if saldo >= saldo else "Falha"

print(f"{status} ao realizar o saque!")