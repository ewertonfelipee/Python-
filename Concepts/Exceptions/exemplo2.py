cadastro_csv = [
    'Joe, 32,SysAdmin',
    'Mariah, 27, FrontEnd Dev',
    'Clark, 42o, Pentester',
    'Tom, 19'
]

def processa_dados(cadastros):

    for cadastro in cadastros:
        dados = cadastro.split(',')

        if len(dados) != 3:
            raise ValueError("Formato incorreto")

        nome = dados[0]


        try:
            idade = int(dados[1])
        except ValueError:
            raise ValueError("Tipo incorreto na conversão dos dados 'idade'")


        cargo = dados[2]

        print(f"{nome} tem {idade} anos e exerce a função de{cargo}")

try:
    processa_dados(cadastro_csv)

except ValueError as e:
    print(f"O erro foi: {e}")