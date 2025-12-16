from tkinter import Frame, Entry, Label, Button, scrolledtext, Tk, END

#import typing

#root = typing.NewType('root', None)
from view.tkinter_root import root

class read_directory_gui(Frame):
     def __init__(self, parent, context:root):
        super().__init__(parent)

        #context.screens["directory_gui"] = self
        # Etiqueta y entrada para archivo de directorio
        Label(self, text="Directorio:", bg="skyblue").grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        entry_file_dir = Entry(self, width=20)
        entry_file_dir.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        btn_carpeta = Button(self, text="Seleccionar", command= lambda : context.postman_.seleccionar_file(entry_file_dir))
        btn_carpeta.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

        # Etiqueta y entrada para carpeta
        Label(self, text="Archivo:", bg="skyblue").grid(row=0, column=3, padx=5, pady=5, sticky="nsew")
        entry_carpeta = Entry(self, width=20)
        entry_carpeta.grid(row=0, column=4, padx=5, pady=5, sticky="nsew")
        btn_carpeta = Button(self, text="Seleccionar", command= lambda: context.postman_.seleccionar_directorio(entry_carpeta))
        btn_carpeta.grid(row=0, column=5, padx=5, pady=5, sticky="nsew")

        # Botón de buscar
        btn_buscar = Button(self, text="Leer Directorio", command=lambda : context.postman_.leer_directorio(entry_file_dir,directory_text))
        btn_buscar.grid(row=1, column=3, pady=10, sticky="nsew")

        Label(self, text="Mensaje:", bg="skyblue").grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        entry_msg = Entry(self, width=40)
        entry_msg.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        
        frame_directory = Frame(self, bg="lightgray", height=50)
        frame_directory.grid(row=2, column=0, columnspan=7)
        #frame_directory.pack(fill="both")
        
        Label(frame_directory, text= "Directorio").grid(row=0, column= 0, padx=5, pady=5)
        directory_text = scrolledtext.ScrolledText(frame_directory, width=60, height=30)
        directory_text.grid(row=1, column=0, padx=10, pady=10, sticky="nsew" )
        
        directory_text.insert(END, f"FORMATO DE DIRECTORIO\n")
        directory_text.insert(END, f"ID | NOMBRE | TELEFONO | EMAIL\n")
        directory_text.insert(END, f"XX | KBKNML | 12334556 | SDDS@\n")

        btn_send =  Button(self, text="Enviar", command= lambda : context.postman_.send())
        btn_send.grid(row = 3, column= 5, padx=10, pady= 10, sticky="nsew")

        for i in range(0, 8):
            self.columnconfigure(i, weight=1)

        #self.grid_configure()



if __name__ == "__main__":
    container = Frame(height="800", width="800")
    container.pack(fill="both", expand=True)
    container.pack_propagate(False)
    test = read_directory_gui(container, Tk)
    test.pack(fill="both", expand=False)
    container.mainloop()