# A estrutura de repetição for é utilizada quando sabemos quantas 
# vezes um bloco de código deverá ser executado. Ela permite automatizar 
# tarefas repetitivas, evitando a necessidade de escrever o mesmo 
# código várias vezes.

# No Python, o for normalmente trabalha junto com a função range(), 
# que gera uma sequência de números utilizada para controlar as repetições.




# Nesse primeiro exemplo, o for apenas repete a mesma instrução 10 vezes.
# A variável 'i' foi criada dentro da sintaxe do for. Portanto ela passou a existir, 
# mas não está sendo utilizada dentro do bloco.

# o laço será executado 10x
for i in range(10):
    # imprime a palavra python em cada repetição
    print('python')



# Neste exemplo, a variável 'n' foi criada na sintaxe do for, como da mesma maneira do 
# exemplo anterior e armazena o valor atual da repetição.
# O for exige que inquemos um nome qualquer para esta variável. Muitas vezes a chamamos 
# de "i" ou "n", mas pode ser qualquer nome.
# O range(10) gera os números de 0 até 9, pois a contagem começa no zero e termina antes 
# do valor final informado.

# o laço será executado 5x repetições
for n in range(5):
    # exibe o valor atual da repetição
    # detalhe aqui é que a contagem das vezes, se inicia em 0, e vai até 4
    # Porém, mesmo assim, o laço será executado 5 vezes, pois de 0 a 4 são 5 números
    print(n)
    # após esta linha, o laço volta para o início, e executa novamente o bloco de comandos
    # até que o laço tenha sido repetido 5 vezes.



# Nesse último exemplo, o for está sendo utilizado para repetir um processo completo 
# várias vezes.
# A cada repetição:
    # o usuário informa dois números;
    # o programa calcula a soma;
    # o resultado é exibido na tela.
# Esse tipo de repetição é muito utilizado em cadastros, cálculos, formulários, operações matemáticas 
# e processamento de dados.

# repete a operação 5 vezes
for i in range(5):
    # exibe o número atual da operação -  utilizamos i+1 para começar mostrando do 1 ao invés do 0
    print(f'Operação {i+1}')

    # recebe dois números do usuário
    num1 = float(input('Informe um número: '))
    num2 = float(input('Informe um número: '))

    # realiza a soma
    total = num1 + num2

    # exibe o resultado da soma
    print(total)
    # após esta linha, o laço volta para o início, e executa novamente o bloco de comandos
    # até que o laço tenha sido repetido 5 vezes.