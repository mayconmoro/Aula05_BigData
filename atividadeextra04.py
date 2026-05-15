# Desenvolva um algoritmo que receba 10 valores de vendas.
# Para cada venda, o programa deve calcular um desconto de 10% caso o valor seja superior a R$ 1000,00.
# Ao final de cada venda, o sistema deve exibir o valor informado e, se houver, o valor do desconto aplicado.

# Estrutura de repetição.
for v in range(10):
    print(f'\nVenda {v + 1}')

    # Entrada de valor da venda fornecida pelo usuário.
    venda = float(input('Digite o valor da venda: '))

    # Variáveis pré definidas.
    taxa_desconto = 0.1
    desconto = venda * taxa_desconto
    venda_minima = 1000

    # Condições para o desconto.
    if venda >= venda_minima:
        print(f'\nTotal de venda: R$ {venda:.2f}')
        print(f'Desconto de 10%: R$ {desconto}')
        print(f'Valor líquido a pagar de R$ {venda - desconto:.2f}')
    else:
        print(f'\nTotal de venda: R$ {venda:.2f}')

    print('\nVenda Concluída!')
        

