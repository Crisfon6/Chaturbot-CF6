# import eel
# import random
# from datetime import datetime
# import pandas as pd
# import wx

# eel.init('web')
# errors = []


# @eel.expose
# def read_csv(wildcard="*",id):
#     app = wx.App(None)
#     style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
#     dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
#     if dialog.ShowModal() == wx.ID_OK:
#         path = dialog.GetPath()
#     else:
#         path = None
#     resp = ''
#     path.split('/')
#     print('/')
#     try:
#         df = pd.read_csv(path)

#         df.columns
#         resp = {
#             "msg": "Cargado Correctamente",
#             "type": "ok"}

#     except:
#         resp = {
#             "msg": "Archivo no aceptado por favor revise que el archivo cumpla con las condiciones",
#             "type": "error"}
#     dialog.Destroy()
#     errors.append(resp)
#     return resp


# @eel.expose
# def run(timeawait, amountproxies):
#     print(timeawait)
#     print(amountproxies)
#     return errors


# eel.start('index.html', size=(600, 600))
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import time
import pandas as pd



class App:
    def __init__(self):
        self.ws = Tk()
        self.ws.title('ChaturbotCF6')
        self.ws.geometry('400x300') 
        self.proxies_path = ''
        self.models_path = ''
        self.accounts_path =''
        self.proxiesByBrowser = ''
        self.timeawait =''
        self.timeawaitval = ''
        self.opcion =''
        self.draw()

    def open_file(self,f):
        # file_path = askopenfile(mode='r', filetypes=[('CSV files', '*csv')])       
        
        if(f=='proxies'):
            self.proxies_path = askopenfile(mode='r', filetypes=[('CSV files', '*csv')]) 
            if self.proxies_path is not None:
                pass 
        elif(f=='models'):
            self.models_path = askopenfile(mode='r', filetypes=[('CSV files', '*csv')])  
                
            if self.models_path is not None:
                pass            
        elif(f=='accounts'):
            self.accounts_path = askopenfile(mode='r', filetypes=[('CSV files', '*csv')]) 
                
            if self.accounts_path is not None:
                pass


    def uploadFiles(self):
        pb1 = Progressbar(
            self.ws, 
            orient=HORIZONTAL, 
            length=300, 
            mode='determinate'
            )
        pb1.grid(row=7, columnspan=3, pady=20)
        self.run()
        for i in range(5):
            self.ws.update_idletasks()
            pb1['value'] += 20
            time.sleep(1)
        pb1.destroy()
        Label(self.ws, text='File Uploaded Successfully!', foreground='green').grid(row=7, columnspan=3, pady=10)
            
        
    def draw(self):
        adhar = Label(
            self.ws, 
            text='Upload proxies'
            )
        adhar.grid(row=0, column=0, padx=10)

        adharbtn = Button(
            self.ws, 
            text ='Choose File', 
            command = lambda:self.open_file('proxies')
            ) 
        adharbtn.grid(row=0, column=1)

        dl = Label(
            self.ws, 
            text='Upload models'
            )
        dl.grid(row=1, column=0, padx=10)

        dlbtn = Button(
            self.ws, 
            text ='Choose File ', 
            command = lambda:self.open_file('models')
            ) 
        dlbtn.grid(row=1, column=1)

        ms = Label(
            self.ws, 
            text='Upload accounts'
            )
        ms.grid(row=2, column=0, padx=10)

        msbtn = Button(
            self.ws, 
            text ='Choose File', 
            command = lambda:self.open_file('accounts')
            ) 

        msbtn.grid(row=2, column=1)
        self.opcion = IntVar()

        Radiobutton(self.ws, text="Usar 1 proxy por navegador", variable=self.opcion, 
                    value=1, command=self.seleccionar).grid(row=3, column=1)
        Radiobutton(self.ws, text="Usar 1 proxy por 4 navegadores", variable=self.opcion, 
                    value=4, command=self.seleccionar).grid(row=4, column=1)

        Label(self.ws, text='Segundos de esperar por navegador', foreground='black').grid(row=5, column=0, pady=10)
        
        self.timeawait = Entry(self.ws)
        self.timeawait.grid(row=5,column=1)
        

        upld = Button(
            self.ws, 
            text='Upload Files', 
            command=self.uploadFiles
            )
        upld.grid(row=6, columnspan=3, pady=10)
        self.ws.mainloop()               
        


    def seleccionar(self):        
        self.proxiesByBrowser = self.opcion.get()
    def run(self):
        
        self.timeawaitval = self.timeawait.get()
        
        print(self.timeawaitval,self.proxiesByBrowser,self.proxies_path,self.models_path,     
            self.accounts_path)
        


app = App()