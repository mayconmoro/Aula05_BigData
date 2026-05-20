# 03 Clientes
# 02 compras
# Calcular o valor total gasto por cada pessoa somando as duas compras informadas
# Ao final de cada cadastro, o programa deverá exibir o total gasto pelo cliente
# ----------------------------------------------------------------------------------

for i in range(3):
    compra01 = float(input('Digite o valor da primeira compra: '))
    compra02 = float(input('Digite o valor da segunda compra: '))
    compra_total = compra01 + compra02

    print(f'\nCliente {i + 1}')
    print(f'Compra 1 é de R$ {compra01:.2f}')
    print(f'Compra 2 é de R$ {compra02:.2f}')
    print(f'Compra total de R$ {compra_total:.2f}')
 
