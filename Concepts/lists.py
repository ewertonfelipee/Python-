"""
list = [1,2,3,4]
list.append(10)
list.remove(2)
print('a quantida de elementos da lista eh: %s' % len(list))
#print (list)
for i in list:
	print('os valores da lista sao %d' % i)
"""
"""
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1].title())
message = "My first bicycke was a  %s" % bicycles[0].title() + "."
print(message)
"""
"""
## exercício 3.1
names = ['gugu', 'gaiba', 'deco']
print(names[0]. title())
print(names[1]. title())
print(names[2]. title())

## exercício 3.2

message0 = "hello, my old friends " + names[0] + "!"
message1 = "hello, my old friends " + names[1] + "!"
message2 = "hello, my old friends " + names[2] + "!"
print(message0)
print(message1)
print(message2)
"""
## MODIFICANDO ELEMENTOS EM UMA LISTA
## ACRESCENTANNDO ELEMENTOS NA LISTA
## MÉTODO APPEND()

"""
motorcycles = ['honda', 'yamaha', 'suzuki']
print('lista original')
print(motorcycles)
motorcycles[0] = 'ducati'
print('lista modificada')
print(motorcycles)
motorcycles.append('dafra')
print(motorcycles)
"""
## MÉTODO INSERT()

"""
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(3, 'dafra')
print(motorcycles)
"""
## REMOVENDO ELEMENTOS DE UMA LISTA

## REMOVENDO UM ITEM USANDO A INSTRUÇÃO DEL

"""
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[2]
print(motorcycles)
"""
## REMOVENDO UM ITEM COM O MÉTODO POP()
"""
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
"""
## REMOVENDO UM ITEM USANDO O MÉTODO REMOVE()

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
