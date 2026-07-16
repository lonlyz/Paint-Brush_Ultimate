import json
import tkinter as tk
from tkinter import filedialog, messagebox

# --- Funções de Manipulação de Arquivos ---

def carregar_json():
    """Abre uma janela para selecionar e carregar um arquivo JSON."""
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo JSON",
        filetypes=(("Arquivos JSON", "*.json"), ("Todos os arquivos", "*.*"))
    )
    
    if caminho_arquivo:
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
                
                # Exemplo: atualiza a caixa de texto com os dados carregados
                entrada_texto.delete("1.0", tk.END)
                entrada_texto.insert(tk.END, json.dumps(dados, indent=4))
                
                messagebox.showinfo("Sucesso", "Arquivo JSON carregado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível carregar o arquivo:\n{e}")

def salvar_json():
    """Abre uma janela para escolher onde salvar os"Erro", f"Não foi possível carregar o arquivo:\n{e}" dados no formato JSON."""
    caminho_arquivo = filedialog.asksaveasfilename(
        title="Salvar arquivo JSON",
        defaultextension=".json",
        filetypes=(("Arquivos JSON", "*.json"), ("Todos os arquivos", "*.*"))
    )
    
    if caminho_arquivo:
        try:
            # Pega o conteúdo da caixa de texto e converte para dicionário Python
            texto_bruto = entrada_texto.get("1.0", tk.END).strip()
            dados = json.loads(texto_bruto)
            
            with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, indent=4, ensure_ascii=False)
                
                messagebox.showinfo("Sucesso", "Arquivo JSON salvo com sucesso!")
        except json.JSONDecodeError:
            messagebox.showerror("Erro", "O texto inserido não está em um formato JSON válido.")
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível salvar o arquivo:\n{e}")

# --- Configuração da Interface (Tkinter) ---

janela = tk.Tk()
janela.title("Editor JSON com Tkinter")
janela.geometry("400x350")

# Botões
botao_carregar = tk.Button(janela, text="Carregar JSON", command=carregar_json)
botao_carregar.pack(pady=10)

botao_salvar = tk.Button(janela, text="Salvar JSON", command=salvar_json)
botao_salvar.pack(pady=5)

# Área de Texto
rotulo_texto = tk.Label(janela, text="Conteúdo do JSON:")
rotulo_texto.pack(pady=5)

entrada_texto = tk.Text(janela, height=12, width=45)
entrada_texto.pack(pady=5)

# Iniciar a aplicação
janela.mainloop()
