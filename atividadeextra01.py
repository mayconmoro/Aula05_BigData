# Crie um algoritmo, que solicite ao usuário a digitação de um número (inteiro ou decimal). O algoritmo então, deve exibir uma mensagem indicando, se o número é: 
# Positivo,
# Negativo,
# Ou zero.

# Entrada de número pelo usuário.
numero = float(input('Digite um número: '))

# Processamento da informação:
match  numero:
    case n if n > 0:
        print("Positivo")
    case n if n < 0:
        print('Negativo')
    case _:
        print('Zero')

print('\nInformação concluída!')

