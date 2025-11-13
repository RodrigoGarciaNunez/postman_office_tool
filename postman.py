from tkinter import Tk, filedialog,  messagebox
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
from directory_reader import directory_reader as dr
from sender import WA_sender, email_sender



class postman():

    def __init__(self):
        pass

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
        
        reader.leer_directorio(file_name)

        for destinatario in reader.direcoty.items():
            directory_text.insert(tk.END, f"{destinatario}\n")
        #fcf.file_check_method(root, finder_)

    def send(self):
        sender_ = WA_sender()
        sender_.send_Message(dict_)
        sender_ = email_sender()
        sender_.send_Message(dict_, "Prueba", "rodrigognunez8@gmail.com")


    # def directory_gui():
    #     top_frame = tk.Frame(root, bg="skyblue", height=50)
    #     top_frame.pack(fill="x")




    # # Etiqueta y entrada para archivo de directorio
    # tk.Label(top_frame, text="Directorio:", bg="skyblue").grid(row=0, column=0, padx=5, pady=5)
    
    # entry_file_dir = tk.Entry(top_frame, width=40)
    # entry_file_dir.grid(row=0, column=1, padx=5, pady=5)
    # btn_carpeta = tk.Button(top_frame, text="Seleccionar", command=seleccionar_file)
    # btn_carpeta.grid(row=0, column=2, padx=5, pady=5)

    # # Etiqueta y entrada para carpeta
    # tk.Label(top_frame, text="Archivo:", bg="skyblue").grid(row=0, column=3, padx=5, pady=5)
    # entry_carpeta = tk.Entry(top_frame, width=40)
    # entry_carpeta.grid(row=0, column=4, padx=5, pady=5)
    # btn_carpeta = tk.Button(top_frame, text="Seleccionar", command=seleccionar_directorio)
    # btn_carpeta.grid(row=0, column=5, padx=5, pady=5)

    # # Botón de buscar
    # btn_buscar = tk.Button(top_frame, text="Leer", command=leer_directorio)
    # btn_buscar.grid(row=2, column=1, pady=10)


    # frame_directory = tk.Frame(root, bg="lightgray", height=50)
    # frame_directory.pack(expand=True)

    # tk.Label(frame_directory, text= "Directorio").grid(row=0, column= 0, padx=5, pady=5)
    # directory_text = ScrolledText(frame_directory, width=100, height=40)
    # directory_text.grid(row=1, column=0, padx=10, pady=10)

    # btn_send = tk.Button(frame_directory, text="Enviar", command= send)
    # btn_send.grid(row = 2, column= 1, padx=10, pady= 10)

if __name__ == '__main__':

    dict_ = dict()
    reader = dr(dict_)
    root =  Tk()
    root.geometry("1000x600")
    root.title("Cartero")

   
    
    root.mainloop()