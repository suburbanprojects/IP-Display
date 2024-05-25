from tkinter import *
from tkinter import ttk
import socket, urllib.request

class TabbedDemo():
    def __init__(self,app):
        self.root = app
        self.display_tabs()

    def display_tabs(self):
        self.tabsystem = ttk.Notebook(app)
        self.tab1 = Frame(self.tabsystem)
        self.tab2 = Frame(self.tabsystem)

        self.tabsystem.add(self.tab1, text="IP Display")
        self.tabsystem.add(self.tab2, text="Host IP Display")
        self.tabsystem.pack(expand=1, fill="both")
        
        #Put the entries for the 1st tab here 
        self.homeIP= ttk.Label(self.tab1, text="Local IP:")
        self.homeIP.grid(column=0, row=1, padx=5, pady=5)
        self.ExtIP= ttk.Label(self.tab1, text="External IP:")
        self.ExtIP.grid(column=0, row=2, padx=5, pady=5)

        self.EntryHomeIP = ttk.Entry(self.tab1, width=25)
        self.EntryHomeIP.grid(column = 1, row=1, ipadx=5, pady=5)
        self.EntryExtIP = ttk.Entry(self.tab1, width=25)
        self.EntryExtIP.grid(column = 1, row=2, ipadx=5, pady=5)

        self.resultButton = ttk.Button(self.tab1, text='Show IP', command=self.showIP)
        self.resultButton.grid(column=0, row=4)

        #Put the entries for the 2nd tab here 
        self.EnterLabel = ttk.Label(self.tab2, text="Enter Address: ")
        self.EnterLabel.grid(column = 0, row = 0, ipadx=5, pady=5)
        self.ResultLabel = ttk.Label(self.tab2, text="IP Address: ")
        self.ResultLabel.grid(column = 0, row = 1, ipadx=5, pady=5)

        self.EntryAddress = ttk.Entry(self.tab2, width=25)
        self.EntryAddress.grid(column = 1, row=0, ipadx=5, pady=5)
        self.EntryHostIP = ttk.Entry(self.tab2, width=25)
        self.EntryHostIP.grid(column = 1, row=1, ipadx=5, pady=5)

        self.resultButton = ttk.Button(self.tab2, text='Show IP', command=self.getIP)
        self.resultButton.grid(column=0, row=4)

    #function for the 1st tab goes here
    def showIP(self):
        #get internal IP
        internalsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        internalsock.connect(("8.8.8.8", 80))
        internal_IP = internalsock.getsockname()
        self.EntryHomeIP.delete(0, "end")
        self.EntryHomeIP.insert(0, internal_IP)

        #get external IP 
        public_ip = urllib.request.urlopen('https://checkip.amazonaws.com').read().decode('utf8')
        self.EntryExtIP.delete(0, "end")
        self.EntryExtIP.insert(0, public_ip)

    #function for the 2nd tab goes here
    def getIP(self):
        self.hostAddress  = self.EntryAddress.get()
        ipaddr = socket.gethostbyname(self.hostAddress)
        self.EntryHostIP.delete(0, "end")
        self.EntryHostIP.insert(0, ipaddr)

if __name__=="__main__":
    app = Tk()
    app.title("IP Display Tool")
    app.geometry("275x125")
    app.resizable(width=False, height=False)
    app2 = TabbedDemo(app)
    app.mainloop()
