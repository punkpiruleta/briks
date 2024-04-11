import os
from pytube import YouTube
from PyQt5 import QtWidgets, uic,QtCore

filename = ""  # Variável global para armazenar o nome do arquivo baixado
def baixar():
    global filename  # Usa a variável global filename
    # Obtém o texto da linha de edição
    url = janela.link.text()
    # Verifica se o campo de entrada está vazio
    if not url:
        return
    # Cria um objeto YouTube com o URL do vídeo
    yt = YouTube(url)
    # Baixa o vídeo com a melhor qualidade disponível
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    # Baixa o vídeo para o diretório atual
    global filename
    filename = video.download()
def abrir_pasta():
    global filename  # Usa a variável global filename

    # Verifica se filename está definido
    if filename:
        # Obtém o diretório onde o vídeo foi baixado
        diretorio = os.path.dirname(filename)

        # Abre o diretório no gerenciador de arquivos padrão do sistema
        os.startfile(diretorio)
app = QtWidgets.QApplication([])
janela = uic.loadUi("yutube.ui")
# Conectar a função baixar ao botão de baixar
janela.baixar.clicked.connect(baixar)
# Conectar a função abrir_pasta ao botão Arquivo
janela.arquivo.clicked.connect(abrir_pasta)
# Exibir a janela
janela.show()


app.exec_()

