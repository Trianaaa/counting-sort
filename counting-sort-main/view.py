from cProfile import label
import tkinter as tk
from tkinter import Toplevel, font
from setuptools import Command
import subprocess as sb
from tkinter.constants import *
from PIL import Image, ImageSequence, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import index
import time

#archivo para que funcione la evaluacion de gramaticas segun la TAS
cmd='python index.py'
def evaluate():
    p=sb.call(cmd,shell=True)

#Crea la ventana principal
mainWindow=tk.Tk()
mainWindow.iconbitmap('icon.ico')
mainFrame=tk.Frame(mainWindow,bg="lightsteelblue2")
frameTitle=tk.Frame(mainWindow, bg="lightsteelblue3")

imagen = tk.PhotoImage(file="hola.png")


#Crea la ventana Generalidades
def ventanaGen():
    ventanaGene = Toplevel()
    ventanaGene.iconbitmap('icon.ico')
    ventanaGene.title("Generalidades")
    ventanaGene.geometry("800x750")
    ventanaGene.resizable(False,False)
    ventanaGene.config(bg="lightsteelblue2")

    frameTitle=tk.Frame(ventanaGene, bg="lightsteelblue3")
    frameTitle.place(x=0.1,relwidth=1)

    title=tk.Label(frameTitle, text="Generalidades", bg="lightsteelblue3", fg="white", font=('Consolas',35))
    title.pack(side=LEFT)

    text=tk.Label(ventanaGene, text="El Counting Sort es un algoritmo de ordenación que ordena los \nelementos de una matriz contando el número de ocurrencias\n de cada elemento único en la matriz. El conteo se almacena\n en una matriz auxiliar y la clasificación se realiza\n mapeando el conteo como un índice de la matriz auxiliar.", bg="lightsteelblue3", fg="white", font=('Consolas',16))
    text.place(x=20,y=100)

    text=tk.Label(ventanaGene, text="Caracteristicas", bg="lightsteelblue3", fg="white", font=('Consolas',20))
    text.place(x=20,y=250)

    text=tk.Label(ventanaGene, text="Se trata de un algoritmo estable cuya complejidad computacional\n es O(n+k), siendo n el número de elementos a ordenar y k el\n tamaño del vector auxiliar (máximo - mínimo).\nLa eficiencia del algoritmo es independiente de lo casi ordenado\n que estuviera anteriormente.\n Es decir no existe un mejor y peor caso, todos los casos se\n tratan iguales.\nEl algoritmo counting, no se ordena in situ, sino que requiere\n de una memoria adicional.", bg="lightsteelblue3", fg="white", font=('Consolas',16))
    text.place(x=20,y=300)

    btn4=tk.Button(ventanaGene, text="Volver", padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 10), command=ventanaGene.destroy)
    btn4.place(x=715,y=15)

    lbImagen = tk.Label(ventanaGene, image=imagen)
    lbImagen.place(x=250, y=550)

#Crea la ventana Funcionamiento
def ventanaFun():
    ventanaFunci = Toplevel()
    ventanaFunci.iconbitmap('icon.ico')
    ventanaFunci.title("Funcionamiento")
    ventanaFunci.geometry("700x550")
    ventanaFunci.resizable(False,False)
    ventanaFunci.config(bg="lightsteelblue2")

    def play_gif():
        global img
        img= Image.open('imagen.gif')

        lblimg=tk.Label(ventanaFunci)
        lblimg.place(x=20,y=100)

        for img in ImageSequence.Iterator(img):
            img=ImageTk.PhotoImage(img)
            lblimg.config(image=img)

            ventanaFunci.update()
            time.sleep(0.01)
        ventanaFunci.after(0,play_gif)

    frameTitle=tk.Frame(ventanaFunci, bg="lightsteelblue3")
    frameTitle.place(relheight=0.1,relwidth=1)

    title=tk.Label(frameTitle, text="Funcionamiento", bg="lightsteelblue3", fg="white", font=('Consolas',35))
    title.pack(side=LEFT)

    btn4=tk.Button(ventanaFunci, text="Volver", padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 10), command=ventanaFunci.destroy)
    btn4.place(x=615,y=15)

    btn4=tk.Button(ventanaFunci, text="Play", padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 10), command=play_gif)
    btn4.place(x=600,y=470)

