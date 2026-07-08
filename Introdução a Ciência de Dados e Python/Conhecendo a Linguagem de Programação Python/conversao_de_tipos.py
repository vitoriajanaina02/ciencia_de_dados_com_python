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