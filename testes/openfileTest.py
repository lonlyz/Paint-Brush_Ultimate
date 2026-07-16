from tkinter import filedialog
import tkinter as tk

def abrirArquivo_teste():
    caminho = filedialog.askopenfilename()

    print(caminho)

abrirArquivo_teste()

#Check