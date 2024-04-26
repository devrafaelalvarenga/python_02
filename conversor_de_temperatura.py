'''
Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, 
garantir que a entrada seja numérica, tratando qualquer ValueError. 
Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.
'''

try:
    celcius = float(input('Informe a temperatura em graus Celcius: '))
    fahrenheit = (celcius * 9/5) + 32
    print(f'A conversão de {celcius}°C para fahrenheit é: {fahrenheit}°F ')
except ValueError:
    print('Por favor, digite um valor valido.')
else:
    print('Conversão efetuada com sucesso')    

