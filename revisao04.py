# recebe o valor da compra
valor = float(input('Informe o valor: '))

# exibe as formas de pagamento disponíveis
print('''
FORMAS DE PAGAMENTO:
[1] - PIX (12% de desconto)
[2] - DÉBITO (8% de desconto)
[3] - CRÉDITO (5% de desconto)
[4] - DINHEIRO (15% de desconto)     
''')

# recebe a opção escolhida pelo usuário
opcao = int(input('\nInforme a opção: '))

# variável que armazenará o valor do desconto
desconto = 0

# variável de controle da operação
operacao = True

# verifica a forma de pagamento escolhida
match opcao:
    # caso o usuário escolha PIX
    case 1:
        print('----- Pagamento em PIX -----')
        # calcula 12% de desconto
        desconto = valor * 0.12

    # caso o usuário escolha débito
    case 2:
        print('----- Pagamento em DÉBITO -----')
        # calcula 8% de desconto
        desconto = valor * 0.08

    # caso o usuário escolha crédito
    case 3:
        print('----- Pagamento em CRÉDITO -----')
        # calcula 5% de desconto
        desconto = valor * 0.05

    # caso o usuário escolha dinheiro
    case 4:
        print('----- Pagamento em DINHEIRO -----')
        # calcula 15% de desconto
        desconto = valor * 0.15

    # caso o usuário digite uma opção inválida
    case _:
        # altera o estado da operação para falso
        operacao = False
        print('Opção Inválida')


# Formas alternativas de validar a operação
# if desconto != 0:  # se operacao for diferente de 0, quer dizer que o valor digitado foi válido e o desconto foi calculado
# if operacao == True:  # se operacao continuar como True, entra no if. (o valor digitado foi válido)

# verifica se a opção digitada está dentro da lista válida
if opcao in [1, 2, 3, 4]:

    # calcula o valor final após o desconto
    valor_final = valor - desconto

    # exibe os resultados
    print(f'Preço normal: R$ {valor:.2f}')
    print(f'Valor do Desconto: R$ {desconto:.2f}')
    print(f'Total à Pagar R$ {valor_final:.2f}')

# caso a opção seja inválida
else:
    print('Escolha uma opção válida')
