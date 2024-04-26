# Calculo de bonus com entrada do usuario

''''
Para resolver os bugs identificados — tratamento de entradas inválidas que não podem ser convertidas para um número de ponto flutuante 
e prevenção de valores negativos para salário e bônus, você pode modificar o código diretamente. Isso envolve adicionar verificações 
adicionais após a tentativa de conversão para garantir que os valores sejam positivos.
'''

ano_vigente: int = 2024
valor_base_calculo_bonus: int = 1000
limite_bonus: int = 3

# 1) Solicita ao usuário que digite seu nome
try:
    nome_usuario: str = input("Digite seu nome: ").title()
    if len(nome_usuario)==0:
        print('Digite um nome valido')
        exit()
    elif any(char.isdigit() for char in nome_usuario):
        print('Verifique o nome, nao pode conter numeros')
        exit()
except ValueError as e:
    print({e})

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
try:
    salario_usuario: float = float(input("Digite o valor do seu salario: R$"))
    if salario_usuario < 0 or salario_usuario == 0:
        print('Verifique o valor informado para o salário')
        exit()
except ValueError:
    print('Entrada inválida para o salário')     
    exit()   

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
try:
    bonus_usuario: float = float(input("Informe o valor do bonus recebido: "))
    if bonus_usuario < 0 or bonus_usuario > limite_bonus:
        print(f'Verifique o valor informado para o bonus.\nLimite de bonus definido para o período: {limite_bonus}')
        exit()
except ValueError:
    print('Entrada inválida para o bonus')     
    exit()   
# 4) Calcule o valor do bônus final
calculo_valor_bonus_usuario = valor_base_calculo_bonus + salario_usuario * bonus_usuario

# 5) Imprima cálculo do KPI para o usuário
# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"{nome_usuario} seu salario é R${salario_usuario:.2f} e o valor do bonus a receber referente ao ano de {ano_vigente} é de R${calculo_valor_bonus_usuario:.2f}")
