import json
from tkinter import filedialog
import os

class SaveAndLoad:  
    def __init__(self, canvasObj):
        # Objeto 
        self.canvasObj = canvasObj

    def obter_dados_atuais(self):
        """Coleta as listas de desenhos atuais diretamente das figuras do Canvas"""
        return {
            "DrawsRet": self.canvasObj.stateDict["retangulo"].arrayDraws,
            "DrawsOval": self.canvasObj.stateDict["circulo"].arrayDraws,
            "DrawsLinha": self.canvasObj.stateDict["linha"].arrayDraws,
            "DrawsMao": self.canvasObj.stateDict["maoLivre"].arrayDraws,
            "DrawsPoly": self.canvasObj.stateDict["poligono"].arrayDraws,
            "DrawsArco": self.canvasObj.stateDict["arco"].arrayDraws
        }

    def save(self):
        # Pede para o usuário escolher onde salvar e o nome do arquivo JSON
        caminho_arquivo = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("Arquivos JSON", "*.json")],
            title="Salvar Desenho"
        )

        if caminho_arquivo:
            dados = self.obter_dados_atuais()
            try:
                with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
                    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
                print(f"Desenho salvo com sucesso em: {caminho_arquivo}")
            except Exception as e:
                print(f"Erro ao salvar arquivo: {e}")

    def load(self):
        # Abre a caixa para selecionar o arquivo JSON salvo anteriormente
        caminho_arquivo = filedialog.askopenfilename(
            filetypes=[("Arquivos JSON", "*.json")],
            title="Abrir Desenho"
        )

        if caminho_arquivo:
            try:
                with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
                    dados = json.load(arquivo)
                
                # 1. Limpa o canvas visualmente para receber o novo desenho
                self.canvasObj.canvas.delete("all")

                # 2. Atualiza as listas internas de cada figura com os dados carregados
                self.canvasObj.stateDict["retangulo"].arrayDraws = dados.get("DrawsRet", [])
                self.canvasObj.stateDict["circulo"].arrayDraws = dados.get("DrawsOval", [])
                self.canvasObj.stateDict["linha"].arrayDraws = dados.get("DrawsLinha", [])
                self.canvasObj.stateDict["maoLivre"].arrayDraws = dados.get("DrawsMao", [])
                self.canvasObj.stateDict["poligono"].arrayDraws = dados.get("DrawsPoly", [])
                self.canvasObj.stateDict["arco"].arrayDraws = dados.get("DrawsArco", [])

                # 3. Redesenha tudo na tela com base nas coordenadas salvas
                self._redesenhar_tudo()
                print("Desenho carregado com sucesso!")

            except Exception as e:
                print(f"Erro ao carregar arquivo: {e}")

    def _redesenhar_tudo(self):
        """Varre os arrays internos e renderiza novamente cada figura no canvas do Tkinter"""
        cv = self.canvasObj.canvas

        # redesenhar Retângulos
        # formato: [ini_x, ini_y, fim_x, fim_y, cor]
        for r in self.canvasObj.stateDict["retangulo"].arrayDraws:
            cv.create_rectangle(r[0], r[1], r[2], r[3], fill=r[4])

        # redesenhar Ovais
        for o in self.canvasObj.stateDict["circulo"].arrayDraws:
            cv.create_oval(o[0], o[1], o[2], o[3], fill=o[4])

        # redesenhar Linhas
        for l in self.canvasObj.stateDict["linha"].arrayDraws:
            cv.create_line(l[0], l[1], l[2], l[3], fill=l[4])

        for p in self.canvasObj.stateDict["poligono"].arrayDraws:
           
            cv.create_polygon(p[0], p[1], p[2], p[3], p[4], p[5], fill=p[6], outline="black")

        # redesenhar Arcos
        for a in self.canvasObj.stateDict["arco"].arrayDraws:
            cv.create_arc(a[0], a[1], a[2], a[3], fill=a[4], style="arc")

        
        for caminho in self.canvasObj.stateDict["maoLivre"].arrayDraws:
            if len(caminho) > 1:
                for i in range(len(caminho) - 1):
                    ponto_atual = caminho[i]
                    proximo_ponto = caminho[i+1]
                   
                    cv.create_line(
                        ponto_atual[0], ponto_atual[1], 
                        proximo_ponto[0], proximo_ponto[1], 
                        capstyle="round", smooth=True, fill="black", width=2
                    )