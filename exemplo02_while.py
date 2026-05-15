# Diferente da estrutura for, onde normalmente já definimos a quantidade 
# de repetições utilizando o range(), no while precisamos controlar manualmente 
# o início, a condição de parada e o incremento da repetição.

# Isso faz com que o while seja mais flexível, porém também exige mais atenção 
# do programador. Caso o contador não seja incrementado corretamente, 
# o laço pode se tornar infinito.



# -----------------------------------------------
# Exemplo de while infinito - ISSO NÃO É BOM!
# -----------------------------------------------
# variável de controle
contador = 0

# enquanto contador for menor que 5
while contador < 5:
    # exibe a palavra Python
    print('Python')

# nesse exemplo o contador nunca aumenta, por isso a condição sempre 
# continuará verdadeira gerando um laço infinito




# -----------------------------------------------
# While com controle correto
# -----------------------------------------------

# variável de controle
contador = 0

# enquanto contador for menor que 5
while contador < 5:
    # exibe a palavra Python
    print('Python')

    # incrementa o contador
    # significa: contador recebe um novo valor, que é: o que já existia guardado em contador somando + 1.
    contador = contador + 1

# Neste exemplo, o laço funciona corretamente porque o contador é atualizado
# a cada repetição. Quando o contador chegar em 5, a condição ficará falsa e o laço será encerrado.




# -----------------------------------------------
# Exibindo o valor da repetição
# -----------------------------------------------

# variável de controle
c = 0

# enquanto c for menor que 10
while c < 10:
    # exibe a palavra Python junto do contador
    print(f'Python {c}')

    # forma reduzida de incremento
    # Isto é o mesmo que escrever c = c + 1
    c += 1 

# Nesse caso, além da repetição, conseguimos visualizar o valor atual do contador.
# Irá imprimir: Python 1, Python 2, Python 3, ..., até Python 9.
# O operador += é uma forma simplificada de escrever:




# -----------------------------------------------
# While com entrada de dados
# -----------------------------------------------

# variável de controle
cont = 0

# variável acumuladora
soma = 0

# enquanto cont for menor que 5
while cont < 5:
    # recebe um número do usuário
    numero = float(input('Informe o número: '))

    # acumula os valores digitados
    # variável soma, recebe o somatório do que já existia guardado nela somado ao valor da variável número
    soma = soma + numero

    # incrementa o contador na versão reduzida
    cont += 1

# exibe a soma total
print(soma)

# Neste último exemplo:
    # cont controla a quantidade de repetições;
    # soma funciona como variável acumuladora;
    # a cada repetição, o valor digitado é somado ao total;
    # no final, o programa mostra a soma de todos os números informados.