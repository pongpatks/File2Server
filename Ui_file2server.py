# -*- coding: utf-8 -*-

# Modified version of 'O:\studioTools\maya\python\tool\pipeline\file2server\ui.ui'
# We have to modify it. Coz we need to add Event Handler for tableWidget.
# 
# So, be mindful that this file doesnt sync with ui.ui then.
#
# Created: Wed Sep 21 14:00 2016
#      by: Kun

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):

	def initUi(self, MainWindow):
		#init mainWindow
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(1000, 514)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))


		#init child widgets
		#YOU MUST ASSIGN THIS ONE WITH YOUR CUSTOM WIDGET
		self.tbl_fileList = None

		self.groupBox = QtGui.QGroupBox(self.centralwidget)
		self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
		
		self.rdo_workFile = QtGui.QRadioButton(self.groupBox)
		self.rdo_heroFile = QtGui.QRadioButton(self.groupBox)
		
		self.rdo_defUser = QtGui.QRadioButton(self.groupBox_2)
		self.rdo_rplUser = QtGui.QRadioButton(self.groupBox_2)
		self.txt_rplUser = QtGui.QLineEdit(self.groupBox_2)
		
		self.chk_sendAll = QtGui.QCheckBox(self.centralwidget)
		self.btn_apply = QtGui.QPushButton(self.centralwidget)

		self.btn_reset = QtGui.QPushButton(self.centralwidget)
		self.btn_rename = QtGui.QPushButton(self.centralwidget)
		self.btn_sendToServer = QtGui.QPushButton(self.centralwidget)
		
	def setupUi(self, MainWindow):
		""""""
		self.gridLayout = QtGui.QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		self.verticalLayout_3 = QtGui.QVBoxLayout()
		self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))

		font = QtGui.QFont()
		font.setPointSize(8)
		self.tbl_fileList.setFont(font)
		self.tbl_fileList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
		self.tbl_fileList.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
		self.tbl_fileList.setTextElideMode(QtCore.Qt.ElideLeft)
		self.tbl_fileList.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
		self.tbl_fileList.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
		self.tbl_fileList.setShowGrid(True)
		self.tbl_fileList.setObjectName(_fromUtf8("tbl_fileList"))
		self.tbl_fileList.setColumnCount(4)
		self.tbl_fileList.setRowCount(0)
		item = QtGui.QTableWidgetItem()
		self.tbl_fileList.setHorizontalHeaderItem(0, item)
		item = QtGui.QTableWidgetItem()
		self.tbl_fileList.setHorizontalHeaderItem(1, item)
		item = QtGui.QTableWidgetItem()
		self.tbl_fileList.setHorizontalHeaderItem(2, item)
		item = QtGui.QTableWidgetItem()
		self.tbl_fileList.setHorizontalHeaderItem(3, item)
		self.verticalLayout_3.addWidget(self.tbl_fileList)
		self.horizontalLayout_4 = QtGui.QHBoxLayout()
		self.horizontalLayout_4.setContentsMargins(5, -1, 5, -1)
		self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))

		self.groupBox.setFlat(False)
		self.groupBox.setObjectName(_fromUtf8("groupBox"))
		self.gridLayout_4 = QtGui.QGridLayout(self.groupBox)
		self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))

		self.rdo_workFile.setChecked(True)
		self.rdo_workFile.setObjectName(_fromUtf8("rdo_workFile"))
		self.gridLayout_4.addWidget(self.rdo_workFile, 0, 0, 1, 1)

		self.rdo_heroFile.setObjectName(_fromUtf8("rdo_heroFile"))
		self.gridLayout_4.addWidget(self.rdo_heroFile, 0, 1, 1, 1)
		self.horizontalLayout_4.addWidget(self.groupBox)

		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
		self.groupBox_2.setSizePolicy(sizePolicy)
		self.groupBox_2.setFlat(False)
		self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
		self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
		self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))

		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.txt_rplUser.sizePolicy().hasHeightForWidth())
		self.txt_rplUser.setSizePolicy(sizePolicy)
		self.txt_rplUser.setMinimumSize(QtCore.QSize(120, 0))
		self.txt_rplUser.setObjectName(_fromUtf8("txt_rplUser"))
		self.gridLayout_3.addWidget(self.txt_rplUser, 0, 3, 1, 1)

		self.rdo_rplUser.setObjectName(_fromUtf8("rdo_rplUser"))
		self.gridLayout_3.addWidget(self.rdo_rplUser, 0, 2, 1, 1)

		self.rdo_defUser.setChecked(True)
		self.rdo_defUser.setObjectName(_fromUtf8("rdo_defUser"))
		self.gridLayout_3.addWidget(self.rdo_defUser, 0, 0, 1, 1)
		self.horizontalLayout_4.addWidget(self.groupBox_2)
		spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout_4.addItem(spacerItem)
		self.gridLayout_5 = QtGui.QGridLayout()
		self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))

		self.chk_sendAll.setObjectName(_fromUtf8("chk_sendAll"))
		self.gridLayout_5.addWidget(self.chk_sendAll, 1, 0, 1, 1)

		self.btn_apply.setMinimumSize(QtCore.QSize(120, 30))
		self.btn_apply.setObjectName(_fromUtf8("btn_apply"))
		self.gridLayout_5.addWidget(self.btn_apply, 1, 1, 1, 1)
		spacerItem1 = QtGui.QSpacerItem(20, 15, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
		self.gridLayout_5.addItem(spacerItem1, 0, 1, 1, 1)
		self.horizontalLayout_4.addLayout(self.gridLayout_5)
		self.verticalLayout_3.addLayout(self.horizontalLayout_4)
		self.line = QtGui.QFrame(self.centralwidget)
		self.line.setFrameShape(QtGui.QFrame.HLine)
		self.line.setFrameShadow(QtGui.QFrame.Sunken)
		self.line.setObjectName(_fromUtf8("line"))
		self.verticalLayout_3.addWidget(self.line)
		self.horizontalLayout = QtGui.QHBoxLayout()
		self.horizontalLayout.setContentsMargins(5, -1, 5, -1)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.btn_reset.sizePolicy().hasHeightForWidth())
		self.btn_reset.setMinimumSize(QtCore.QSize(75, 30))
		self.btn_reset.setObjectName(_fromUtf8("btn_reset"))
		self.horizontalLayout.addWidget(self.btn_reset)
		spacerItem2 = QtGui.QSpacerItem(300, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem2)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.btn_rename.sizePolicy().hasHeightForWidth())
		self.btn_rename.setSizePolicy(sizePolicy)
		self.btn_rename.setMinimumSize(QtCore.QSize(100, 30))
		self.btn_rename.setObjectName(_fromUtf8("btn_rename"))

		self.horizontalLayout.addWidget(self.btn_rename)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.btn_sendToServer.sizePolicy().hasHeightForWidth())

		self.btn_sendToServer.setSizePolicy(sizePolicy)
		self.btn_sendToServer.setMinimumSize(QtCore.QSize(170, 30))
		self.btn_sendToServer.setObjectName(_fromUtf8("btn_sendToServer"))
		self.horizontalLayout.addWidget(self.btn_sendToServer)
		self.horizontalLayout.setStretch(1, 2)
		self.horizontalLayout.setStretch(3, 2)
		self.verticalLayout_3.addLayout(self.horizontalLayout)
		self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 699, 21))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		MainWindow.setMenuBar(self.menubar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
		item = self.tbl_fileList.horizontalHeaderItem(0)
		item.setText(QtGui.QApplication.translate("MainWindow", "Input file", None, QtGui.QApplication.UnicodeUTF8))
		item = self.tbl_fileList.horizontalHeaderItem(1)
		item.setText(QtGui.QApplication.translate("MainWindow", "Destination file", None, QtGui.QApplication.UnicodeUTF8))
		item = self.tbl_fileList.horizontalHeaderItem(2)
		item.setText(QtGui.QApplication.translate("MainWindow", "Destination path", None, QtGui.QApplication.UnicodeUTF8))
		item = self.tbl_fileList.horizontalHeaderItem(3)
		item.setText(QtGui.QApplication.translate("MainWindow", "Status", None, QtGui.QApplication.UnicodeUTF8))
		self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Versions", None, QtGui.QApplication.UnicodeUTF8))
		self.rdo_workFile.setText(QtGui.QApplication.translate("MainWindow", "Work", None, QtGui.QApplication.UnicodeUTF8))
		self.rdo_heroFile.setText(QtGui.QApplication.translate("MainWindow", "Hero", None, QtGui.QApplication.UnicodeUTF8))
		self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "User Name", None, QtGui.QApplication.UnicodeUTF8))
		self.rdo_defUser.setText(QtGui.QApplication.translate("MainWindow", "Default", None, QtGui.QApplication.UnicodeUTF8))
		self.rdo_rplUser.setText(QtGui.QApplication.translate("MainWindow", "Replace", None, QtGui.QApplication.UnicodeUTF8))
		self.chk_sendAll.setText(QtGui.QApplication.translate("MainWindow", "All Items", None, QtGui.QApplication.UnicodeUTF8))
		self.btn_apply.setText(QtGui.QApplication.translate("MainWindow", "Apply", None, QtGui.QApplication.UnicodeUTF8))
		self.btn_reset.setText(QtGui.QApplication.translate("MainWindow", "Reset", None, QtGui.QApplication.UnicodeUTF8))
		self.btn_rename.setText(QtGui.QApplication.translate("MainWindow", "Rename Only", None, QtGui.QApplication.UnicodeUTF8))
		self.btn_sendToServer.setText(QtGui.QApplication.translate("MainWindow", "Send to Server", None, QtGui.QApplication.UnicodeUTF8))

