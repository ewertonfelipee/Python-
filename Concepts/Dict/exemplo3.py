fila = {
    '0' : 'Maria',
    '1' : 'João',
    '2' : 'Ana',
    '3' : 'Paula',
    '4' : 'Charles'
}

print(fila)

del fila['0']

print(fila)

fila.pop('4')

print(fila)

fila.popitem()

print(fila)

fila.clear()

print(fila)