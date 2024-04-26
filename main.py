# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

num_1 = int(input('Insira o primeiro numero inteiro: '))
num_2 = int(input('Insira o segundo numero inteiro: '))
soma = num_1 + num_2
#print(f'{num_1} + {num_2} = {soma}')


# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

divisor = 5
num_1 = float(input('Insira o primeiro numero: '))
resto_divisao = num_1 % 5
#print(f'O resto da divisão de {num_1} / {divisor} = {resto_divisao}')


# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

num_1 = float(input('Insira o primeiro numero: '))
num_2 = float(input('Insira o segundo numero: '))
multiplicacao = num_1 * num_2
#print(f'{num_1} * {num_2} = {multiplicacao}')


# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

num_1 = int(input('Insira o primeiro numero inteiro: '))
num_2 = int(input('Insira o segundo numero inteiro: '))
divisao = num_1 // num_2
#print(f'{num_1} / {num_2} = {divisao}')


# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

num_1 = float(input('Insira o primeiro numero: '))
quadrado = num_1 ** 2
#print(f'{num_1} ** 2 = {quadrado}')


# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

num_1 = float(input('Insira o primeiro numero: '))
num_2 = float(input('Insira o segundo numero: '))
soma = num_1 + num_2
#print(f'{num_1} + {num_2} = {soma}')


# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

num_1 = float(input('Insira o primeiro numero: '))
num_2 = float(input('Insira o segundo numero: '))
media = (num_1 + num_2) / 2
#print(f'Média de {num_1} + {num_2} = {media}')


# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

num_1 = float(input('Insira o primeiro numero: '))
num_2 = float(input('Insira o expoente para o calculo: '))
potencia = num_1 ** num_2
#print(f'A potencia de {num_1} elevado a {num_2} = {potencia}')


# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# formula: (0 °C × 9/5) + 32 = 32 °F

celcius = float(input('Informe a temperatura em graus Celcius: '))
fahrenheit = (celcius * 9/5) + 32
#print(f'A conversão de {celcius}°C para fahrenheit é: {fahrenheit}°F ')


# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# formula: A = π·r2, se se conhece o raio r;

import math

#pi = 3.14
raio = int(input('Informe o raio para o calculo da area do circulo: '))
area = math.pi * (raio ** 2)
#print(f'{area:.2f}')


# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

palavra = input('Digite uma palavra: ')
palavra_maiuscula = palavra.upper()
#print(palavra_maiuscula)


# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

nome_usuario = input('Informe seu nome completo: ')
nome_usuario_minusculo = nome_usuario.lower()
#print(nome_usuario_minusculo)


# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

frase = input('Digite uma frase: ')
frase_sem_espaco = frase.strip()
#print(frase) #frase com espaço
#print(frase_sem_espaco)


# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# opcao 1
data = input('Digite uma data no formato dd/mm/aaaa: ')
dia = data[0:2]
mes = data[3:5]
ano = data[6:10]
#print(f'dia:{dia}, mes:{mes}, ano:{ano}')
 
#opcao2
data = input('Digite uma data no formato dd/mm/aaaa: ')
data = data.split("/") 
#print(data)
#print(f'Dia: {data[0]}, Mes: {data[1]}, Ano: {data[2]}')

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

primeiro_nome = input('Informe seu primeiro nome: ')
segundo_nome = input('Informe seu sobrenome: ')
nome_completo = primeiro_nome.title() +' '+ segundo_nome.title()
#print(nome_completo)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
expressao1 = input('Escolha uma expressão booleana entre True e False: ').title()
expressao2 = input('Escolha uma expressão booleana entre True e False: ').title()

if expressao1 == expressao2:
    print(f'{expressao1} AND {expressao2} = True')
else:
    print(f'{expressao1} AND {expressao2} = False')  

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

valor_booleano = input('Insira um valor booleano True or False: ')
if valor_booleano == 'True':
    print('False')
elif valor_booleano == 'False':
    print('True')


# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

num_1 = int(input('Insira o primeiro numero: '))
num_2 = int(input('Insira o segundo numero: '))
if num_1 == num_2:
    print('Numeros são iguais')
else:
    print('Numeros são diferentes')    


# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

num_1 = int(input('Insira o primeiro numero: '))
num_2 = int(input('Insira o segundo numero: '))
if num_1 == num_2:
    print('Numeros são iguais')
else:
    print('Numeros são diferentes')    

# #### try-except e if

#Exercício 21: Conversor de Temperatura
#Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

#Exercício 22: Verificador de Palíndromo
#Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.

#Exercício 23: Calculadora Simples
#Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

#Exercício 24: Classificador de Números
#Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".

#Exercício 25: Conversão de Tipo com Validação
#Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros. Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.


# codigo sem erro

nome = 'Rafael'
try: #tenta isso se estiver correto imprimi o resultado
    resultado = len(nome) #erro 
    print(resultado)
except: #se der errado imprimi o erro
    print('Tudo errado')    
else: #se der td certo, faça isso tb
    print('Tudo certo!')
finally: #independete do que aconteceu, faça isso tambem
    print('Chegamos ao fim')     

# codigo com erro

nome = 'Rafael'
try: #tenta isso se estiver correto imprimi o resultado
    resultado = len(nome) #erro 
    print(resultado)
except: #se der errado imprimi o erro
    print('Tudo errado')    
else: #se der td certo, faça isso tb
    print('Tudo certo!')
finally: #independete do que aconteceu, faça isso tambem
    print('Chegamos ao fim')    


# codigo sem erro
nome = 'Rafael'
if isinstance(nome, str): #verifique se a variavel é uma string
    print('A variavel é uma string')
else:
    print('A variavel não é uma string')    

# codigo sem erro
nome = 123456
if isinstance(nome, str): #verifique se a variavel é uma string
    print('A variavel é uma string')
else:
    print('A variavel não é uma string')       
  