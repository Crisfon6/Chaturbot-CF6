from tkinter import *

from tkinter.ttk import *

from tkinter.filedialog import askopenfile 
import time
import pandas as pd

from ..Setup.Setup import Setup


class Gui:

    def __init__(self):

        self.ws = Tk()

        self.ws.title('ChaturbotCF6')

        self.ws.geometry('400x300') 

        self.proxies_path = ''

        self.models_path = ''

        self.accounts_path =''
        self.oneproxybybrowser = ''
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

                    value=False, command=self.seleccionar).grid(row=3, column=0)

        Radiobutton(self.ws, text="Usar 1 proxy por 4 navegadores", variable=self.opcion, 

                    value=True, command=self.seleccionar).grid(row=4, column=0)


        Label(self.ws, text='Segundos de esperar por navegador', foreground='black').grid(row=5, column=0, pady=10)
        

        self.timeawait = Entry(self.ws)

        self.timeawait.grid(row=5,column=1)
        


        upld = Button(
            self.ws, 

            text='Start', 

            command=self.uploadFiles
            )

        upld.grid(row=6, columnspan=3, pady=10)
        self.ws.mainloop()               
        



    def seleccionar(self):        
        self.oneproxybybrowser = self.opcion.get()
    def run(self):        
        self.timeawaitval = self.timeawait.get()
        Setup(self.proxies_path,self.models_path,self.accounts_path,self.timeawaitval,self.oneproxybybrowser).run()
        
        

        
        




