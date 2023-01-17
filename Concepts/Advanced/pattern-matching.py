# PADRÕES LITERAIS
genero = "G"

match genero:
    case "M":
        print("Gênero Masculino")
    case "F":
        print("Gênero Feminino")
    case _:
        print("Not found")

age = 15
match age:
    case x if x < 18:
        print("Menor de idade")


# PADRÕES CORINGA (WILDCARD)
genero = "A"

match genero:
    case "M":
        print("Gênero Masculino")
    case "F":
        print("Gênero Feminino")
    case _:
        print("Gênero não encontrado")

# PADRÕES DE SEQUÊNCIA e de CAPTURA(dar nome as variváveis)
#notas = []
#notas = [5]
#notas = [5,8]
#notas = [5,10,6]
notas = [0,5,9]

match notas:
    case []:
        print("O aluno não realizou nenhuma prova")
    case [p1]:
        print(f"O aluno realizou uma prova e sua média foi: {p1/3:.2f}")
    case [p1,p2]:
        print(f"O aluno realizou duas provas e sua média foi: {(p1+p2)/3:.2f}")
    case [0, *resto]: # vai pegar todas as posições, fora a primeira posição e colocar na váriavel resto
        print(f"O aluno zerou a primeira prova e as notas seguintes foram: {resto}")
    case [p1,p2, p3]:
        print(f"O aluno realizou três provas e sua média foi: {(p1+p2+p3)/3:.2f}")


# PADRÕES OR
notas = [0.0,5,9]

match notas:
    case []:
        print("O aluno não realizou nenhuma prova")
    case [p1]:
        print(f"O aluno realizou uma prova e sua média foi: {p1/3:.2f}")
    case [p1,p2]:
        print(f"O aluno realizou duas provas e sua média foi: {(p1+p2)/3:.2f}")
    case [0 | 0.0, *resto]: # vai pegar todas as posições, fora a primeira posição e colocar na váriavel resto
        print(f"O aluno zerou a primeira prova e as notas seguintes foram: {resto}")
    case [p1,p2, p3]:
        print(f"O aluno realizou três provas e sua média foi: {(p1+p2+p3)/3:.2f}")


# PADRÕES AS
notas = [0.0,5,9]

match notas:
    case []:
        print("O aluno não realizou nenhuma prova")
    case [p1]:
        print(f"O aluno realizou uma prova e sua média foi: {p1/3:.2f}")
    case [p1,p2]:
        print(f"O aluno realizou duas provas e sua média foi: {(p1+p2)/3:.2f}")
    case [0 | 0.0, *resto] as lista: # vai pegar todas as posições, fora a primeira posição e colocar na váriavel resto
        print(f"Primeira nota: {lista[0]}") # usado para ter acesso a primeira variável
        print(f"O aluno zerou a primeira prova e as notas seguintes foram: {resto}")
    case [p1,p2, p3]:
        print(f"O aluno realizou três provas e sua média foi: {(p1+p2+p3)/3:.2f}")