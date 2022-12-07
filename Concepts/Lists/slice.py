lista = ['a', 'b', 'c', 'd', 'e', 'f']

#lista1 = slice(0,7,2)
print(lista[::2])

#lista2 = slice(1,7,2)
print(lista[1::2])

print(lista[::-1])

lista_result = lista[::2] + lista[1::2]

print(lista_result)