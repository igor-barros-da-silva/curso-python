Para preparar seu ambiente de desenvolvimento e começar a programar em Python no Mac, siga os passos abaixo:

### **Passo 1 – Instalando o Python no macOS**

1. **Baixar o instalador:** Acesse o site oficial (python.org/downloads) e baixe a versão para macOS.  
2. **Executar a instalação:** Abra o arquivo `.pkg` baixado e siga o assistente de instalação clicando em **Continuar** e, finalmente, em **Instalar**.  
3. **Verificar a versão:** Após concluir, abra o Terminal e digite o comando `python3 --version` para confirmar se a instalação foi bem-sucedida.  
   * **Dica:** No macOS, é importante sempre utilizar o comando **`python3`**, pois o comando `python` pode estar vinculado a versões antigas (2.x) do sistema.

### **Passo 2 – Instalando o PyCharm no Mac**

1. **Download:** Vá ao site da JetBrains e baixe a **versão Community**, que é gratuita.  
2. **Instalação:** Abra o arquivo `.dmg` e **arraste o ícone do PyCharm para a pasta Applications**.  
3. **Configuração Inicial:** Ao abrir o software pela primeira vez, selecione "Do not import settings".  
4. **Interpretador:** Crie um novo projeto e selecione o interpretador Python 3 instalado anteriormente (geralmente localizado no caminho `/usr/local/bin/python3`).

### **Testando o ambiente**

Para garantir que a configuração está correta:

1. No PyCharm, crie um novo arquivo chamado `hello.py`.  
2. Insira o seguinte código: `print("Hello, Mac!")`.  
3. Clique com o botão direito no arquivo e selecione **Run 'hello'**; o resultado deve aparecer no console na parte inferior da tela.

### **Observações Importantes**

* **Command Line Tools:** O sistema pode solicitar a instalação das ferramentas de linha de comando do **Xcode**; se isso ocorrer, clique em “Instalar”.  
* **Apple Silicon (M1, M2):** Em Macs com chips da Apple, certifique-se de utilizar versões do Python compatíveis, podendo ser necessário o uso do **Rosetta** em alguns casos.  
* **Caminho do Python:** Se não localizar o Python automaticamente, verifique manualmente os caminhos `/usr/local/bin/python3` ou `/opt/homebrew/bin/python3`.

