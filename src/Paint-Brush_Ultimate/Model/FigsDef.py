from Controller.figures import Figuras
from tkinter import filedialog
import json
import tkinter as tk
from tkinter import messagebox

class Retangulo(Figuras):
    def __init__(self, canvas):
        self.tela = canvas
        self.ini_x = self.ini_y = self.fim_x = self.fim_y = 0
        
    def marca_inicio(self, event):
        self.ini_x = event.x
        self.ini_y = event.y

    def draw(self, event, cor):
        self.fim_x = event.x
        self.fim_y = event.y
        self.tela.delete("preview")
        self.tela.create_rectangle(self.ini_x, self.ini_y, self.fim_x, self.fim_y, tags="preview", fill=cor)

class Oval(Figuras):
    def __init__(self, canvas):
        self.tela = canvas
        self.ini_x = self.ini_y = self.fim_x = self.fim_y = 0
        
    def marca_inicio(self, event):
        self.ini_x = event.x
        self.ini_y = event.y

    def draw(self, event, cor):
        self.fim_x = event.x
        self.fim_y = event.y
        self.tela.delete("preview")
        self.tela.create_oval(self.ini_x, self.ini_y, self.fim_x, self.fim_y, tags="preview", fill=cor)

class Linha(Figuras):
    def __init__(self, canvas):
        self.tela = canvas
        self.ini_x = self.ini_y = self.fim_x = self.fim_y = 0
        
    def marca_inicio(self, event):
        self.ini_x = event.x
        self.ini_y = event.y

    def draw(self, event, cor):
        self.fim_x = event.x
        self.fim_y = event.y
        self.tela.delete("preview") 
        self.tela.create_line(self.ini_x, self.ini_y, self.fim_x, self.fim_y, tags="preview", fill=cor)

class Poligono(Figuras):
    def __init__(self, canvas):
        self.tela = canvas
        self.ini_x = self.ini_y = self.fim_x = self.fim_y = 0
        
    def marca_inicio(self, event):
        self.ini_x = event.x
        self.ini_y = event.y

    def draw(self, event, cor):
        self.fim_x = event.x
        self.fim_y = event.y
        self.tela.delete("preview") 
        
        ponto3_x = self.ini_x - (self.fim_x - self.ini_x)
        
        self.tela.create_polygon(
            self.ini_x, self.ini_y, 
            self.fim_x, self.fim_y, 
            ponto3_x, self.fim_y, 
            tags="preview", fill=cor, outline="black"
        )


class Arco(Figuras):
    def __init__(self, canvas):
        self.tela = canvas
        self.ini_x = self.ini_y = self.fim_x = self.fim_y = 0

    def marca_inicio(self, event):
        self.ini_x = event.x
        self.ini_y = event.y

    def draw(self, event, cor):
        self.fim_x = event.x
        self.fim_y = event.y
        self.tela.delete("preview")
        self.tela.create_arc(self.ini_x, self.ini_y, self.fim_x, self.fim_y, fill=cor,tags="preview", style="arc")

class MaoLivre(Figuras):
    def __init__(self, canvas):
        self.tela = canvas
        self.ini_x = self.ini_y = 0
        

    def marca_inicio(self, event):
        self.ini_x = event.x
        self.ini_y = event.y

    def draw(self, event, cor):
    
        self.tela.create_line(self.ini_x, self.ini_y, event.x, event.y, capstyle="round", smooth=True, fill=cor,width=2)
        
        self.ini_x = event.x
        self.ini_y = event.y

def save_json():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".json",
        filetypes=[("JSON files", "*.json")],
        initialdir="src/salvo"
        )
    if file_path:
        try:
            infos = None
            dados = json.loads(infos)

            with open(file_path, 'w',encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, indent=4, ensure_ascii=False)

                messagebox.showinfo("Sucesso", "Arquivo JSON salvo com sucesso!")
        except json.JSONDecodeError:
            messagebox.showerror("Erro", "O texto inserido não está em um formato JSON válido.")
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível salvar o arquivo:\n{e}")

def open_json():
    file_path = filedialog.askopenfilename(
        filetypes=[("JSON files", "*.json")],
        initialdir="src/salvo"
        )
    
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)

                #entrada_texto.delete("1.0", tk.END)
                #entrada_texto.insert(tk.END, json.dumps(dados, indent=4))
                
                messagebox.showinfo("Sucesso", "Arquivo JSON carregado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível carregar o arquivo:\n{e}")