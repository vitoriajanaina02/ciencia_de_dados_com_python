# TIPOS DE DADOS

# ETAPA 1: O que são tipos?
# ETAPA 2: Tipos numéricos
# ETAPA 3: Booleanos e Strings

# Por que usamos tipos?
# Os tipos servem para definir as caracteristicas e comportamentos de um valor (objeto) para o interpretador.
# Por exemplo:
# Com esse tipo eu sou capaz de realizar operações matematicas.
# Esse tipo para ser armazenado em memória irá consumir 24 bytes.

# Os tipos built-in são:
# Texto         -> str
# Númerico      -> int, float, complex
# Sequência     -> list, tuple, range
# Mapa          -> dict
# Coleção       -> set, fronzenset
# Booleano      -> bool
# Binário       -> bytes, bytearray, memoryview

print(1 + 10)
print(11 + 10)
print(1.5 + 1 + 0.5)
print(True)
print(False)
print("Python")


# MODO INTERATIVO
# ETAPA 1: Usando o modo interativo
# ETAPA 2: Funções dir e help

# O modo interativo:
# O interpretador Python pode executar em modo que possibilite o desenvolvedor 
# a escrever código, e ver o resultado na hora.

# Iniciando o modo interativo:
# Existem duas formas de iniciar o modo interativo, chamando apenas o interpretador (python)
# ou executando o script com a  flag-i (python -i app.py).

# DIR
# Sem argumentos, retorna a lista de nomes no escopo local atual. Com um argumento,
# retorna uma lista de atributos válidos para o objeto. Exemplo:
# dir()
# dir(100)

# HELP
# Invoca o sistema de ajuda itegrado. É possível fazer buscas em modo interativo ou informar por
# parâmetro qual o nome do módulo, função, classe, método ou váriavel. Exemplo:
# help()
# help(100)


# VARIÁVEIS E CONSTANTES
# ETAPA 1: O que são variáveis e constantes
# ETAPA 2: Boas práticas

# Variáveis:
# Em linguagens de programação podemos definir valores que podem sofrer alterações no decorrer da execução do programa.
# Esses valores recebem o nome de variáveis, pois eles nascem com um valor e não necessariamente devem permanecer
# com o mesmo durante a execução do programa.

# EXEMPLO 1
age = 24
name = "Vitória"
print(f"Meu nome é {name} e eu tenho {age} ano(s) de idade.")

# EXEMPLO 2
age, name = (24, "Vitória")
print(f"Meu nome é {name} e eu tenho {age} ano(s) de idade.")

# Alterando os valores:
# Perceba que não precisamos definir o tipo de dados da variável, o Python faz isso automaticamente para nós. Por isso
# não podemos simplesmente criar uma variável sem atribuir um valor. Para alterar o valor da variável basta fazer uma
# atrubuição de um novo valor: 

# Constantes;
# Assim como as variáveis, constantes são utilizadas para armazenar valores. Uma constante nasce com um valor e
# permanece com ele até o final da execução do programa, ou seja, o valor é imutável.

# Python não tem constante:
# Não existe uma palavra reservada para informar ao interpretador que o valor é constante. Em algumas linguagens
# por exemplo: Java e C utilizamos final e const, respectivamente para declarar uma constante.
# Em Python usamos a convenção que diz ao programador que a variável é uma constante. Para fazer isso, você deve
# criar a variável com o nome todo em letras maíusculas: 

# EXEMPLOS
ABS_PATH = "/home/guilherme/Documents/python_course/"
DEBUG = True
STATES = [
    "SP",
    "RJ",
    "MG",
]
AMOUNT = 30.2

# Boas Práticas:
# O padrão de nomes deve ser snake case. (não pode ter espaços, usar anderlaine "_")
# Escolher nomes sugestivos.
# Nome de constantes todo em maiúsculo.

nome = "Vitória"
idade = 24

nome, idade = ("Michel", 23) # O () é opcional

print(nome, idade)

limite_saque_diario = 1000

BRAZILIAN_STATES = ["SP", "RJ", "SC", "RS"]

print(BRAZILIAN_STATES)



# CONVERSÃO DE TIPOS
# Objetivo Geral: Aprender a converter os tipos das variáveis.

# Convertendo tipos: 
# Em alguns momentos é necessário converter o tipo de uma variável para manipular de forma diferente. Por exemplo:
# Variáveis do tipo string, que armazenam números e precisamos fazer alguma operação matemática com esse valor.

# Inteiro para  float
preco = 10
print(preco)

preco = float(preco)
print(preco)

preco = 10 / 2 
print(preco)

# Float para inteiro
preco = 10.30
print(preco)

preco = int(preco)
print(preco)

# Conversão por divisão
preco = 10
print(preco)

print(preco / 2) # número float

print(preco // 2) # número inteiro

# Númerico para string
preco = 10.50
idade = 28

print(str(preco))
print(str(idade))

texto = f"idade {idade}  preco {preco}"
print(texto)

# String para número
preco = "10.50"
idade = "28"

print(float(preco))
print(int(idade))

# Erro de conversão
preco = "python"
print(float(preco))

# EXEMPLOS
print(int(1.97348728))
print(int("10"))
print(float("10.10"))
print(float(100))

valor = 10
valor_str = str(valor)
print(type(valor))          # <class 'int'> a variável é um número inteiro
print(type(valor_str))      # <cass 'str'> a variável é um texto (string)

print(100 / 2)
print(100 // 2)

# OBS: type() é uma função built-in do Python que retorna o tipo de dado de uma variável.
# O type() é muito útil para debugar e entender o que está acontecendo com seus dados.



# FUNÇÕES DE ENTRADAS E SAÍDAS
# Objetivo Geral: Aprender  como receber e exibir informações para  usuário.

# ETAPA 1: Lendo valores com a função input
# ETAPA 2: Exibindo valores com a função print

# Função input:
# A função builtin input é utilizada quando queremos ler dados da entrada padrão (teclado). Ela recebe um
# argumento do tipo string, que é exibido para o usuário na saída padrão (tela). A função lê a entrada,
# converte para string e retorna o valor.

# EXEMPLO
nome = input("Informe o seu nome: ")

# Função print:
# A função builtin print é utilizada quando queremos exibir dados na saída padrão (tela). Ela recebe um
# argumento obrigatório do tipo varargs de objetos e 4 argumentos opcionais (sep, end, file e flush). 
# Todos os objetos são convertidos para string, separados por sep e terminados  por end. A string é
# exibida para o usuário.

# EXEMPLO 
nome = "Vitoria"
sobrenome = "Nicolau"

print(nome, sobrenome) # Vitoria Nicolau
print(nome, sobrenome, end="...\n") # Vitoria Nicolau...
print(nome, sobrenome, sep="#") # Vitoria#Nicolau   