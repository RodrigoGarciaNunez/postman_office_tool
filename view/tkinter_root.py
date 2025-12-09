from tkinter import Tk, Frame

#import sys
#sys.path.append('../model')

from model.postman import postman

class root(Tk):
    def __init__(self):
        super().__init__()
        self.title("root")
        self.geometry("800x600")

        # Contenedor de la pantallas
        self.container = Frame(self)
        self.container.pack(fill="both", expand=True)
        self.screens = {}
        
        self.postman_ = postman()

      


    def pack_frames(self):
        from view.welcome_gui import welcome_gui
        from view.read_directory_gui import read_directory_gui


        self.screens["welcome"] = welcome_gui(self.container, self)
        self.screens["directory"] = read_directory_gui(self.container, self)

        for screen in self.screens.values():
            screen.grid(row=0, column=0, sticky="nsew")

        # Mostrar pantalla inicial
        self.show("welcome")

    def show(self, gui_index):
        screen:Frame = self.screens[gui_index]
        screen.tkraise()




if __name__ == "__main__":
    root_ = root()
    root_.pack_frames()
    root_.mainloop()