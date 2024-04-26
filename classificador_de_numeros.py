''''
Escreva um programa que solicite ao usuário para digitar um número. 
Utilize try-except para assegurar que a entrada seja numérica e 
utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". 
Adicionalmente, identifique se o número é "par" ou "ímpar".
'''

numero_usuario = input('Digite um numero inteiro: ')


def classificador_numerico(numero_usuario: int):
    try:
        numero_usuario = int(numero_usuario)
    except ValueError as e:
        print(f'{e}')    

    if numero_usuario > 0 and numero_usuario % 2 == 0:
        print('Numero positivo e par')
    elif numero_usuario < 0 and numero_usuario % 2 == 0:
        print('Numero negativo e par') 
    elif numero_usuario > 0 and numero_usuario % 2 != 0:
        print('Numero positivo e impar')  
    elif numero_usuario < 0 and numero_usuario % 2 != 0:
        print('Numero negativo e impar')              
    else:
        print('Numero igual a zero')       
    
classificador_numerico = classificador_numerico(numero_usuario)        