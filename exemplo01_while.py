# A estrutura de repetição while é utilizada quando desejamos repetir 
# um bloco de código enquanto uma condição for verdadeira. Diferente 
# do for, que normalmente é usado quando sabemos exatamente a quantidade 
# de repetições, o while trabalha baseado em uma condição lógica.

# Neste exemplo, utilizaremos uma variável de controle para contar as 
# repetições manualmente. O laço continuará executando enquanto a 
# variável for menor que 10.


# variável de controle
contador = 0

# o bloco será repetido enquanto contador for menor que 10
while contador < 10:

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

    # incrementa o contador
    # sem isso o laço ficaria infinito
    contador += 1