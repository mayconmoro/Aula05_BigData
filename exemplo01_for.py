# Antes de utilizar a estrutura de repetição for, o programa executava os cálculos
# apenas uma vez. Isso significa que, para realizar o processo novamente, 
# seria necessário repetir o código manualmente várias vezes, deixando o 
# programa maior, mais repetitivo e mais difícil de manter.

# Com o uso do for, conseguimos automatizar a repetição das instruções. Nesse exemplo, 
# o bloco de código será executado 5 vezes, permitindo que o usuário informe diferentes 
# números sem precisar duplicar o código.


# -----------------------------------------------
# Exemplo sem o uso da estrutura de repetição For
# -----------------------------------------------

# recebe um número do usuário
numero = int(input('Informe o número: '))

# realiza os cálculos
dobro = numero * 2
triplo = numero * 3
quadrado = numero ** 2

# exibe os resultados
print(f'O dobro de {numero} é {dobro}')
print(f'O triplo de {numero} é {triplo}')
print(f'O quadrado de {numero} é {quadrado}')



# -----------------------------------------------
# Uso da estrutura de repetição For
# -----------------------------------------------

# O laço for repete o bloco de código 5 vezes
for i in range(5):

    # recebe um número do usuário
    numero = int(input('Informe o número: '))

    # realiza os cálculos
    dobro = numero * 2
    triplo = numero * 3
    quadrado = numero ** 2

    # exibe os resultados
    print(f'O dobro de {numero} é {dobro}')
    print(f'O triplo de {numero} é {triplo}')
    print(f'O quadrado de {numero} é {quadrado}')