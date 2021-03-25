from PyQt5 import QtWidgets

class UploadTableWidget(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super(UploadTableWidget, self).__init__(parent)

        print("kreee")

    def cellDoubleClicked(self, row, column):
    	QtWidgets.QTableWidget.cellDoubleClicked(self, row, col)
    	print("hohoho")

    def shout(self):
    	print("browww")