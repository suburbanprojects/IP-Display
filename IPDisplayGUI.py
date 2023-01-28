import socket
import urllib.request
import tkinter as tk
import pyperclip

app =tk.Tk()
app.title("IP Display")
app.geometry("350x125")

def showIP():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    localIP = s.getsockname()[0]
    EntryHomeIP.delete(0, "end")
    EntryHomeIP.insert(tk.INSERT, localIP)

    publicip= urllib.request.urlopen('https://v4.ident.me/').read().decode('utf8')
    EntryExtIP.delete(0, "end")
    EntryExtIP.insert(tk.INSERT, publicip)

def CopyPass1():
    pyperclip.copy(EntryHomeIP.get())

def CopyPass2():
    pyperclip.copy(EntryExtIP.get())

HomeIP = tk.Label(app, text="Local IP")
HomeIP.grid(column = 0, row=0, ipadx=5, pady=5, sticky=tk.W+tk.N)
ExtIP = tk.Label(app, text="External IP")
ExtIP.grid(column=0, row=1, ipadx=5, pady=5, sticky=tk.W+tk.S)

EntryHomeIP = tk.Entry(app, width=20)
EntryExtIP = tk.Entry(app, width=20)
EntryHomeIP.grid(column=1,row=0,padx=10,pady=5, sticky=tk.N)
EntryExtIP.grid(column=1,row=1,padx=10,pady=5, sticky=tk.S)

resultButton = tk.Button(app, text='Show IP', command=showIP)
resultButton.grid(column=0, row=4) 
resultCopy1 = tk.Button(app, text='Copy', command=CopyPass1)
resultCopy1.grid(column=3, row=0) 
resultCopy2= tk.Button(app, text='Copy', command=CopyPass2)
resultCopy2.grid(column=3, row=1) 
resultQuit = tk.Button(app, text='Quit', command=app.quit)
resultQuit.grid(column=3, row=4) 

app.mainloop()
