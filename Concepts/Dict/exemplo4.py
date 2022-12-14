# Métodos de Dicts

family = {
    'Mãe' : 'Maria',
    'Pai' : 'João',
    'filha1' : 'Ana',
    'filha2' : 'Paula',
    'filho1' : 'Charles'
}

print(f'Dict familia: {family}')

# método copy()
family_copy = family.copy()
print(f'Cópia do dict familia é: {family_copy}')

# método itens() retorn chave e valor em formato de lista
itens = family.items()
print(f'Itens: {itens}')
for item in itens:
    print(f'\tChave = {item[0]} e valor = {item[1]}')

# método keys()
chaves = family.keys()
print(f'Chaves: {chaves}')

for chave in chaves:
    print(f'\tchaves: {chave}')

#método values()
valores = family.values()
print(f'Valores: {valores}')
for valor in valores:
    print(f'\tvalores: {valor}')

# método setdefault()
new_key = family.setdefault('avô', 'José')
print(f'A nova chave é: {new_key}')
for item in itens:
    print(f'\tChave = {item[0]} e valor = {item[1]}')

# método fromkeys() cria um dicionário a partir de uma lista de chaves e um valor
chaves = ['Mãe', 'Pai', 'filha1', 'filha2', 'filho1']
valor = 0 # valor iniciado em todos os elementos
jogo = dict.fromkeys(chaves, valor)
print(f'jogo: {jogo}')