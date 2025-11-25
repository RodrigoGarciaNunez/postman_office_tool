import openpyxl


class directory_reader:
    
    def __init__(self, direcoty):
        self.direcoty =  direcoty

    def leer_directorio(self, file):

       
        try:
            wb = openpyxl.load_workbook(file, read_only=True, data_only=True)
            
            # primero, corroborar el formato
            if len(wb.sheetnames) > 1:
                print("Formato de directorio no valido")
                return     
            
            for hoja in wb.sheetnames:
                ws = wb[hoja]
                for fila in ws.iter_rows(min_row= 1, min_col=2):
                    for celda in fila:
                        #print(f"{celda.value}{celda.coordinate}")
                        self.direcoty[ws.cell(celda.row, 1).value] = celda.value
            
            print(self.direcoty)

            
        except:
            print(f"[XLSX] No se pudo leer {file}")
            #self.output_text_2.insert(tk.END, f"[XLSX] No se pudo leer {ruta}")