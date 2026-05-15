# Neste exemplo, realizamos uma melhoria nas condições do match case. 
# Diferente do código anterior, agora os intervalos foram definidos de 
# maneira mais explícita, deixando o código mais organizado, 
# seguro e fácil de entender.

# Antes, o programa verificava apenas, se a idade era menor que 12 
# ou menor que 18. Agora, cada faixa etária possui um intervalo claramente 
# definido, mostrando exatamente quais valores pertencem a cada classificação.

# Outra vantagem dessa alteração é que valores inválidos, como 
# idades negativas, não entram em nenhuma categoria e acabam 
# sendo tratados no case _, funcionando como uma validação.

# exibe as classificações de idade
print('''
CLASSIFICAÇÃO DE IDADE:
ADULTO: 18 Anos ou mais
ADOLESCENTE: 12 a 17 anos
CRIANÇA: 11 anos ou menos
''')

# recebe a idade digitada pelo usuário
idade = float(input('Informe a idade: '))

# verifica a idade informada
match idade:

    # verifica se a idade está entre 0 e 11
    case i if 0 <= i < 12:
        print('Criança')

    # verifica se a idade está entre 12 e 17
    case i if 12 <= i < 18:
        print('Adolescente')

    # verifica se a idade é 18 ou maior
    case i if i >= 18:
        print('Adulto')

    # caso a idade não se encaixe em nenhuma condição
    # exemplo: idade negativa
    case _:
        print('Opção inválida')