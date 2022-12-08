# dictionary = {"nome" : "Ewerton"}
# print(dictionary["nome"])

cadastro = {
    'id' : 1,
    'nome' : 'ozzy',
    'raça' : ['shi-tzu','puddle'],
    'idade' : 3,
    'pelos' : [
        {
            'cor' : 'amarelados',
            'tamanho' : 'médio'
        }
    ]
}

# print(cadastro['id'])
# print(cadastro['nome'])
# print(cadastro['raça'][0])
# print(cadastro['raça'][1])
# print(cadastro['idade'])
# print(cadastro['pelos'])
# print(cadastro['pelos'][0]['cor'])
# print(cadastro['pelos'][0]['tamanho'])

raça = cadastro.get('raça', None)
# None serve para tratar um erro caso uma chave que não existe seja passada
print(raça)