import tkinter as tk
import telaDesenho as tc

janela = tk.Tk()

janela.geometry("1200x800")
janela.title("Janela main")
janela.resizable(False,False) # proibe que a tela seja redimencionada, fica mais d boa trabalhar kk 

meio = tc.telaDdesenho(janela) #  Chama o arquivo telaDesenho

janela.mainloop()