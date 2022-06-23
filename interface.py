from tkinter import *
from matplotlib.pyplot import draw 
from graph import * 
from dijkstra import *
from helpers import *

# FUNCTIONS INTERFACE

def return_main(): 
    windowCredits.destroy()
    opened = False
    printMenu()

def return_main_2():
    windowMain.destroy()
    opened = False
    printMenu()

def openCredits():
    global opened, windowCredits
    windowHome.withdraw()  # withdraw main instead of destroying it
    if opened == True:
        windowCredits.deiconify()
    else:
        # Create new window
        windowCredits = Toplevel(windowHome) 
        windowCredits.configure(bg = "#31C6F7")
        windowCredits.title("Créditos del proyecto")
        windowCredits.geometry("600x300")
        # Labels
        labelTitle = Label(windowCredits, text = "Integrantes", bg = "#31C6F7", font = ("Cooper Black", 19), fg = "black").place(x = 20, y =  20)
        labelMemberOne =  Label(windowCredits, text = "Paolo Cisneros", bg = "#31C6F7", font = ("Cooper Black", 13), fg = "black").place(x = 20, y =  70)
        labelMemberTwo =  Label(windowCredits, text = "Enzo Livelli", bg = "#31C6F7", font = ("Cooper Black", 13), fg = "black").place(x = 20, y =  100)
        # Buttons
        buttonBack = Button(windowCredits, text = "Regresar", font = ("Cooper Black", 12), width= 8, height = 2, command=return_main)
        buttonBack.place(x = 20, y = 220)

def openMainApp():
    global opened, windowMain
    windowHome.withdraw()
    if opened == True:
        windowMain.deiconify()
    else:
        # Create new window
        windowMain = Toplevel(windowHome)
        windowMain.configure(bg = "#31C6F7")
        windowMain.title("Waze - Lima")
        windowMain.geometry("600x300")
        # Labels
        labelNumberNodes = Label(windowMain, text = "Numero de intersecciones que desea: ", font = ("Times New Roman", 12), bg = "#31C6F7").place(x = 10, y = 60)
        labelTitle = Label(windowMain, text = "Waze - Lima", bg = "#31C6F7", font = ("Times New Roman", 19, "bold")).place(x = 240, y = 10)
        labelShortestPath = Label(windowMain, text = "Ingrese el ID de origen de la interseccion: ",font = ("Times New Roman", 12), bg = "#31C6F7").place(x = 10, y = 140)
        # Inputs
        inputNumberNodes = Entry(windowMain, width = 25)
        inputNumberNodes.pack(padx = 270, pady =63)
        inputIdSource = Entry(windowMain, width = 11)
        inputIdSource.pack()

        # Functions
        def createWeightedGraph():
            number = inputNumberNodes.get()
            drawGraphOne(int(number))
        def creatGraphNormal():
            number = inputNumberNodes.get()
            drawGraphTwo(int(number))
        def getShortestPath():
            id = int(inputIdSource.get())
            calculateShortestRouteBetweenTwoNodes(id)
        # Buttons
        buttonBack2 = Button(windowMain, text = "Regresar", font = ("Times New Roman", 10), width= 7, height = 1, command=return_main_2)
        buttonBack2.place(x = 10, y = 270)
        buttonSendNumberNodes = Button(windowMain, text = "Crear grafo ponderado", font = ("Times New Roman", 10), width= 17, height = 1, command = createWeightedGraph)
        buttonSendNumberNodes.place(x = 340, y = 60)
        buttonSendNumberNodes2 = Button(windowMain, text = "Crear grafo", font = ("Times New Roman", 10), width= 9, height = 1, command = creatGraphNormal)
        buttonSendNumberNodes2.place(x = 490, y = 60)
        buttonCalculatePath = Button(windowMain, text = "Conseguir ruta", font = ("Times New Roman", 10), width= 13, height = 1, command = getShortestPath)
        buttonCalculatePath.place(x = 350, y = 140)
def printMenu():
    # Create windowHome Home
    global windowHome
    windowHome = Tk()  
    windowHome.title("Trabajo Final de Complejidad Algorítmica")
    windowHome.geometry("600x300")
    windowHome.configure(bg = "#31C6F7")
    # Labels
    labelName = Label(windowHome, text = "Recreación de Waze - Grupo 3", bg = "#31C6F7", font = ("Times New Roman", 19), fg = "white")
    labelName.config(width = 500) 
    labelName.pack()
    # Buttons
    buttonStartProject = Button(windowHome, text = "Empezar", font = ("Times New Roman", 12), width= 20, height = 2, command = openMainApp)
    buttonCredits = Button(windowHome, text = "Créditos", font = ("Times New Roman", 12), width= 20, height = 2, command = openCredits)
    buttonExit = Button(windowHome, text = "Salir", font = ("Times New Roman", 12), width= 20, height = 2, command = windowHome.destroy)
    # # Add buttons to the windowHome
    buttonStartProject.pack(pady = 15 )
    buttonCredits.pack(pady = 15)
    buttonExit.pack(pady = 15)
    # Execute the windowHome
    windowHome.mainloop()  # call mainloop only for main
opened = False 
printMenu()

