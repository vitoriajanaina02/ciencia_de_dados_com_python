# MÉTODOS DA CLASSE DICT
#
# {}.clear
contatos = {
    "vitoria@gmail.com": {"nome": "Vitoria", "telefone": "3333-2221"},
    "daniel@gmail.com": {"nome": "Daniel", "telefone": "3443-2121"},
    "juninho@gmail.com": {"nome": "Juninho", "telefone": "3344-9871"},
    "rosiane@gmail.com": {"nome": "Rosiane", "telefone": "3333-7766"},
}

contatos.clear()
contatos # {}

# {}.copy
contato = {
     "vitoria@gmail.com": {"nome": "Vitoria", "telefone": "3333-2221"},
}

copia = contato.copy()
copia["vitoria@gmail.com"] = {"nome": "Vih"}

contato["vitoria@gmail.com"] #  "vitoria@gmail.com": {"nome": "Vitoria", "telefone": "3333-2221"}
copia["vitoria@gmail.com"] # {"nome": "Vih"}

# {}.fromkeys
dict.fromkeys(["nome", "telefone"]) # {"nome": None, "telefone": None}

dict.fromkeys(["nome", "telefone"], "vazio") # {"nome": "vazio", "telefone": "vazio"}

# {}.get
contato1 = {
    "vitoria@gmail.com": {"nome": "Vitoria", "telefone": "3333-2221"},
}

contato1["chave"] # KeyError

contato1.get("chave") # None
contato1.get("chave", {}) # {}
contato1.get("vitoria@gmail.com", {}) # {"vitoria@gmail.com": {"nome": "Vitoria", "telefone": "3333-2221"}}

# {}.items
contato2 = {
    "vitoria@gmail.com": {"nome": "Vitoria", "telefone": "3333-2221"},
}

contato2.items() # dict_items([("vitoria@gmail.com", {"nome": "Vitoria", "telefone": "3333-2221"})])

# {}.pop
contato3 = {
    "vitoria@gmail.com": {"nome": "Vitoria", "telefone": "3333-2221"},
}

contato3.pop("vitoria@gmail.com") # {"nome": "Vitoria", "telefone": "3333-2221"}
contato3.pop("vitoria@gmail.com", {}) # {}

# {}.popitem
contato4 = {
    "vitoria@gmail.com": {"nome": "Vitoria", "telefone": "3333-2221"},
}

contato4.pop() # ("vitoria@gmail.com", {"nome": "Vitoria", "telefone": "3333-2221"})
contato4.pop() # KeyError

# {}.setdefault
contato5 = {"nome": "Vitoria", "telefone": "3333-2221"}

contato5.setdefault("nome", "Michel") # "Vitoria"
contato5 #  {"nome": "Vitoria", "telefone": "3333-2221"}

contato.setdefault("idade", 24) # 24
contato5 #  {"nome": "Vitoria", "telefone": "3333-2221", "idade": 28}

# {}.update
contato6 = {
    "vitoria@gmail.com": {"nome": "Vitoria", "telefone": "3333-2221"},
}

contato6.update({"vitoria@gmail.com": {"nome": "Vih"}})
contato6 # {"vitoria@gmail.com": {"nome": "Vih"}}

contato6.update({"daniel@gmail.com": {"nome": "Daniel", "telefone": "3443-2121"}})
contato6 # {"vitoria@gmail.com": {"nome": "Vih"}}, "daniel@gmail.com": {"nome": "Daniel", "telefone": "3443-2121"}}

# {}.values
contatos1 = {
    "vitoria@gmail.com": {"nome": "Vitoria", "telefone": "3333-2221"},
    "daniel@gmail.com": {"nome": "Daniel", "telefone": "3443-2121"},
    "juninho@gmail.com": {"nome": "Juninho", "telefone": "3344-9871"},
    "rosiane@gmail.com": {"nome": "Rosiane", "telefone": "3333-7766"},
}

contatos1.values() 
# dict_values([{"nome": "Vitoria", "telefone": "3333-2221"},
# "{"nome": "Daniel", "telefone": "3443-2121"},
# "{"nome": "Juninho", "telefone": "3344-9871"},
# "{"nome": "Rosiane", "telefone": "3333-7766"},])

# in
contatos2 = {
    "vitoria@gmail.com": {"nome": "Vitoria", "telefone": "3333-2221"},
    "daniel@gmail.com": {"nome": "Daniel", "telefone": "3443-2121"},
    "juninho@gmail.com": {"nome": "Juninho", "telefone": "3344-9871"},
    "rosiane@gmail.com": {"nome": "Rosiane", "telefone": "3333-7766"},
}

"vitoria@gmail.com" in contatos2 # True
"eden@gmail.com" in contatos2 # False
"idade" in contatos2["vitoria@gmail.com"] # False
"telefone" in contatos2["daniel@gmail.com"] # True

# del
contatos3 = {
    "vitoria@gmail.com": {"nome": "Vitoria", "telefone": "3333-2221"},
    "daniel@gmail.com": {"nome": "Daniel", "telefone": "3443-2121"},
    "juninho@gmail.com": {"nome": "Juninho", "telefone": "3344-9871"},
    "rosiane@gmail.com": {"nome": "Rosiane", "telefone": "3333-7766"},
}

del contatos3["vitoria@gmail.com"]["telefone"]
del contatos3["juninho@gmail.com"]

contatos3 # {"vitoria@gmail.com": {"nome": "Vitoria"}, "daniel@gmail.com":
# {"nome": "Daniel", "telefone": "3443-2121"}, "rosiane@gmail.com": {"nome": "Rosiane", "telefone": "3333-7766"}}