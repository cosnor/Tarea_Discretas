import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy as np
import networkx as nx

def plot():
    ax.clear()
    grados = [3,3,3,3,2]
    grafo = nx.random_degree_sequence_graph(grados)
    nx.draw(grafo, with_labels=True, font_weight='bold')
    canvas.draw()
    

#Se inicializa tkinter

root = tk.Tk()
root.title("Havel-Hakimi")
root.geometry("1920x1000")
root.resizable(False, False)


fig, ax = plt.subplots()
ax.axis('off')  # Desactivar ejes coordenados


#Se crea la ventana principal
frame = tk.Frame(root)
label = tk.Label(text="Havel-Hakimi")
label.config(font=("Courier", 32))
label.pack()

canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack(side="bottom")

frame.pack()
tk.Button(frame, text="Grafo Simple", command=plot).pack(pady=10)


root.mainloop()