#Crea la ventana demostracion
def ventanaDem():
    ventanaDemo = Toplevel()
    ventanaDemo.iconbitmap('icon.ico')
    ventanaDemo.title("Generalidades")
    ventanaDemo.geometry("740x500")
    ventanaDemo.resizable(False,False)
    ventanaDemo.config(bg="lightsteelblue2")

    frameTitle=tk.Frame(ventanaDemo, bg="lightsteelblue3")
    frameTitle.place(x=0.1,relwidth=1)

    title=tk.Label(frameTitle, text="Demostracion", bg="lightsteelblue3", fg="white", font=('Consolas',35))
    title.pack(side=LEFT)

    btn4=tk.Button(ventanaDemo, text="Volver", padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 10), command=ventanaDemo.destroy)
    btn4.place(x=650,y=15)

    initial_label = tk.Label(ventanaDemo,text="Enter the number of random numbers for the first iteration:", fg="white", bg="lightsteelblue3", font=('Consolas', 12))
    initial_label.place(x=20,y=100)

    initial = tk.Entry(ventanaDemo, fg="black", bg="lightsteelblue3", font=('Consolas', 10))
    initial.place(x=20,y=150)

    increase_label = tk.Label(ventanaDemo, text="Enter the number of random numbers that is incremented by between iterations:", fg="white", bg="lightsteelblue3", font=('Consolas', 12))
    increase_label.place(x=20,y=250)

    increase = tk.Entry(ventanaDemo, fg="black", bg="lightsteelblue3", font=('Consolas', 10))
    increase.place(x=20,y=300)

    iterations_label = tk.Label(ventanaDemo,text="Enter the number of iterations to perform:",fg="white", bg="lightsteelblue3", font=('Consolas', 12))
    iterations_label.place(x=20,y=400)

    iterations = tk.Entry(ventanaDemo, fg="black", bg="lightsteelblue3", font=('Consolas', 10))
    iterations.place(x=20,y=450)

    def ejecutar(initial,iterations,increase):
        # print('hola')
        arrays_unsorted= index.random_Array(initial,iterations,increase)
        index.sort_arrays_unsorted_show_table(arrays_unsorted)

    def ejecutar2(initial,iterations,increase):
        # print('hola')
        arrays_unsorted= index.random_Array(initial,iterations,increase)
        index.sort_arrays_unsorted_show_graphic(arrays_unsorted)

    ejecutar_btn = tk.Button(ventanaDemo, text='Mostrar tabla', padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 10), command=lambda: ejecutar(int(initial.get()),int(iterations.get()),int(increase.get())))
    ejecutar_btn.place(x=550,y=400)

    ejecutar_btn = tk.Button(ventanaDemo, text='Mostrar graficos',padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 10), command=lambda: ejecutar2(int(initial.get()),int(iterations.get()),int(increase.get())))
    ejecutar_btn.place(x=550,y=450)

#Funcion para la configuracion de la ventana Principal
def mainWindowConfig():
    mainWindow.title("CountingSort")
    mainWindow.geometry("200x300")
    mainWindow.resizable(False,False)

#Funcion donde se configura y se ubican los contenedores de los labels y botones
def loadFrames():
    mainFrame.place(relheight=1, relwidth=1)
    frameTitle.place(relheight=0.1,relwidth=1)

#Funcion para configurar los labels
def loadLbl():
    title=tk.Label(frameTitle, text="CountingSort", bg="lightsteelblue3", fg="white", font=('Consolas',16))
    title.pack(side=TOP)

    #Variables globales con el fin de acceder a ellas más abajo
    global grammarLblR
    global grammarEntry

#Funcion para crear y configurar los botones de la venta principal
def loadBtn():
    btn1=tk.Button(mainWindow, text="Generalidades", padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 10), command=ventanaGen)
    btn1.place(x=45,y=75)
    
def loadBtn1():
    btn2=tk.Button(mainWindow, text="Funcionamiento", padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 10), command= ventanaFun)
    btn2.place(x=40,y=150)

def loadBtn2():
    btn3=tk.Button(mainWindow, text="Demostracion", padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 10), command= ventanaDem)
    btn3.place(x=45,y=225)

mainWindowConfig()
loadFrames()
loadLbl()
loadBtn1()
loadBtn2()
loadBtn()

mainWindow.mainloop()