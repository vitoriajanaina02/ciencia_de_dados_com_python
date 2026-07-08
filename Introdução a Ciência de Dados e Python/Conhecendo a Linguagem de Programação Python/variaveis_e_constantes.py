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