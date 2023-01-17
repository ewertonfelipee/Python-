# lista = [1,2,3,4,5]

# iter_lista = iter(lista)

# print(next(iter_lista))
# print(next(iter_lista))
# print(next(iter_lista))
# print(next(iter_lista))
# print(next(iter_lista))

class OddNumber:
    def __init__(self, maximo):
        self.maximo = maximo
        self.atual = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual > self.maximo:
            raise StopIteration

        retorno = self.atual # guarda o valor da itereção passada

        self.atual += 2

        return retorno

par = OddNumber(maximo=20)

for odd in par:
    print(odd, end=" ")


#GENERATOR

def pares(maximo):
    atual = 0

    while atual < maximo:
        yield atual

        atual += 2