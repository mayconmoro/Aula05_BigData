# ATIVIDADE
# Uma escola deseja desenvolver um sistema para calcular a média final de seus alunos. Crie um programa que realize o cadastro de 10 alunos, recebendo 4 notas para cada um.
# O sistema deverá calcular a média final de cada aluno a partir das notas informadas e, ao final de cada cadastro, exibir a média obtida com duas casas decimais.
# -----------------------------------------------------------------------

for i in range(10):
    nota1 = float(input('\nInserir a primeira nota: '))
    nota2 = float(input('Inserir a segunda nota: '))
    nota3 = float(input('Inserir a terceira nota: '))
    nota4 = float(input('Inserir a quarta nota: '))
    media = (nota1 + nota2 + nota3 + nota4) / 4

    print(f'\nAluno {i + 1}')
    print(f'A média do aluno foi {media:.2f}')

# Versão professor
for aluno in range(10):
    print(f'\nAluno {aluno + 1}')

    soma = 0
    for nota in range(4):
        valor_nota = float(input(f'Informe a nota {nota + 1} do aluno: '))
        soma += valor_nota
        
    media = soma / 4
    print(f'\nA média do aluno {aluno + 1} foi {media:.2f}')

   
