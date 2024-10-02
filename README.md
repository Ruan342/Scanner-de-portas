
# **NETWORK SCANNER COM INTERFACE GRÁFICA**

Este é um projeto simples de varredura de rede desenvolvido em **Python**, utilizando o **Nmap** para realizar a varredura de portas e o **Tkinter** para criar uma interface gráfica amigável ao usuário.

## **FUNCIONALIDADES**

- Varredura de rede baseada em IP ou intervalo de IPs fornecido pelo usuário.
- Varredura de portas específicas ou intervalos de portas.
- Exibição dos resultados diretamente na interface gráfica.

## **REQUISITOS**

Antes de executar o projeto, certifique-se de que você tem os seguintes requisitos instalados:

1. **Python 3.x** - [Baixar Python](https://www.python.org/downloads/)
2. **Nmap** - [Baixar Nmap](https://nmap.org/download.html)
3. **Bibliotecas Python**:
   - `python-nmap`
   - `tkinter`

### **INSTALANDO DEPENDÊNCIAS**

Execute o seguinte comando para instalar a biblioteca `python-nmap`:

```bash
pip install python-nmap
```

Para instalar o Tkinter, dependendo do seu sistema operacional:

- **Windows**: Tkinter já está incluído na instalação padrão do Python.
- **Linux**: Execute o seguinte comando:
  ```bash
  sudo apt-get install python3-tk
  ```
- **Mac**: Tkinter está incluído na instalação padrão do Python no macOS.

**4. Digite o intervalo de IPs e portas na interface gráfica e clique no botão "Iniciar Varredura" para ver os resultados.**


## **EXEMPLO DE USO**

- Você pode inserir um intervalo de IPs como `192.168.1.0/24`.
- Pode inserir uma porta específica como `22` ou um intervalo de portas como `20-80`.
- O resultado da varredura será exibido diretamente na interface gráfica, com informações sobre o host e as portas abertas.
