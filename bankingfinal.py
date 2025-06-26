import sys
import math
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QLabel,QMainWindow,QVBoxLayout,QLineEdit

class mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        vbox=QVBoxLayout()
        self.welcomelabel=QLabel("Welcome to the Bank of Tamil Nadu",self)
        self.instructionlabel=QLabel("Choose The Action To Be Performed:",self)
        self.checkbutton=QPushButton("Show Balance",self)
        self.depositbutton=QPushButton("Deposit",self)
        self.withdrawbutton=QPushButton("Withdraw",self)
        self.exitbutton=QPushButton("Exit",self)
        self.checkbutton.clicked.connect(self.openbalancewindow)
        self.depositbutton.clicked.connect(self.opendepositwindow)
        self.withdrawbutton.clicked.connect(self.openwithdrawwindow)
        self.exitbutton.clicked.connect(self.openexitwindow)
        self.initUI()

    def openbalancewindow(self):
        self.balancewindow=balancewindow()
        self.balancewindow.show()
    def opendepositwindow(self):
        self.depositwindow=depositwindow()
        self.depositwindow.show()
    def openwithdrawwindow(self):
        self.withdrawwindow=withdrawwindow()
        self.withdrawwindow.show()
    def openexitwindow(self):
        self.exitwindow=exitwindow()
        self.exitwindow.show()
    def initUI(self):

        vbox=QVBoxLayout()
        vbox.addWidget(self.welcomelabel)
        vbox.addWidget(self.instructionlabel)
        vbox.addWidget(self.checkbutton)
        vbox.addWidget(self.depositbutton)
        vbox.addWidget(self.withdrawbutton)
        vbox.addWidget(self.exitbutton)
        self.setLayout(vbox)

class balancewindow(QWidget):
    def __init__(self):
        super().__init__()
        vbox=QVBoxLayout()
        self.welcomelabel=QLabel("Welcome to the Bank of Tamil Nadu",self)
        self.instructionlabel=QLabel("your total balance is:",self)
        self.Qline=QLineEdit(self)
        self.enterbutton=QPushButton("Enter",self)
        self.exitbutton=QPushButton("Exit",self)
        self.initUI()
    def initUI(self):

        vbox=QVBoxLayout()
        vbox.addWidget(self.welcomelabel)
        vbox.addWidget(self.instructionlabel)
        vbox.addWidget(self.Qline)
        vbox.addWidget(self.exitbutton)
        vbox.addWidget(self.enterbutton)
        self.setLayout(vbox)
        
class depositwindow(QWidget):
    def __init__(self):
        super().__init__()
        vbox=QVBoxLayout()
        self.welcomelabel=QLabel("Welcome to the Bank of Tamil Nadu",self)
        self.instructionlabel=QLabel("Enter The Amout you want to deposit:",self)
        self.depamount=QLineEdit(self)
        self.exitbutton=QPushButton("Exit",self)
        self.initUI()
    def initUI(self):

        vbox=QVBoxLayout()
        vbox.addWidget(self.welcomelabel)
        vbox.addWidget(self.instructionlabel)
        vbox.addWidget(self.exitbutton)
        deposit=self.depamount.text().strip()
        self.setLayout(vbox)
class withdrawwindow(QWidget):
    def __init__(self):
        super().__init__()
        vbox=QVBoxLayout()
        self.welcomelabel=QLabel("Welcome to the Bank of Tamil Nadu",self)
        self.instructionlabel=QLabel("your total balance is:",self)
        self.depamount=QLineEdit(self)
        self.exitbutton=QPushButton("Exit",self)
        self.initUI()
    def initUI(self):

        vbox=QVBoxLayout()
        vbox.addWidget(self.welcomelabel)
        vbox.addWidget(self.instructionlabel)
        vbox.addWidget(self.exitbutton)
        deposit=self.depamount.text().strip()
        self.setLayout(vbox)

class exitwindow(QWidget):
    def __init__(self):
        super().__init__()
        vbox=QVBoxLayout()
        self.welcomelabel=QLabel("Welcome to the Bank of Tamil Nadu",self)
        self.instructionlabel=QLabel("your total balance is:",self)
        self.Qline=QLineEdit("f{balance}")
        self.exitbutton=QPushButton("Exit",self)
        self.initUI()
    def initUI(self):

        vbox=QVBoxLayout()
        vbox.addWidget(self.welcomelabel)
        vbox.addWidget(self.instructionlabel)
        vbox.addWidget(self.exitbutton)
        self.setLayout(vbox)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    banking=mainwindow()
    banking.show()
    sys.exit(app.exec_())