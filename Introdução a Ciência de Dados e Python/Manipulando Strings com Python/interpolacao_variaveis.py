# INTERPOLAÇÃO DE VAIÁVEIS
#
# Em Python temos 3 formas de interpolar variáveis em string, a primeira é usando
# o sinal de %, a segunda é utilizando o método format e a última é utilizando f strings.
# A primeira forma não é atualmente recomendada e seu uso em Python 3 é raro, por esse
# motivo iremos focar nas 2 últimas.
#
# Old Style
nome = "Vitoria"
idade = 24
profissao = "Programadora"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade. trabalho como %s e estou " \
"matriculada no curso de %s." % (nome, idade, profissao, linguagem))

# Método format
nome = "Vitoria"
idade = 24
profissao = "Programadora"
linguagem = "Python"

print("Olá, me chamo {}. Eu tenho {} anos de idade. trabalho como {} e estou " \
"matriculada no curso de {}.".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {}. Eu tenho {} anos de idade. trabalho como {} e estou " \
"matriculada no curso de {}.".format(linguagem, profissao, idade, nome))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade. trabalho como {profissao} e estou " \
"matriculada no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))


pessoa = { # é necessário criar um dicionário para ser possível chamar as variáveis.
    "nome": "Vitoria",
    "idade": 24,
    "profissao": "Programadora",
    "linguagem": "Python"
}

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade. trabalho como {profissao} e estou " \
"matriculada no curso de {linguagem}.".format(**pessoa))

# f string
nome = "Vitoria"
idade = 24
profissao = "Programadora"
linguagem = "Python"

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade. trabalho como {profissao} e estou " \
"matriculada no curso de {linguagem}.")

# Formatar strings com f-string

PI = 3.14159

print(f"Valor de PI: {PI:.2f}") # Valor de PI: 3.14

print(f"Valor de PI: {PI:10.2f}") # Valor de PI:          3.14