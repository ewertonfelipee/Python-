import random

alunos = ['Ewerton', 'Felipe', 'Clara', 'João']

# for aluno in alunos:
#     print(f'O nome do aluno é: {aluno}')

# for aluno in alunos:
#     nota = random.randint(0, 10)
#     print(f'O aluno {aluno} obteve nota: {nota}')

for aluno in alunos:
    nota1 = random.randint(0, 10)
    nota2 = random.randint(0, 10)
    nota3 = random.randint(0, 10)

    nota_final = nota1 * 0.2 + nota2 * 0.3 + nota3 * 0.5
    print(f'O aluno {aluno} obteve nota: {nota_final:.2f}')