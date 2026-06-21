import tkinter as tk
import telaDesenho as tc
import botoesfunc as btf

janela = tk.Tk()

janela.geometry("1200x800")
janela.title("Janela main")
janela.resizable(False,False) # proibe que a tela seja redimencionada, fica mais d boa trabalhar kk 

botoes = btf.botoes(janela)
meio = tc.telaDdesenho(janela,botoes) #  Chama o arquivo telaDesenho


janela.mainloop()