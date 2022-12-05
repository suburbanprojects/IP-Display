import socket
import urllib.request
import tkinter as tk

app =tk.Tk()
app.title("IP Display")

def showIP():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    localIP = s.getsockname()[0]
    
    EntryHomeIP.insert(tk.INSERT, localIP)
    EntryHomeIP.config(state='disabled')

    publicip= urllib.request.urlopen('http://myip.dnsomatic.com').read().decode('utf8')
    EntryExtIP.insert(tk.INSERT, publicip)
    EntryExtIP.config(state='disabled')

HomeIP = tk.Label(app, text="Local IP")
HomeIP.grid(column = 0, row=0, ipadx=5, pady=5, sticky=tk.W+tk.N)
ExtIP = tk.Label(app, text="External IP")
ExtIP.grid(column=0, row=1, ipadx=5, pady=5, sticky=tk.W+tk.S)

EntryHomeIP = tk.Entry(app, width=20)
EntryExtIP = tk.Entry(app, width=20)
EntryHomeIP.grid(column=1,row=0,padx=10,pady=5, sticky=tk.N)
EntryExtIP.grid(column=1,row=1,padx=10,pady=5, sticky=tk.S)

resultButton = tk.Button(app, text='Show IP', command=showIP)
resultButton.grid(column=0, row=4, pady=10, sticky=tk.W)
resultQuit = tk.Button(app, text='Quit', command=app.quit)
resultQuit.grid(column=1, row=4, pady=10, sticky=tk.W)

app.mainloop()
