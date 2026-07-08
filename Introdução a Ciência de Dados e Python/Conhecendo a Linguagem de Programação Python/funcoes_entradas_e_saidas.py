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