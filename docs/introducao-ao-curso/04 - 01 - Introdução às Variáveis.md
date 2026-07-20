Neste material, vamos falar sobre variáveis, um dos conceitos mais importantes na programação. Entender como as variáveis funcionam é essencial para armazenar e manipular dados em seus programas.

### **O Que São Variáveis?**

Uma variável é como uma "caixa" na memória do computador onde você pode armazenar dados para usar mais tarde. Cada variável tem um nome, e você pode atribuir diferentes valores a ela ao longo do programa.

Pense em uma variável como uma etiqueta que identifica o conteúdo que você está guardando. Por exemplo, você pode criar uma variável chamada idade para armazenar a idade de uma pessoa.

Exemplo: *idade \= 25*

Aqui, idade é o nome da variável, e 25 é o valor que está sendo armazenado nela.

### **Regras para Nomear Variáveis**

Existem algumas regras e boas práticas para nomear variáveis em Python: O nome de uma variável deve começar com uma letra ou underline (*), nunca com um número. Pode conter letras, números e underscores (*), mas não pode conter espaços. Nomes de variáveis são sensíveis a maiúsculas e minúsculas. Ou seja, idade, Idade e IDADE são três variáveis diferentes.

*\_idade \= 25 \# Válido* *idade2 \= 30 \# Válido* *2idade \= 40 \# Inválido (não pode começar com número)* *idade do aluno \= 22 \# Inválido (não pode conter espaços)*

### **Atribuição de Valores às Variáveis**

Para atribuir valores às variáveis, usamos o símbolo \=. Uma vez que a variável tem um valor, você pode reutilizá-la sempre que precisar.

Exemplo: *nome \= "Maria"* *idade \= 30* *altura \= 1.65* *print(nome)* *print(idade)* *print(altura)*

Cada vez que você define uma variável, o Python guarda o valor na memória e, quando você quiser acessá-lo, basta chamar o nome da variável.

### **Mudando o Valor de uma Variável**

Uma variável pode mudar de valor ao longo do programa. Isso permite que você reutilize a mesma variável para armazenar novos dados.

Exemplo: *idade \= 25* *print(idade) \# Exibe: 25* *print(idade) \# Exibe: 26*

### **Tipos de Dados em Variáveis**

As variáveis em Python podem armazenar diferentes tipos de dados. Os principais são: **int: números inteiros (ex: 10, \-5) float: números com casas decimais (ex: 3.14, 0.5) str: cadeias de caracteres ou strings (ex: "Olá", "Python")**

Exemplo: *nome \= "Carlos" \# String* *idade \= 28 \# Inteiro* *altura \= 1.75 \# Float*

**Tipagem Dinâmica em Python** Python é uma linguagem de tipagem dinâmica, o que significa que o tipo da variável é definido automaticamente com base no valor atribuído a ela. Você pode até mudar o tipo de dado de uma variável ao longo do programa.

Exemplo: *idade \= 25 \# Inteiro* *idade \= "Vinte e cinco" \# Mudou para string* *print(idade)*

### **Boas Práticas para Nomear Variáveis**

Aqui estão algumas dicas para escolher nomes de variáveis que tornam seu código mais claro e fácil de entender: Use nomes descritivos que expliquem o que a variável representa.

Exemplo: *salario \= 10 \# Nome mais descritivo*

**Utilize o padrão snake\_case, onde palavras são separadas por underscores (\_).**

Exemplo: *salario\_anual \= 50000* *nome\_do\_aluno \= "João"*

### **Trabalhando com Múltiplas Variáveis**

Você pode atribuir valores a várias variáveis ao mesmo tempo, o que torna o código mais conciso.

Exemplo: *nome, idade, altura \= "Paulo", 22, 1.80* *print(nome)* *print(idade)* *print(altura)*

### **Concatenando Strings e Variáveis**

**Para combinar texto com variáveis, utilizamos o f-string.** Isso facilita a formatação de strings em Python, tornando o código mais legível.

Exemplo: *nome \= "Ana"* *idade \= 23* *print(f"Meu nome é {nome} e eu tenho {idade} anos.")*

Com essas informações, você já está preparado para utilizar variáveis nos seus programas Python de forma eficaz. Variáveis são a base de qualquer código e desempenham um papel fundamental na manipulação de dados em seus projetos.

