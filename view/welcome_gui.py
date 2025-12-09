from tkinter import Tk, Radiobutton, Frame, Label, Entry, Button, scrolledtext
from view.tkinter_root import root

# class GUI_class(Frame):

#     def __init__(self, parent, context):
#         super().__init__(parent)


class welcome_gui(Frame):
    def __init__(self, parent, context:"root"):
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
    


if __name__== '__main__':
    container = Frame(height="800", width="800")
    container.pack(fill="both", expand=True)
    container.pack_propagate(False)
    
    test = welcome_gui(container, Tk)
    test.pack(fill="both", expand=False)
    container.mainloop()