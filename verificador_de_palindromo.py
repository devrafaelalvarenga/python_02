'''
Exercício 22: Verificador de Palíndromo.
Crie um programa que verifica se uma palavra ou frase é um palíndromo.
(lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
Utilize try-except para garantir que a entrada seja uma string. 
Dica: Utilize a função isinstance() para verificar o tipo da entrada.
'''
#socorram me subi no ônibus em Marrocos
#ana
#renner
#Roma é amor

from unicodedata import normalize

try:
    string = input('Digite uma palavra ou frase e verifique se ela é um palíndromo: ')
    #string = 12345 
    if isinstance(string, str):
        string_formatada =  normalize('NFKD', string).encode('ASCII','ignore').decode('ASCII').replace(' ', '').lower()
        string_palindromo = string_formatada[::-1].lower() 
        if string_formatada == string_palindromo:
            print(f'A string {string.upper()} é um palíndromo.')     
        else:
            print(f'A string {string.upper()} não é um palíndromo.')
    else:
        print('Verifique a string informada')         
except ValueError:
    print('Verifique os dados informados')

