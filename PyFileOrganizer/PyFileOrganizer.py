import os
from tkinter.filedialog import askdirectory

# Abre uma janela pop-up para o utilizador selecionar a pasta que deseja organizar
caminho = askdirectory(title='Seleciona uma pasta')

# Lista todos os arquivos na pasta selecionada
lista_arquivos = os.listdir(caminho)

# Dicionário que mapeia os tipos de arquivo às respetivas extensões
locais = {
    'imagens': ['.png', '.jpg', '.PNG', '.JPG'],  # Extensões de imagens
    'tabelas': ['.xlsx'],  # Extensões de ficheiros Excel
    'pdfs': ['.pdf', '.PDF'],  # Extensões de ficheiros PDF
    'csv': ['.csv'],  # Extensão de ficheiros CSV
    'word': ['.docx']  # Extensão de ficheiros Word
}

# Para cada arquivo na pasta
for arquivo in lista_arquivos:
    # Separa o nome do arquivo da sua extensão
    nome, extensao = os.path.splitext(f'{caminho}/{arquivo}')

    # Verifica se a extensão do arquivo corresponde a uma das categorias no dicionário
    for pasta in locais:
        if extensao in locais[pasta]:
            # Se a pasta correspondente não existir, cria-a
            if not os.path.exists(f'{caminho}/{pasta}'):
                os.mkdir(f'{caminho}/{pasta}')

            # Move o arquivo para a pasta correta
            os.rename(f'{caminho}/{arquivo}', f'{caminho}/{pasta}/{arquivo}')
