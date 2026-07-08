# CONHECENDO MÉTODOS ÚTEIS DA CLASSE STRING
# 
#  A classe string do Python é famosa por ser rica em métodos e possuir uma interface muito fácil de trabalhar.
# Em algumas linguagens manipular sequências de caracteres não é um trabalho trivial, porém, em Python esse 
# trabalho é muito simples.
#
# Maiúscula, minúscula, e título:
curso = "pYtHon"

print(curso.upper()) # PYTHON

print(curso.lower()) # python

print(curso.title()) # Python

# Eliminando espaço em branco
curso = "       Python  "

print(curso.strip())  # "Python"

print(curso.lstrip()) # "Python  "

print(curso.rstrip()) # "       Python"

# Junções e centralização
curso = "Python"

print(curso.center(10, "#")) # "##Python##"

print(".".join(curso)) # "P.y.t.h.o.n"