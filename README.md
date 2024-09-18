# PyFileOrganizer

**PyFileOrganizer** é uma ferramenta em Python que te ajuda a organizar automaticamente os teus ficheiros numa pasta, com base nas suas extensões. Com uma interface gráfica simples, este projeto facilita a organização dos teus diretórios, movendo ficheiros para pastas como Imagens, PDFs, Tabelas, entre outras.

## Funcionalidades

- **Organização Automática**: Classifica e move ficheiros para pastas consoante as suas extensões.
- **Interface Gráfica**: Permite escolher a pasta a ser organizada através de uma janela pop-up.
- **Categorias Personalizáveis**: É fácil de ajustar para adicionar mais tipos de ficheiros e categorias.

## Pré-requisitos

Para usar o PyFileOrganizer, precisas de:

- **Python 3.6** ou superior
- **Biblioteca tkinter** (para a interface gráfica) – geralmente já vem com o Python.

## Instalação

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/Pelinho03/PyFileOrganizer.git
    ```

2. **Vê para o diretório do projeto:**

    ```bash
    cd PyFileOrganizer
    ```

3. **Roda o script principal:**

    ```bash
    python PyFileOrganizer.py
    ```

## Como Usar

1. **Roda o script principal**:

    Vai até ao diretório do projeto e corre o script:

    ```bash
    python PyFileOrganizer.py
    ```

2. **Escolhe a pasta**:

    Vai aparecer uma janela pop-up. Escolhe a pasta que queres organizar.

3. **Organização dos ficheiros**:

    O script vai mover os ficheiros para as pastas certas, consoante as suas extensões. As pastas serão criadas automaticamente, se não existirem.


## Exemplo de Organização

### Antes:
```bash
|-- pasta
    |-- imagem1.jpg
    |-- documento.pdf
    |-- video.mp4
```

### Depois de Executar:
```bash
|-- pasta
    |-- Imagens
        |-- imagem1.jpg
    |-- PDFs
        |-- documento.pdf
    |-- Vídeos
        |-- video.mp4
```

## Contribuições

As contribuições são bem-vindas! Se tiveres ideias de melhorias ou novas funcionalidades, faz um fork do projeto e envia um pull request.

---
