from tkinter import Frame, Entry, Label, Button, scrolledtext, Tk

#import typing

#root = typing.NewType('root', None)
from tkinter_root import root

class read_directory_gui(Frame):
     def __init__(self, parent, context:root):
        super().__init__(parent)

        #context.screens["directory_gui"] = self
        # Etiqueta y entrada para archivo de directorio
        Label(self, text="Directorio:", bg="skyblue").grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
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



if __name__ == "__main__":
    container = Frame()
    container.pack(fill="both", expand=True)
    test = read_directory_gui(container, Tk)
    test.mainloop()