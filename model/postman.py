from tkinter import Tk, filedialog,  messagebox
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
from model.directory_reader import directory_reader as dr
from model.sender import WA_sender, email_sender



class postman():

    def __init__(self):
        self.reader = dr()
        self.directorio = dict()
        self.message = str()
        self.file = str()


    def seleccionar_file(self, entry_dir):
        file =  filedialog.askopenfilename()
        if file:
            entry_dir.delete(0, tk.END)
            entry_dir.insert(0, file)


    def seleccionar_directorio(self, entry_carpeta):
        directory = filedialog.askdirectory()
        if directory:
            entry_carpeta.delete(0, tk.END)
            entry_carpeta.insert(0, directory)


    def leer_directorio(self, entry_file, directory_text):
        
        file_name =  entry_file.get()
    
        if not file_name:
            messagebox.showwarning("Error", "Por favor ingresa carpeta y palabra.")
            return
        
        self.reader.leer_directorio(file_name)

        if len(self.reader.direcoty) > 1:
            directory_text.delete('1.0', tk.END)
            for destinatario in self.reader.direcoty.items():
                directory_text.insert(tk.END, f"{destinatario}\n")
            
            return

        messagebox.showwarning("Error", "DIRECTORIO NO VALIDO")
        #fcf.file_check_method(root, finder_)

    def send(self, message):
        sender_ = WA_sender(self.reader.direcoty,message,self.file)
        sender_.send_Message()
        #sender_ = email_sender()
        #sender_.send_Message(dict_, "Prueba", "")


if __name__ == '__main__':

    #dict_ = dict()
    reader = dr()
    root =  Tk()
    root.geometry("1000x600")
    root.title("Cartero")

   
    
    root.mainloop()