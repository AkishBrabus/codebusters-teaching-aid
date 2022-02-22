import string
import sys
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from collections import Counter

alphabetTable = dict(zip(range(1,27), string.ascii_uppercase))

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("code.ui", self)

        self.label = self.findChild(QtWidgets.QLabel, 'label')
        self.label_2 = self.findChild(QtWidgets.QLabel, 'label_2')
        self.label_3 = self.findChild(QtWidgets.QLabel, 'label_3')
        self.label_4 = self.findChild(QtWidgets.QLabel, 'label_4')
        self.label_5 = self.findChild(QtWidgets.QLabel, 'label_5')
        self.label_6 = self.findChild(QtWidgets.QLabel, 'label_6')
        self.label_7 = self.findChild(QtWidgets.QLabel, 'label_7')
        self.label_8 = self.findChild(QtWidgets.QLabel, 'label_8')
        self.label_9 = self.findChild(QtWidgets.QLabel, 'label_9')
        self.label_10 = self.findChild(QtWidgets.QLabel, 'label_10')
        self.label_11 = self.findChild(QtWidgets.QLabel, 'label_11')
        self.label_12 = self.findChild(QtWidgets.QLabel, 'label_12')
        self.label_13 = self.findChild(QtWidgets.QLabel, 'label_13')
        self.label_14 = self.findChild(QtWidgets.QLabel, 'label_14')
        self.label_15 = self.findChild(QtWidgets.QLabel, 'label_15')
        self.label_16 = self.findChild(QtWidgets.QLabel, 'label_16')
        self.label_17 = self.findChild(QtWidgets.QLabel, 'label_17')
        self.label_18 = self.findChild(QtWidgets.QLabel, 'label_18')
        self.label_19 = self.findChild(QtWidgets.QLabel, 'label_19')
        self.label_20 = self.findChild(QtWidgets.QLabel, 'label_20')
        self.label_21 = self.findChild(QtWidgets.QLabel, 'label_21')
        self.label_22 = self.findChild(QtWidgets.QLabel, 'label_22')
        self.label_23 = self.findChild(QtWidgets.QLabel, 'label_23')
        self.label_24 = self.findChild(QtWidgets.QLabel, 'label_24')
        self.label_25 = self.findChild(QtWidgets.QLabel, 'label_25')
        self.label_26 = self.findChild(QtWidgets.QLabel, 'label_26')
        self.freq = {1: self.label_2, 2: self.label_3, 3: self.label_4, 4: self.label_5, 5: self.label, 6: self.label_6, 7: self.label_7, 8: self.label_8, 9: self.label_9, 10: self.label_24, 11: self.label_14, 12: self.label_16, 13: self.label_10, 14: self.label_22, 15: self.label_20, 16: self.label_23, 17: self.label_12, 18: self.label_25, 19: self.label_19, 20: self.label_17, 21: self.label_26, 22: self.label_21, 23: self.label_18, 24: self.label_15, 25: self.label_13, 26: self.label_11}

        self.lineEdit = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.lineEdit_2 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_2')
        self.lineEdit_3 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_3')
        self.lineEdit_4 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_4')
        self.lineEdit_5 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_5')
        self.lineEdit_6 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_6')
        self.lineEdit_7 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_7')
        self.lineEdit_8 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_8')
        self.lineEdit_9 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_9')
        self.lineEdit_10 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_10')
        self.lineEdit_11 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_11')
        self.lineEdit_12 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_12')
        self.lineEdit_13 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_13')
        self.lineEdit_14 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_14')
        self.lineEdit_15 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_15')
        self.lineEdit_16 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_16')
        self.lineEdit_17 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_17')
        self.lineEdit_18 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_18')
        self.lineEdit_19 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_19')
        self.lineEdit_20 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_20')
        self.lineEdit_21 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_21')
        self.lineEdit_22 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_22')
        self.lineEdit_23 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_23')
        self.lineEdit_24 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_24')
        self.lineEdit_25 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_25')
        self.lineEdit_26 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_26')
        self.replace = {1: self.lineEdit, 2: self.lineEdit_2, 3: self.lineEdit_3, 4: self.lineEdit_4, 5: self.lineEdit_5, 6: self.lineEdit_6, 7: self.lineEdit_7, 8: self.lineEdit_8, 9: self.lineEdit_9, 10: self.lineEdit_11, 11: self.lineEdit_16, 12: self.lineEdit_12, 13: self.lineEdit_18, 14: self.lineEdit_20, 15: self.lineEdit_25, 16: self.lineEdit_17, 17: self.lineEdit_10, 18: self.lineEdit_23, 19: self.lineEdit_19, 20: self.lineEdit_21, 21: self.lineEdit_13, 22: self.lineEdit_14, 23: self.lineEdit_26, 24: self.lineEdit_24, 25: self.lineEdit_15, 26: self.lineEdit_22}

        self.updateButton = self.findChild(QtWidgets.QPushButton, 'updateButton')
        self.updateButton.clicked.connect(self.updateButtonClicked)

        self.pushCypherButton = self.findChild(QtWidgets.QPushButton, 'pushCypherButton')
        self.pushCypherButton.clicked.connect(self.pushCypherButtonClicked)

        self.pushCypherTextEdit = self.findChild(QtWidgets.QTextEdit, 'pushCypherTextEdit')

        self.cypherText = self.findChild(QtWidgets.QLabel, 'cypherLabel')

    def updateButtonClicked(self):
        text = self.cypherText.text()
        cypherText = text.partition('\n')[0]
        decypherText = re.sub('\w', '_', cypherText)

        decypherTable = {}
        for letter in self.replace.keys():
            if self.replace[letter].text() != '':
                decypherTable[alphabetTable[letter]] = self.replace[letter].text()

        for decypherKey in decypherTable.keys():
            decypherKeyPos = [pos for pos, char in enumerate(cypherText) if char == decypherKey]
            for position in decypherKeyPos:
                decypherText = decypherText[:position] + decypherTable[decypherKey].upper() + decypherText[position+1:]

        text = cypherText+'\n'+decypherText
        self.cypherText.setText(text)

    def pushCypherButtonClicked(self):
        # updates the cypher text in the actual cypher box
        cypherText = self.pushCypherTextEdit.toPlainText().upper()
        decypherText = re.sub('\w', '_', cypherText)
        self.cypherText.setText(cypherText+'\n'+decypherText)

        # clears the numbers in the frequency box and updates them
        counts = Counter(cypherText)
        for letter in self.freq.keys():
            self.freq[letter].setText('')
            if alphabetTable[letter] in counts.keys():
                num = counts[alphabetTable[letter]]
                if num != 0:
                    self.freq[letter].setText(str(num))



app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()