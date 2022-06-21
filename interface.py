from tkinter import * 

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
             # Buttons
        buttonBack2 = Button(windowMain, text = "Regresar", font = ("Cooper Black", 12), width= 8, height = 2, command=return_main_2)
        buttonBack2.place(x = 20, y = 220)

def printMenu():
    # Create windowHome Home
    global windowHome
    windowHome = Tk()  
    windowHome.title("Trabajo Final de Complejidad Algorítmica")
    windowHome.geometry("600x300")
    windowHome.configure(bg = "#31C6F7")

    # Labels
    labelName = Label(windowHome, text = "Recreación de Waze - Grupo 3", bg = "#31C6F7", font = ("Cooper Black", 19), fg = "white")
    labelName.config(width = 500) 
    labelName.pack()
    # Buttons
    buttonStartProject = Button(windowHome, text = "Empezar", font = ("Cooper Black", 12), width= 20, height = 2, command = openMainApp)
    buttonCredits = Button(windowHome, text = "Créditos", font = ("Cooper Black", 12), width= 20, height = 2, command = openCredits)
    buttonExit = Button(windowHome, text = "Salir", font = ("Cooper Black", 12), width= 20, height = 2, command = windowHome.destroy)
    # # Add buttons to the windowHome
    buttonStartProject.pack(pady = 15 )
    buttonCredits.pack(pady = 15)
    buttonExit.pack(pady = 15)
    # Execute the windowHome
    windowHome.mainloop()  # call mainloop only for main

opened = False 
printMenu()