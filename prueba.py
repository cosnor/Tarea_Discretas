from tkinter import Widget
import customtkinter
import os
from PIL import Image
from nodo import Grafo
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy as np
import networkx as nx


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.secuencia = []
        self.nodos = 0
        self.title("image_example.py")
        self.geometry("1280x760")
        self.dibujar = False

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(5, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo_hakimi.png")), size=(100, 100))
        self.house_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "house.png")), size=(30, 30))
        self.node_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "marketing.png")), size=(30, 30))
        self.prompt_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "prompt.png")), size=(542, 139))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Hakimi Grapher", image=self.logo_image,compound="left", font=customtkinter.CTkFont(size=15, weight="bold", family="Arial"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Hakimi Havel", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.house_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Graph", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.node_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")


        
        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.prompt_image)
        self.home_frame_large_image_label.grid(row=0, column=3, padx=10, pady=10, )

        self.home_label = customtkinter.CTkLabel(self.home_frame, text="Número de vértices", font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"))
        self.home_label.grid(row=1, column=2, padx=20, pady=20)
        self.home_slider = customtkinter.CTkSlider(self.home_frame, from_=1, to=20, command=self.slider_event, number_of_steps=19)
        self.home_slider.grid(row=2, column=2, padx=20, pady=10)
        self.home_label2= customtkinter.CTkLabel(self.home_frame, text="10", font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"))
        self.home_label2.grid(row=3, column=2, padx=20, pady=10)
        
        self.home_combobox1 = customtkinter.CTkComboBox(self.home_frame, values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"], font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"), command=self.combo_event, variable = 0, width=90, state="readonly")
        self.home_combobox2 = customtkinter.CTkComboBox(self.home_frame, values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"], font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"), command=self.combo_event, variable = 1, width=90, state="readonly")
        self.home_combobox3 = customtkinter.CTkComboBox(self.home_frame, values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"], font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"), command=self.combo_event, variable = 2, width=90, state="readonly")
        self.home_combobox4 = customtkinter.CTkComboBox(self.home_frame, values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"], font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"), command=self.combo_event, variable = 3, width=90, state="readonly")
        self.home_combobox5 = customtkinter.CTkComboBox(self.home_frame, values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"], font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"), command=self.combo_event, variable = 4, width=90, state="readonly") 
        self.home_combobox6 = customtkinter.CTkComboBox(self.home_frame, values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"], font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"), command=self.combo_event, variable = 5, width=90, state="readonly")
        self.home_combobox7 = customtkinter.CTkComboBox(self.home_frame, values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"], font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"), command=self.combo_event, variable = 6, width=90 , state="readonly")
        self.home_combobox8 = customtkinter.CTkComboBox(self.home_frame, values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"], font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"), command=self.combo_event, variable = 7, width=90, state="readonly")
        self.home_combobox9 = customtkinter.CTkComboBox(self.home_frame, values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"], font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"), command=self.combo_event, variable = 8, width=90, state="readonly")
        self.home_combobox10 = customtkinter.CTkComboBox(self.home_frame, values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"], font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"), command=self.combo_event, variable=9, width=90, state="readonly")
        self.home_combobox11 = customtkinter.CTkComboBox(self.home_frame, values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"], font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"), command=self.combo_event, variable=10, width=90, state="disabled")
        self.home_combobox12 = customtkinter.CTkComboBox(self.home_frame, values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"], font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"), command=self.combo_event, variable=11, width=90, state="disabled")
        self.home_combobox13 = customtkinter.CTkComboBox(self.home_frame, values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"], font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"), command=self.combo_event, variable=12, width=90, state="disabled")
        self.home_combobox14 = customtkinter.CTkComboBox(self.home_frame, values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"], font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"), command=self.combo_event, variable=13, width=90, state="disabled")
        self.home_combobox15 = customtkinter.CTkComboBox(self.home_frame, values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"], font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"), command=self.combo_event, variable=14, width=90, state="disabled")
        self.home_combobox16 = customtkinter.CTkComboBox(self.home_frame, values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"], font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"), command=self.combo_event, variable=15, width=90, state="disabled")
        self.home_combobox17 = customtkinter.CTkComboBox(self.home_frame, values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"], font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"), command=self.combo_event, variable=16, width=90, state="disabled")
        self.home_combobox18 = customtkinter.CTkComboBox(self.home_frame, values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"], font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"), command=self.combo_event, variable=17, width=90, state="disabled")
        self.home_combobox19 = customtkinter.CTkComboBox(self.home_frame, values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"], font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"), command=self.combo_event, variable=18, width=90, state="disabled")
        self.home_combobox20 = customtkinter.CTkComboBox(self.home_frame, values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"], font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"), command=self.combo_event, variable=19, width=90, state="disabled")
        self.COMBOS = [self.home_combobox1, self.home_combobox2, self.home_combobox3, self.home_combobox4, self.home_combobox5, self.home_combobox6, self.home_combobox7, self.home_combobox8, self.home_combobox9, self.home_combobox10, self.home_combobox11, self.home_combobox12, self.home_combobox13, self.home_combobox14, self.home_combobox15, self.home_combobox16, self.home_combobox17, self.home_combobox18, self.home_combobox19, self.home_combobox20]
        self.home_combobox1.place(x=30, y=380)
        self.home_combobox2.place(x=30, y=410)
        self.home_combobox3.place(x=30, y=440)
        self.home_combobox4.place(x=30, y=470)
        self.home_combobox5.place(x=30, y=500)
        self.home_combobox6.place(x=30, y=530)
        self.home_combobox7.place(x=30, y=560)
        self.home_combobox8.place(x=30, y=590)
        self.home_combobox9.place(x=30, y=620)
        self.home_combobox10.place(x=30, y=650)
        
        self.home_combobox11.place(x=135, y=380)
        self.home_combobox12.place(x=135, y=410)
        self.home_combobox13.place(x=135, y=440)
        self.home_combobox14.place(x=135, y=470)
        self.home_combobox15.place(x=135, y=500)
        self.home_combobox16.place(x=135, y=530)
        self.home_combobox17.place(x=135, y=560)
        self.home_combobox18.place(x=135, y=590)
        self.home_combobox19.place(x=135, y=620)
        self.home_combobox20.place(x=135, y=650)
        
        self.home_secuencia_button = customtkinter.CTkButton(self.home_frame, text="Aplicar teorema", font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"), command=self.secuencia_event, fg_color="gray20", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"))
        self.home_secuencia_button.place(x=60, y=685)
        
        self.home_label3 = customtkinter.CTkLabel(self.home_frame, text="Grados de los vértices", font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"))
        self.home_label3.place(x=30, y=350)
        self.text_box = customtkinter.CTkTextbox(self.home_frame, width=300, height=1000, font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"))
        
        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        self.graph_button = customtkinter.CTkButton(self.second_frame, text="Grafo Simple", font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"), command=self.plot, fg_color="gray20", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"))
        self.graph_button.place(x=60, y=685)
        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
    
    def slider_event(self, value):
        self.home_label2.configure(text=value)
        self.nodos = int(value)
        for combo in self.COMBOS:
            if int(value) <= int(combo.cget("variable")):
                combo.configure(state="disabled")
            else:
                combo.configure(state="readonly")

    def combo_event(self, value):
        print("")
    
    def secuencia_event(self):
        self.dibujar = False
        self.secuencia = []
        simple = True
        self.home_label4 = customtkinter.CTkLabel(self.home_frame, text="", font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"))
        for combo in self.COMBOS:
            if combo.cget("state") == "readonly":
                if combo.get() == "":
                    combo.set("0")
                elif int(combo.get()) >= self.nodos:
                    simple = False
                self.secuencia.append(int(combo.get()))
        print(self.secuencia)
        if simple:
            self.dibujar = True
            self.text_box.delete("0.0", "end")
            print("Es simple")
            self.text_box.place(x=300, y=350)
            grafo = Grafo()
            grafo.teorema(self.secuencia)
            self.text_box.insert("end", "Grados de los vértices: ")
            for i in grafo.mostrar:
                self.text_box.insert("end", str(i) + "\n")
        else:
            self.dibujar = False
            self.home_label4 = customtkinter.CTkLabel(self.home_frame, text="El grafo no es simple", font=customtkinter.CTkFont(size=12, weight="bold", family="Arial"))
            self.home_label4.place(x=30, y=720)
    
    
        
    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")
        
    def plot(self): 
        # if self.dibujar:
        #     fig, ax = plt.subplots()
        #     ax.axis('off')  # Desactivar ejes coordenados
        #     canvas = FigureCanvasTkAgg(fig, master=self.second_frame)
        #     canvas.get_tk_widget().pack(side=tk.TOP, padx= 300, pady=200, expand=1)
        #     ax.clear()
        #     grados = self.secuencia
        #     grafo = nx.random_degree_sequence_graph(grados)
        #     nx.draw(grafo, with_labels=True, font_weight='bold')
        #     canvas.draw()
    # Crear una nueva figura y eje en cada llamada
        fig, ax = plt.subplots()
        ax.axis('off')  # Desactivar ejes coordenados
        canvas = FigureCanvasTkAgg(fig, master=self.second_frame)
        canvas.get_tk_widget().pack(side=tk.TOP, padx=300, pady=200, expand=1)
        
        grados = self.secuencia
        try:
            grafo = nx.random_degree_sequence_graph(grados)
            nx.draw(grafo, with_labels=True, font_weight='bold')
        except Exception as e:
            ax.clear()
            ax.text(0.5, 0.5, "No existe el grafo", ha='center', va='center', fontsize=12)
        
        canvas.draw()
    
        
                

if __name__ == "__main__":
    app = App()
    app.resizable(False, False)
    app.mainloop()