import os, sys

from PyQt5 import QtCore, QtWidgets
from PyQt5 import uic

uiPath = "D:\\Documents\\GitHub\\File2Server\\promoteTest.ui"

moduleFile = sys.modules[__name__].__file__
moduleDir = os.path.dirname(moduleFile)

from uploadtablewidget import *

# x = uploadtablewidget.UploadTableWidget()

form_class, base_class = uic.loadUiType(uiPath)



# Simple example that show a list of employees 
class ExampleDialog(form_class, base_class):
    def __init__(self, parent=None):
        super(ExampleDialog, self).__init__(parent)
        
        # Required by uic module. You need to call this before accessing any ui elements below.
        self.setupUi(self)

        self.tbl_fileList.setRowCount(5)
        self.tbl_fileList.setColumnCount(1)

        item = QtWidgets.QTableWidgetItem()
        item.setText("hahahah")
        self.tbl_fileList.setItem(0, 0, item)

        # self.tbl_fileList.shout()

        self.tbl_fileList.installEventFilter(self)

    def eventFilter(self, source, event):
        """Very useful func that intercept event from installed widget. Now vhvu dont have to create custom widget class just for overriding its event anymore.
            But u have to call installEventFilter on the widget first (check initUi func.)"""
        if source is self.tbl_fileList:
            #Move and Enter, pre-drop events which are required if u want to activate DropEvent.
            if event.type() == QtCore.QEvent.DragMove:
                event.accept()
                return True
            elif event.type() == QtCore.QEvent.DragEnter:
                event.accept()
                return True
            elif event.type() == QtCore.QEvent.Drop:
                self.filteredDropEvent(event)
                return True

        #if u expect Qt to handle event as it s normally do, u must return false.
        #True, if u have already handle event for Qt, and dont expect Qt to act anything.
        return False

    def filteredDropEvent(self, event):
        """Func that emulate tableWidget DropEvent."""
        #some kind of qt container, which was packed in the Event
        mime = event.mimeData()

        #if dropped data can be translated as path or url
        if mime.hasUrls():
            numRow = self.tbl_fileList.rowCount()

            #Note: old school loop style coz our counter i has to ignore files which do not end with .ma or .mov
            i = 0
            for url in mime.urls():
                fileName = str(url.toLocalFile())
                print(fileName)
                currRow = numRow+i

                self.tbl_fileList.insertRow(currRow)
                
                item = QtWidgets.QTableWidgetItem()
                item.setText(fileName)
                self.tbl_fileList.setItem(currRow, 0, item)
                self.tbl_fileList.resizeColumnToContents(0)

                i += 1

# Run the application
app = QtWidgets.QApplication(sys.argv)
MainWindow = ExampleDialog()
MainWindow.show()
sys.exit(app.exec_())
