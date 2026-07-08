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