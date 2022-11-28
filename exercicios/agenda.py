agenda = []


def pede_nome():
    return (input("Nome: "))


def pede_telefone():
    return (input("Telefone: "))


def pede_email():
    return (input("email: "))


def mostra_dados(nome, telefone, email):
    print("\nNome: %s\nTelefone: %s\nEmail: %s" % (nome, telefone, email))


def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None


def novo():
    global agenda
    nome = pede_nome()
    telefone = pede_telefone()
    email = pede_email()
    agenda.append([nome, telefone, email])


def apaga():
    global agenda
    nome = pede_nome()
    p = pesquisa(nome)
    if p != None:
        del agenda[p]
    else:
        print("Nome não encontrado.")


def altera():
    p = pesquisa(pede_nome())
    if p != None:
        nome = agenda[p][1]
        telefone = agenda[p][2]
        email = agenda[p][3]
        print("Encontrado:")
        mostra_dados(nome, telefone, email)
        nome = pede_nome()
        telefone = pede_telefone()
        email = pede_email()
        agenda[p] = [nome, telefone, email]
    else:
        print("Nome não encontrado.")


def lista():
    print("\nAgenda\n\n------")
    for posição, e in enumerate(agenda):
        print("Posição: %d " % posição, end="")
        mostra_dados(e[0], e[1], e[2])
    print("------\n")


def ordena():
    fim = len(agenda)
    while fim > 1:
        i = 0
        trocou = False
        while i < (fim - 1):
            if agenda[i] > agenda[i + 1]:
                temp = agenda[i + 1]
                agenda[i + 1] = agenda[i]
                agenda[i] = temp
                trocou = True
            i += 1
        if not trocou:
            break


def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return (valor)
        except ValueError:
            print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))


def menu():
    print("""
   1 - Novo
   2 - Altera
   3 - Apaga
   4 - Lista
   5 - Ordena por nome

   0 - Sai
""")
    print("\nNomes na agenda: %d\n" % len(agenda))
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 5)


while True:
    opção = menu()
    if opção == 0:
        break
    elif opção == 1:
        novo()
    elif opção == 2:
        altera()
    elif opção == 3:
        apaga()
    elif opção == 4:
        lista()
    elif opção == 5:
        ordena()