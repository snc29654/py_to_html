import sys
import tkinter
import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import tkinter as tk

import webbrowser
import os


#最初の画面のクラス
class py_to_html():  
    imgs = []
    def __init__(self):  
        self.root = Tk()  
        self.root.title("Image Viewer")  
        self.root.geometry("850x300") 
        self.cwd = os.getcwd()


        self.txt3 = tkinter.Entry(width=80)
        self.txt3.place(x=10, y=60)
        self.txt3.insert(tkinter.END,"ここに渡したいメッセージを入れる")



        button4 = tk.Button(self.root, text = 'web実行', command=self.webtest)
        button4.grid(row=0, column=1)  
        button4.place(x=770, y=40) 

        button5 = tk.Button(self.root, text = '終了', command=self.endall)
        button5.grid(row=0, column=1)  
        button5.place(x=770, y=250) 

        self.root.mainloop() 


    def quit(self):
        self.root.destroy()

    def endall(self):
        sys.exit()
               
    def webtest(self):
       
        print(self.cwd)
        web_site=self.cwd+"\\test.html"
        f = open(web_site, 'w')
        message=self.txt3.get()

        datalist = []


        datalist.append('<html>\n')
        datalist.append('<head>\n')
        datalist.append('<title>from python</title>\n')
        datalist.append('</head>\n')
        datalist.append('<body>\n')
        datalist.append(message)
        datalist.append('\n')
        datalist.append('</body>\n')
        datalist.append('</html>\n')

        f.writelines(datalist)

        f.close()
        webbrowser.open(web_site)

py_to_html()  

