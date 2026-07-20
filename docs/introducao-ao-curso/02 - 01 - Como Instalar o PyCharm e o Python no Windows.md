### **Como Instalar o PyCharm e o Python no Windows**

Para começar a programar, siga estes passos para realizar a instalação corretamente:

#### **Passo 1: Instalar o Python**

Antes de usar o PyCharm, é necessário garantir que o Python esteja no seu sistema.

1. **Baixar o instalador:** Acesse o site oficial (python.org/downloads) e clique em “Download Python”.  
2. **Executar o instalador:** Ao abrir o arquivo `.exe`, **marque a opção “Add Python to PATH”** antes de clicar em “Install Now”. Isso é fundamental para que o sistema reconheça o Python.  
3. **Verificar a instalação:** Abra o terminal (`cmd`) e digite `python --version`. Se aparecer a versão instalada, o processo foi bem-sucedido.

#### **Passo 2: Instalar o PyCharm**

O PyCharm será a sua interface para escrever código (IDE).

1. **Download:** Vá ao site da JetBrains e escolha a **versão Community**, que é gratuita.  
2. **Instalação:** Siga as instruções do instalador e certifique-se de marcar a opção **"Add launchers dir to the PATH"** durante o processo.

#### **Passo 3: Configurar seu Primeiro Projeto**

1. **Novo Projeto:** Ao abrir o PyCharm, clique em **"New Project"**.  
2. **Interpretador:** Na seção "Project venv", você pode selecionar a versão do Python que deseja usar. O PyCharm permite configurar o interpretador diretamente no projeto.  
3. **Finalização:** Clique em **"Create"** para concluir a configuração do ambiente.

#### **Verificando se tudo funciona**

Para testar, crie um arquivo chamado `test.py` dentro do PyCharm com o seguinte código:

print("Instalação completa\!")

Ao executar, a mensagem deve aparecer no terminal do PyCharm, confirmando que você está pronto para desenvolver.

