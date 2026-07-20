### **Introdução**

Um ambiente virtual no Python é um **espaço isolado** onde você pode instalar e gerenciar pacotes de forma independente para cada projeto. Cada ambiente possui sua própria instalação do Python e suas bibliotecas, o que é fundamental para evitar conflitos de dependências entre diferentes trabalhos.

As principais **vantagens** de utilizar um ambiente virtual são:

* **Isolamento:** As bibliotecas instaladas em um ambiente não afetam outros projetos, permitindo que você utilize versões diferentes de uma mesma biblioteca simultaneamente no sistema.  
* **Manutenção:** Facilita o controle e a documentação das dependências, tornando o projeto mais fácil de ser compartilhado ou migrado.  
* **Compatibilidade:** Garante que o projeto utilize exatamente as versões de que precisa para funcionar corretamente.

### **Quando usar um ambiente virtual?**

É considerada uma boa prática configurar um ambiente virtual **sempre que iniciar um novo projeto**. Isso garante organização e evita que o desenvolvimento dependa de bibliotecas instaladas globalmente, prevenindo potenciais conflitos.

### **Configurando no PyCharm**

O PyCharm simplifica esse processo durante a criação de um novo projeto:

1. Escolha o local para salvar o projeto.  
2. Na seção **"Python Interpreter"**, selecione a opção **"New environment using"**.  
3. Escolha **"Virtualenv"** para indicar que deseja um novo ambiente isolado.  
4. Clique em **"Create"** e o software criará automaticamente o ambiente dentro do diretório do projeto.

### **Testando o ambiente**

Após a configuração, você pode verificar se tudo está funcionando criando um programa simples:

1. Abra o arquivo `main.py` (criado automaticamente pelo PyCharm).  
2. Insira o código: `print("Hello, World!")`.  
3. Clique com o botão direito no arquivo e selecione **"Run 'main'"**.  
4. A exibição da mensagem no console confirma que o ambiente virtual está configurado e pronto para o desenvolvimento.

