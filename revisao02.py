# Diferente do exemplo anterior, onde o match case comparava valores exatos (1, 2 e 3), 
# neste código ele está sendo utilizado com condições lógicas utilizando if dentro dos cases.
# Isso faz com que o match case funcione de maneira mais próxima do if/elif, permitindo
# trabalhar com intervalos de valores, como classificação de idade.
# Nesse tipo de situação, muitas vezes o if ainda é mais comum e mais simples de ler,
# porém o match case também consegue resolver o problema utilizando condições adicionais.


# Exemplo
# exibe as classificações de idade
print('''
CLASSIFICAÇÃO DE IDADE:
ADULTO: 18 anos ou mais
ADOLESCENTE: 12 a 17 anos
CRIANÇA: 11 anos ou menos
''')

# recebe a idade do usuário
idade = float(input('Informe a idade: '))

# verifica a idade informada
match idade:

    # captura o valor digitado na variável i
    # e verifica se é menor que 12
    case i if i < 12:
        print('Criança')

    # verifica se a idade é menor que 18
    # (e automaticamente maior ou igual a 12,
    # pois o case anterior já foi testado)
    case i if i < 18:
        print('Adolescente')

    # verifica se a idade é maior ou igual a 18
    case i if i >= 18:
        print('Adulto')

    # caso nenhum case seja atendido
    case _:
        print('Opção inválida')