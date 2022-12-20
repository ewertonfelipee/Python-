tupla = (0, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(f'Quinto elemento da tupla: {tupla[4]}')

print(f'Ultimo elemento da tupla: {tupla[-1]}')

tuple_slicing = tupla[4:]
print(f'Do 5 ao 10 elemento: {tuple_slicing}')

#Não se pode fazer alterações ou deleções na tupla, principal diferença entre tupla e lista
# tupla[0] = 1
# print(tupla) TypeError: 'tuple' object does not support item assignment

# A tupla inteira pode ser apagada
# del tupla
# print(tupla)

print(f'Quantidade de elementos iguais a 1: {tupla.count(1)}')

print(f'O elemento 4 esta na posição: {tupla.index(4)}')