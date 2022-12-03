# A função zip() vai iterar sobre varias listas diferentes ao mesmo tempo

import random

alunos = ['Ewerton', 'Felipe', 'Clara', 'João']

notas = [random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10)]

for aluno, nota in zip(alunos, notas):
    print(f'O aluno {aluno} obteve a nota {nota:.2f}')