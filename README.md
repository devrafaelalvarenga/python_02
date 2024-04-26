# python_02

- pyenv local 3.12.2
- poetry init
- poetry env use 3.12.2

TypeError
Um TypeError ocorre em Python quando uma operação ou função é aplicada a um objeto de tipo inadequado. Python não sabe como aplicar a operação porque os tipos de dados não são compatíveis.

Type Check
Verificação de tipo (type check) é o processo de verificar o tipo de uma variável. Isso pode ser útil para garantir que operações ou funções sejam aplicadas apenas a tipos de dados compatíveis, evitando erros em tempo de execução.

Exemplo de Type Check
Para verificar o tipo de uma variável em Python, você pode usar a função type() ou isinstance().

Type Conversion
Conversão de tipo (type conversion), também conhecida como casting, é o processo de converter o valor de uma variável de um tipo para outro. Python oferece várias funções integradas para realizar conversões explícitas de tipo, como int(), float(), str(), etc.

try-except
A estrutura try-except é usada para tratamento de exceções em Python. Uma exceção é um erro que ocorre durante a execução do programa e que, se não tratado, interrompe o fluxo normal do programa e termina sua execução. O tratamento de exceções permite que o programa lide com erros de maneira elegante, permitindo que continue a execução ou falhe de forma controlada.

try: Este bloco é o primeiro na estrutura de tratamento de exceções. Python tenta executar o código dentro deste bloco.
except: Se uma exceção ocorrer no bloco try, a execução imediatamente salta para o bloco except. Você pode especificar tipos de exceção específicos para capturar e tratar apenas essas exceções. Se nenhum tipo de exceção for especificado, ele captura todas as exceções.

if
O if é uma estrutura de controle de fluxo que permite ao programa executar diferentes ações com base em diferentes condições. Se a condição avaliada pelo if for verdadeira (True), o bloco de código indentado sob ele será executado. Se a condição for falsa (False), o bloco de código será ignorado.

if: Avalia uma condição. Se a condição for verdadeira, executa o bloco de código associado.
elif: Abreviação de "else if". Permite verificar múltiplas condições em sequência.
else: Executa um bloco de código se todas as condições anteriores no if e elif forem falsas.

elif idade == 18:
    print("Exatamente 18 anos")
else:
    print("Maior de idade")
Ambas as estruturas, try-except e if, são fundamentais para a criação de programas em Python que são capazes de lidar com situações inesperadas (como erros de execução) e tomar decisões com base em condições, permitindo assim que você construa programas mais robustos, flexíveis e seguros.

Any(xyz) / All(xyz)

any() retorna:

True - se pelo menos um elemento de um iterável for verdadeiro
False - se todos os elementos forem falsos ou se um iterável estiver vazio

all() retorna:

True – se todos os elementos em um iterável forem verdadeiros
False – Se algum elemento em um iterável for falso
