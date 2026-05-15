# O match case é uma estrutura utilizada para comparar um mesmo valor com várias opções diferentes. 
# Ele funciona de forma parecida com vários if, elif e else, porém deixa o código mais organizado 
# e fácil de ler quando precisamos trabalhar com menus, opções numeradas, categorias ou comandos fixos.
# Geralmente utilizamos match case quando temos muitas possibilidades para uma única variável. 
# Já o if costuma ser mais utilizado em comparações lógicas, intervalos de valores e condições mais complexas.

# Exemplo:
# exibe um menu com as opções disponíveis
print('''
[1] - CRIANÇA
[2] - ADOLESCENTE
[3] - ADULTO
''')

# recebe a opção escolhida pelo usuário
opcao = int(input('Informe uma opção: '))

# verifica o valor digitado na variável opcao
match opcao:
    # caso o usuário digite 1
    case 1:
        print('Criança')
    # caso o usuário digite 2
    case 2:
        print('Adolescente')
    # caso o usuário digite 3
    case 3:
        print('Adulto')
    # caso o usuário digite qualquer outro valor
    case _:
        print('Opção inválida')

