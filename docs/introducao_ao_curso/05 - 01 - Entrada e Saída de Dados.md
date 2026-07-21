

**Introdução**   
Nesta aula, vamos aprender como fazer entrada e saída de dados em Python. Esses conceitos são fundamentais para interagir com o usuário e permitir que ele insira informações e receba respostas do programa. Vamos abordar a função input() para receber dados e a função print() para exibir dados.

**Entrada de Dados com a Função input()**   
A função input() é usada para capturar a entrada do usuário. Ela pausa o programa e espera que o usuário digite algo no teclado, que será retornado como uma string. Um exemplo simples de uso:

Digite seu nome \= input("Digite seu nome: ")   
print(f"Olá, {Digite seu nome}\!")

Neste exemplo, o programa solicita que o usuário digite seu nome e, em seguida, exibe uma mensagem de saudação.

**Convertendo a Entrada do Usuário**   
A função input() sempre retorna uma string, mesmo que o usuário digite números. Se   
precisarmos trabalhar com números, devemos converter a entrada para o tipo apropriado. Veja o exemplo:

idade \= input("Digite sua idade: ")   
idade \= int(idade)   
print(f"Você tem {idade} anos.")

Aqui, a entrada é convertida para um número inteiro usando a função int().

**Tratando Erros de Conversão**   
Quando esperamos um número, o usuário pode digitar algo inválido. Para evitar que o   
programa trave, podemos usar o bloco try/except para tratar esses erros:

try:   
idade \= int(input("Digite sua idade: "))   
print(f"Você tem {idade} anos.")   
except ValueError:   
print("Por favor, insira um número válido.")

Isso garante que, se o usuário digitar algo que não seja um número, o programa exiba uma mensagem de erro amigável.

**Saída de Dados com a Função print()**   
A função print() é usada para exibir mensagens no terminal. Ela pode exibir textos simples, valores de variáveis e realizar formatações. Um exemplo básico de saída de dados:

print("Olá, mundo\!")

Essa função também pode exibir múltiplos itens separados por vírgulas:

nome \= "Leandro"   
idade \= 25   
print("Nome:", nome, "Idade:", idade)

Isso irá exibir: **Nome: Leandro Idade: 25**

**Formatação de Strings com f-strings**   
A partir do Python 3.6, foi introduzida uma nova maneira de formatar strings usando f-strings, que facilita a inserção de variáveis em uma string:

nome \= "Leandro"   
idade \= 25   
print(f"Meu nome é {nome} e eu tenho {idade} anos.")

**Exercício Prático**   
Agora, uma atividade para praticar:

Crie um programa que pergunte ao usuário seu nome, idade e cidade, e em seguida, exiba uma mensagem formatada com essas informações.

Solução:

nome \= input("Digite seu nome: ")   
idade \= int(input("Digite sua idade: "))   
cidade \= input("Digite sua cidade: ")   
print(f"Seu nome é {nome}, você tem {idade} anos e mora em {cidade}.")

**Conclusão**   
Agora você já sabe como fazer entrada e saída de dados em Python, utilizando input() e print(). Esses conceitos são fundamentais para a criação de aplicações que interagem com o usuário.