'''''
Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a 
operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

'''
def somar(numero1, numero2):
    return numero1 + numero2

def subtrair(numero1, numero2):
    return numero1 - numero2

def dividir(numero1, numero2):
    return numero1 / numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2

numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
operacao = int(input('Digite a operação desejada:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n:'))

if operacao == 1:
    adicao = somar(numero1=numero1, numero2=numero2)
    print(f'O resultado de {numero1} + {numero2} = {adicao}')
elif operacao == 2:
    subtracao = subtrair(numero1=numero1, numero2=numero2)
    print(f'O resultado de {numero1} - {numero2} = {subtracao}')        
elif operacao == 3:
    multiplicacao = multiplicar(numero1=numero1, numero2=numero2)
    print(f'O resultado de {numero1} * {numero2} = {multiplicacao}')
try:        
    if operacao == 4:
        divisao = dividir(numero1=numero1, numero2=numero2)
        print(f'O resultado de {numero1} / {numero2} =  {divisao}')
except ZeroDivisionError as e:
    print(f'Erro identificado: {e}')

