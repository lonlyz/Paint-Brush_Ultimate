# Desenha apenas uma linha
# Ao desenhar outra, apaga a anterior
enter = input("Digite a forma que deseja desenhar:\n opções:\n- linha\n- retangulo\n- oval\n")

if enter == "linha":
    def atualiza_fim(event):
        global fim_x, fim_y
        fim_x = event.x
        fim_y = event.y
        canvas.delete("all")  # apaga a linha anterior
        canvas.create_line(ini_x, ini_y, fim_x, fim_y)  # desenha a nova linha
elif enter == "oval":
    def atualiza_fim(event):
        global fim_x, fim_y
        fim_x = event.x
        fim_y = event.y
        canvas.delete("all")  # apaga a linha anterior
        canvas.create_oval(ini_x, ini_y, fim_x, fim_y)  # desenha a nova linha
else:
    print("Opção inválida. Por favor, execute o programa novamente e escolha uma opção válida.")
    quit()
import tkinter as tk

def marca_inicio(event):
    global ini_x, ini_y
    ini_x = event.x
    ini_y = event.y




root = tk.Tk()
root.title("Paint Brush Ultimate")
texto = tk.Label(root, text="Bem Vindo ao Paint Brush Ultimate | clique e arraste para desenhar")
texto.pack()

canvas = tk.Canvas(root, bg='white', width=600, height=600)
canvas.pack()

ini_x = None  # coordenadas do ponto inicial da linha
ini_y = None
fim_x = None
fim_y = None
canvas.bind('<ButtonPress-1>', marca_inicio)
canvas.bind('<B1-Motion>', atualiza_fim)
#canvas.bind('<ButtonRelease-1>', reset)

root.mainloop()
