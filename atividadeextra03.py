# Desenvolva um programa que solicite o valor de um ingresso e permita ao usuário escolher o tipo de entrada.
# As opções disponíveis são:
# ·	1 - Inteira (sem desconto); 
# ·	2 - Meia entrada (50% de desconto); 
# ·	3 - Promoção (30% de desconto). 
# De acordo com a opção escolhida, o programa deve calcular e exibir o valor final do ingresso. Caso o usuário informe uma opção inválida, o programa deve exibir uma mensagem informando o erro.

# Opções disponíveis
print('''
[1] - Inteira
[2] - Meia Entrada (50% de desconto)
[3] - Promoção (30% de desconto)
''')

# Opção definida pelo usuário.
ingresso = int(input('Escolha uma opção de ingresso: '))

# Variável pré-definida.
valor_ingresso = 50
desconto_meia = valor_ingresso * 0.5 # 50% de desconto
desconto_promo = valor_ingresso * 0.3 # 30% de desconto

# Processamento do pedido.
match ingresso:
    case 1:
        print(f'\nOpção Inteira selecionada.\nValor do ingresso: R$ {valor_ingresso:.2f}')
        print(f'Valor a pagar de R$ {valor_ingresso:.2f}')
    
    case 2:
        print(f'\nOpção Meia Entrada selecionada.\nValor do ingresso: R$ {valor_ingresso:.2f}')
        print(f'Desconto de R$ {desconto_meia:.2f}')
        print(f'Valor a pagar de R$ {valor_ingresso - desconto_meia}')

    case 3:
        print(f'\nOpção de Promoção selecionada.\nValor do ingresso: R$ {valor_ingresso:.2f}')
        print(f'Desconto de R$ {desconto_promo:.2f}')
        print(f'Valor a pagar de R$ {valor_ingresso - desconto_promo}')
    
    case _:
        print('Opção Inválida, selecione entre as opções de 1 a 3')
