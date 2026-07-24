# FUNÇÕES PYTHON - PARTE 2
#
# Parâmetros Especiais
# Por padrão, argumentos podem ser passados para uma função Python tanto
# por posição quanto explicitamente pelo nome. Para uma melhor legibilidade
# e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser
# passados, assim um desenvolvedor precisa apenas olhar para a definição da
# função para determinar se os itens são passados
# por posição, por posição e nome, ou por nome.
#
# Positional only
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido

# Keyword only
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido

# Keyword and positional only
# * colocado em outro lugar, faz com que o parâmetro se torne opcional seja por posição ou nome
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido

# Objetos de Primeira Classe
# Em Python tudo é objeto, dessa forma FUNÇÕES TAMBÉM SÃO OBJETOS o que as tornam objetos
# de primeira classe. Com isso podemos ATRIBUIR FUNÇÕES A VARIÁVEIS, PASSÁ-LAS COMO
# PARÂMETROS PARA FUNÇÕES, USÁ-LAS COMO VALORES EM ESTRUTURAS DE DADOS (listas, tuplas,
# dicionários, etc) e usar como valor de retorno para uma função (closures).
#
# Exemplo
def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar) # O resultado da operação 10 + 10 = 20

# Escopo local e escopo global
# Python trabalha com escopo local, e global, dentro do bloco da função o escopo é local.
# Portanto alterações ali feitas em objetos imútaveis serão perdidas quando o método terminar
# de ser executado. Para usar objetos globais utilizamos a palavra-chave GLOBAL, que informa
# ao interpretador que a variável que está sendo manipulada no escopo local é global. Essa
# NÃO É UMA BOA  PRÁTICA E DEVE SER EVITADA.
#
# Exemplo
salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

salario_bonus(500) # 2500