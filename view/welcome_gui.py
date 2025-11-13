from tkinter import Tk, Radiobutton, Frame, Label, Entry, Button, scrolledtext

import sys
sys.path.append("../postman")

from postman import postman


class root(Tk):
    def __init__(self):
        super().__init__()
        self.title("root")
        self.geometry("1000x1000")

        # Contenedor de la pantallas
        container = Frame(self)
        container.pack(fill="both", expand=True)
        self.screens = {}
        
        self.postman_ = postman()

        self.screens["welcome"] = welcome_gui(container, self)
        self.screens["directory"] = read_directory_gui(container, self)

        for screen in self.screens.values():
            screen.grid(row=0, column=0, sticky="nsew")

        # Mostrar pantalla inicial
        self.show("welcome")

        

    def show(self, gui_index):
        screen:Frame = self.screens[gui_index]
        screen.tkraise()



# class GUI_class(Frame):

#     def __init__(self, parent, context):
#         super().__init__(parent)


class welcome_gui(Frame):
    def __init__(self, parent, context:root):
        super().__init__(parent)

        #context.screens["welcome"] = self

        Label(self, text="Bienvenido", bg="skyblue").grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        WA_ = Radiobutton(self, text= 'Whats app')
        WA_.grid(row=1, column=0, padx=5 , pady=5, sticky="nsew")
        WA_.grid_columnconfigure(0, weight=1)
        EMAIL =  Radiobutton(self, text='Email')
        EMAIL.grid(row=2, column=0, padx=5 , pady=5, sticky="nsew")
        EMAIL.grid_columnconfigure(0, weight=1)


        continuar =  Button(self, text='Continuar', command=lambda: context.show("directory") )
        continuar.grid(row=3, column=0, padx=5 , pady=5)
    

class read_directory_gui(Frame):
     def __init__(self, parent, context:root):
        super().__init__(parent)

        #context.screens["directory_gui"] = self
        # Etiqueta y entrada para archivo de directorio
        Label(self, text="Directorio:", bg="skyblue").grid(row=0, column=0, padx=1, pady=1, sticky="nsew")
        
        entry_file_dir = Entry(self, width=40)
        entry_file_dir.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        btn_carpeta = Button(self, text="Seleccionar", command= lambda : context.postman_.seleccionar_file(entry_file_dir))
        btn_carpeta.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

        # Etiqueta y entrada para carpeta
        Label(self, text="Archivo:", bg="skyblue").grid(row=0, column=3, padx=5, pady=5, sticky="nsew")
        entry_carpeta = Entry(self, width=40)
        entry_carpeta.grid(row=0, column=4, padx=5, pady=5, sticky="nsew")
        btn_carpeta = Button(self, text="Seleccionar", command= lambda: context.postman_.seleccionar_directorio(entry_carpeta))
        btn_carpeta.grid(row=0, column=5, padx=5, pady=5, sticky="nsew")

        # Botón de buscar
        btn_buscar = Button(self, text="Leer", command=lambda : context.postman_.leer_directorio(entry_file_dir,directory_text))
        btn_buscar.grid(row=2, column=6, pady=10, sticky="nsew")


        #frame_directory = Frame(self, bg="lightgray", height=50)
        #frame_directory.pack(expand=True)

        Label(self, text= "Directorio").grid(row=0, column= 7, padx=5, pady=5, sticky="nsew")
        directory_text = scrolledtext.ScrolledText(self, width=100, height=40)
        directory_text.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        btn_send =  Button(self, text="Enviar", command= lambda : context.postman_.send())
        btn_send.grid(row = 2, column= 8, padx=10, pady= 10, sticky="nsew")


if __name__== '__main__':

    root_ = root()
    root_.mainloop()