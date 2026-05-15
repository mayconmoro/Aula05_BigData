# Escreva um algoritmo em Python, que receba um valor monetário de venda fornecido pelo usuário e classifique esta venda de acordo com as seguintes regras:
	# Venda pequena: Valores inferiores a 100.
	# Venda média: Valores entre 100 (inclusivo) e 500 (exclusivo).
	# Venda grande: Valores iguais ou superiores a 500.

# Valor fornecido pelo usuário.
venda = float(input('Digite o valor total da venda: '))

# Info. sobre classificação das compras.
print('\n##### INFORMATIVO #####\n')
print('[Venda Grande] Compras de R$ 500.00 ou superior\n[Venda Média] Compras com valores entre R$ 100.00 e R$ 499.99\n[Venda Pequena] Compras com valor abaixo de R$ 100.00')

# Processamento da compra.
match venda:
    case v if v >= 500:        
        print('\nVenda grande!')        
        print(f'O valor da venda foi de R$ {venda:.2f}')
        
    case v if v < 500 and v >= 100:
        print('\nVenda média!')
        print(f'O valor da venda foi de R$ {venda:.2f}')
        
    case _:        
        print('\nVenda pequena')        
        print(f'O valor da venda foi de R$ {venda:.2f}')
        

