from os import path
import win32com.client

class Excel:
    def paste_excel(): 
        if path.exists(r'C:\Users\heitor.muller\OneDrive - Grupo Herval (1)\Itens Mercado x Global.xlsm'): 
            xl = win32com.client.Dispatch("Excel.Application")
            xl.Workbooks.Open(path.abspath(r'C:\Users\heitor.muller\OneDrive - Grupo Herval (1)\Itens Mercado x Global.xlsm'))
            xl.Visible = True
            try:
                xl.Application.Run("'Itens Mercado x Global.xlsm'!python")
            except:
                xl.Application.Quit()
            del xl

if __name__ == '__main__':
    Excel