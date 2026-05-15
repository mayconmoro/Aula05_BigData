# Diferente dos exemplos anteriores, neste caso o while não está controlando uma 
# quantidade fixa de repetições. Agora a repetição depende da decisão do usuário.

# Esse tipo de estrutura é muito utilizado em sistemas reais, principalmente em menus, 
# cadastros, cálculos, registros de vendas e programas onde não sabemos antecipadamente 
# quantas vezes o processo deverá acontecer.

# O laço continuará executando enquanto a resposta for igual a "S".



# variável de controle
# inicia com "S" para permitir a primeira execução
resposta = 'S'

# enquanto a resposta for igual a S
while resposta == 'S':

    # recebe um número do usuário
    num = float(input('Informe o número: '))

    # aqui poderiam existir várias outras instruções
    # como cálculos, somas, cadastros, etc.

    # pergunta ao usuário se deseja continuar
    resposta = input('Quer continuar? [S/N]: ').upper()