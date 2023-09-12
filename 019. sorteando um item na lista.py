from random import choice
aluno1 = str(input('Digite um nome: '))
aluno2 = str(input('Digite mais um nome: '))
aluno3 = str(input('Digite outro nome: '))
aluno4 = str(input('Digite o ultimo nome: '))
alunos = [aluno1, aluno2, aluno3, aluno4]
print('O aluno escolhido foi {}.'.format(choice(alunos)))