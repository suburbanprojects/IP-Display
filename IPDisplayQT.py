from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit, QGridLayout, 
                             QApplication, QPushButton)
import sys, socket, urllib.request

class IPDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('IP Display')
        self.setFixedSize(350, 125)
        #put labels here
        self.homeIP = QLabel('Local IP: ')
        self.ExternalIP = QLabel('External IP: ')
        #create line edits
        self.EntryHomeIP = QLineEdit()
        self.EntryExtIP = QLineEdit()
        #create button
        self.ShowIPButton = QPushButton('Show IP', self)
        self.ShowIPButton.clicked.connect(self.showIP)
        #create grid layout
        grid = QGridLayout()
        #grid for labels here
        grid.addWidget(self.homeIP, 0, 0)
        grid.addWidget(self.ExternalIP, 1, 0)
        #grid for line edit here
        grid.addWidget(self.EntryHomeIP, 0,1)
        grid.addWidget(self.EntryExtIP, 1,1)
        #grid to add button
        grid.addWidget(self.ShowIPButton, 2,1)
        self.setLayout(grid)
    
    #function for the IP display goes here
    def showIP(self):
        #get internal IP
        internalsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        internalsock.connect(("8.8.8.8", 80))
        internal_IP = internalsock.getsockname()
        self.EntryHomeIP.clear()
        self.EntryHomeIP.insert(str(internal_IP))
        #get external IP 
        public_ip = urllib.request.urlopen('https://checkip.amazonaws.com').read().decode('utf8')
        self.EntryExtIP.clear()
        self.EntryExtIP.insert(str(public_ip))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_gui = IPDisplay()
    main_gui.show()
    sys.exit(app.exec())