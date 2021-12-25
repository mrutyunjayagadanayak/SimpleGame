import sys
from PyQt5 import QtWidgets
import mainwindow
import random

# This is a simple Rock paper Scissor game

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.options = ['Rock', 'Paper', 'Scissor']
        self.userWinsCounter = 0
        self.computerWinsCounter = 0
        self.ui.userWins.setText(str(self.userWinsCounter))
        self.ui.computerWins.setText(str(self.computerWinsCounter))
        self.ui.computeSelection.setText("")
        self.ui.submitButton.clicked.connect(self.submitClicked)
        self.ui.actionQuit.triggered.connect(quit)
    
    def submitClicked(self):
        userInput = self.ui.userSelection.currentText().lower()
        randomNumber = random.randint(0,2)
        self.ui.computeSelection.setText(self.options[randomNumber])
        computerInput = self.options[randomNumber].lower()
        #0 : Rock, 1: paper, 2: Scissor
        
        if userInput == 'rock' and computerInput == 'scissor':
            self.userWinsCounter += 1
            self.ui.userWins.setText(str(self.userWinsCounter))
        elif userInput == 'scissor' and computerInput == 'paper':
            self.userWinsCounter += 1
            self.ui.userWins.setText(str(self.userWinsCounter))
        elif userInput == 'paper' and computerInput == 'rock':
            self.userWinsCounter += 1
            self.ui.userWins.setText(str(self.userWinsCounter))
        elif userInput == computerInput:
            pass
        else:
            self.computerWinsCounter += 1
            self.ui.computerWins.setText(str(self.computerWinsCounter))

app = QtWidgets.QApplication(sys.argv)

my_mainWindow = MainWindow()
my_mainWindow.show()

sys.exit(app.exec_())
