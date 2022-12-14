#criando um set
# set_1 = {1,3,4,}
# lista = [1,2,5]
# set_2 = set(lista)
# print(set_2)

wallet = {'Bitcoin', 'Etherum', 'Monero', 'Shiba', 'Bcoin'}
print(f'Minha carteira: {wallet}')

# adicionando elemento
wallet.add('Dot')
print(f'carteira após o add(): {wallet}')

# atualizando a carteira
wallet.update({'Dot', 'Litecoin', 'Cardano'})
print(f'carteira após a atualização com o update(): {wallet}')

# removendo elementos com o discard
wallet.discard('Dot')
print(f'Removendo elemento: {wallet}')

# removendo elementos com o remove
# a diferença entre remove e discard é que o remove lança uma exception: KeyError: 'dot'
# se o elemento não estiver no set, a discard não mostra nada
wallet.remove('Shiba')
print(f'removendo elemento: {wallet}')

# removendo com o pop()
wallet.pop()
print(f'removendo aleatoriamente com o pop(): {wallet}')

#removendo com o clear()
#limpa o set
wallet.clear()
print(f'Limpando o set: {wallet}')