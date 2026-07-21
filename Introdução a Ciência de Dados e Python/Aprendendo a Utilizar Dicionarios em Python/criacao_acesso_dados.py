# CRIAÇÃO E ACESSO DE DADOS
#
# Um dicionário é um conjunto não-ordenado de pares chaves: valor, onde as chaves são únicas
# em uma dada instância do dicionário. Dicionários são delimitados por chaves: {}, e contém 
# uma lista de pares chaves: valor separado por vírgulas.
#
# Exemplo
pessoa = {"nome": "Vitoria", "idade": 24}

pessoa = dict(nome="Vitoria", idade=24)

pessoa["telefone"] = "3333-1234" # {"nome": "Vitoria", "idade": 24, "telefone": "3333-1234"}

# Acesso aos dados
# Os dados são acessados e modificados atráves da chave.
#
# Exemplo
dados = {"nome": "Vitoria", "idade": 24, "telefone": "3333-1234"}

dados["nome"] # "Vitoria"
dados["idade"] # 24
dados["telefone"] # 3333-1234

dados["nome"] = "Nivea"
dados["idade"] = 56
dados["telefone"] = 9988-1781

dados # {"nome": "Nivea", "idade": 56, "telefone": "339988-1781"}

# Dicionários Aninhados
# Dicionários podem armazenar qualquer tipo de objeto Python  como valor,  desde que a chave
# para esse valor seja um objeto imútavel como (strings e números).
#
# Exemplos
contatos = {
    "vitoria@gmail.com": {"nome": "Vitoria", "telefone": "3333-1234"},
    "nivea@gmail.com": {"nome": "Nivea", "telefone": "3443-2121"},
    "michel@gmail.com": {"nome": "Michel", "telefone": "3344-9871"},
    "felipe@gmail.com": {"nome": "Felipe", "telefone": "3333-7766"},
}

contatos["nivea@gmail.com"]["telefone"] # "3443-2121"

# Iterar Dicionários: Exemplo
for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)

# "vitoria@gmail.com": {"nome": "Vitoria", "telefone": "3333-1234"}
# "nivea@gmail.com": {"nome": "Nivea", "telefone": "3443-2121"}
# "michel@gmail.com": {"nome": "Michel", "telefone": "3344-9871"}
# "felipe@gmail.com": {"nome": "Felipe", "telefone": "3333-7766"}