# By Kun

#Import python modules
import os, sys, re
sys.path.append('O:\\studioTools\\lib\\pyqt')
sys.path.append('O:\\studioTools\\maya\\python')

#Import GUI
from PyQt4 import QtCore, QtGui, uic

# import pipeline modules
from tool.utils import config, fileUtils

moduleFile = sys.modules[__name__].__file__
moduleDir = os.path.dirname(moduleFile)
sys.path.append(moduleDir)

#from Ui_file2server import Ui_MainWindow

projectInfo = {'frd' : 'Lego_FRDCG',
                'frz' : 'Lego_Frozen',
                'cty' : 'Lego_CTYCG',
                'ppl' : 'Lego_Pipeline'}

class ptShotNameConvention:
    """Data wrapper for breaking down shot name convention into shot information"""
    def __init__(self, filePath):
        
        self.breakdownFileName(filePath)

    def breakdownFileName(self, filePath):
        """break down file name into shot information"""

        #Original input
        self.IFileName = filePath.split('/')[-1]
        self.IFileDir = '/'.join(filePath.split('/')[:-1])
        self.IFilePath = filePath

        nameSplit = self.IFileName.split('_')
        splitCount = len(nameSplit)

        allRegex = re.compile(r'(.+_){2,}q[0-9]{4}_s[0-9]{4}_\w+[.][a-zA-Z]+')
        if not allRegex.match(self.IFilePath):
            raise AssertionError('Invalid name convention')

        halfRegex = re.compile(r'_q[0-9]{4}_s[0-9]{4}_')
        halfSplit = halfRegex.split(self.IFileName)
        halfMatch = halfRegex.search(self.IFileName).group(0)

        epSplit = halfSplit[0].split('_', 1)
        self.project = epSplit[0]
        self.episode = epSplit[1]

        seqSplit = halfMatch.split('_')
        self.seq = seqSplit[1]
        self.shot = seqSplit[2]

        verRegex = re.compile(r'_v[0-9]+_')
        verSplit = verRegex.split(halfSplit[1])

        #hero file
        if len(verSplit) < 2:
            extSplit = verSplit[0].split('.')
            self.dep = extSplit[0]
            self.isHero = True
            self.version = ''
            self.userName = ''
            self.extension = extSplit[-1]
        #work file
        else:
            self.dep = verSplit[0]
            self.isHero = False

            extSplit = verSplit[1].split('.')
            self.userName = extSplit[0]
            self.extension = extSplit[1]

            verMatch = verRegex.search(halfSplit[1]).group(0)
            self.version = verMatch.split('_')[1]

        self.projName = None
        self.epName = None


def autoCorrectConvention(shot, episode=None):
    """"""
    projName = projectInfo[shot.project]
    epName = 'None'
    epCode = episode if episode else shot.episode

    epConfigList = config.searchConfig(epCode, config.episodeConfig)
    
    if not epConfigList and not episode:
        epCode = shot.episode.lower()
        epConfigList = config.searchConfig(epCode, config.episodeConfig)

    if not epConfigList and not episode:
        epCode = shot.episode.upper()
        epConfigList = config.searchConfig(epCode, config.episodeConfig)

    if not epConfigList and not episode:
        epName = shot.IFileDir.split('/')[3]

        epConfigList = config.searchConfig(epName, config.episodeConfig)
        for epEntry in epConfigList:
            epInfo = epEntry.split(':')
            
            if epInfo[0] == projName:
                if epInfo[1] == epName:
                    epCode = epInfo[3]
                    break
    else:
        for epEntry in epConfigList:
            epInfo = epEntry.split(':')
            #Searching config with just an epCode can get urself duplicate entries, so project name is needed for the query.
            if epInfo[0] == projName:
                if epInfo[3] == epCode:
                    epName = epInfo[1]
                    break

    shot.projName = projName
    shot.episode = epCode
    shot.epName = epName

def constructFileName(shot, version=None, userName=None, isHero=None):
    """generate new fileName"""
    if isHero==None : isHero = shot.isHero
    if version==None : version = shot.version
    if userName==None : userName = shot.userName

    filePathPart = '_'.join([shot.project, shot.episode, shot.seq, shot.shot, shot.dep])

    verCtrlPart = ''
    if isHero == False:
        verCtrlPart = '_'+version+'_'+userName

    return filePathPart+verCtrlPart+'.'+shot.extension

def determineFilePath(shot, isHero=None):
    """Construct file path based from file name"""
    if isHero==None : isHero = shot.isHero 

    typeFolder = 'playblast' if shot.extension == 'mov' else 'scenes'

    if isHero == True:
        return '/'.join([config.drive, shot.projName, 'film', shot.epName, shot.seq, shot.shot, shot.dep, typeFolder])
    else:
        return '/'.join([config.drive, shot.projName, 'film', shot.epName, shot.seq, shot.shot, shot.dep, typeFolder, 'work'])


#load ui using PyQt uic
form_class, base_class = uic.loadUiType("%s/ui.ui" % moduleDir)

class MyForm(form_class, base_class):

    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)

        self.fileList = []

        #setup ui
        self.setupUi(self)
        self.setWindowTitle('PT Pipeline File Drop Tool')

        self.tbl_fileList.setAcceptDrops(True)
        self.tbl_fileList.setColumnWidth(0, 260)
        self.tbl_fileList.setColumnWidth(1, 260)
        self.tbl_fileList.setColumnWidth(2, 330)
        self.tbl_fileList.setColumnWidth(3, 60)
        self.tbl_fileList.horizontalHeader().setMinimumSectionSize(60)
            #.setResizeMode(QtGui.QHeaderView.ResizeToContents)
        self.tbl_fileList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        
        #install event filter on widgets that we want to intercept events.
        self.tbl_fileList.installEventFilter(self)
        
        self.initSignals()

    def initSignals(self): 
        """ connect qt signal """
        self.rdo_heroFile.toggled.connect(self.toggleUserNameEdit)
        self.rdo_workFile.toggled.connect(self.toggleUserNameEdit)
        self.btn_reset.clicked.connect(self.clearData)
        self.btn_apply.clicked.connect(self.applyRename)
        self.btn_rename.clicked.connect(self.renameFiles)
        self.btn_sendToServer.clicked.connect(self.copyFiles)
        
    def initFunctions(self): 
        """ initial function that need to run first """ 
        print 'ha'

    def fillInTable(self, row, column, text, color = [255, 255, 255]):
        """ add item to table """
        item = QtGui.QTableWidgetItem()
        item.setText(text)
        item.setBackground(QtGui.QColor(color[0], color[1], color[2]))
        self.tbl_fileList.setItem(row, column, item)

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

                if fileName.endswith('.ma') or fileName.endswith('.mov'):
                    if self.isUniqueInput(fileName):
                        currRow = numRow+i

                        #store data in array of ptShotNameConvention class, which will automatically split filepath into strip for easy to change later.
                        self.fileList.append(ptShotNameConvention(fileName))

                        self.tbl_fileList.insertRow(currRow)
                        self.fillInTable(currRow, 0, self.fileList[currRow].IFileName)
                        self.tbl_fileList.resizeColumnToContents(0)

                        autoCorrectConvention(self.fileList[currRow])
                        #we must always fill filePath first, befor fileName. Since in case of workfile, we need filePath to get latest version number
                        newPath = determineFilePath(self.fileList[currRow])
                        self.fillInTable(currRow, 2, newPath)
                        self.tbl_fileList.resizeColumnToContents(2)

                        version = None
                        if self.fileList[currRow].isHero == False:
                            version = 'v%03d' % (int(self.fileList[currRow].version[1:])+1)

                        newName = constructFileName(self.fileList[currRow], version, isHero=self.fileList[currRow].isHero)
                        self.fillInTable(currRow, 1, newName)
                        self.tbl_fileList.resizeColumnToContents(1)

                        i += 1

            self.scanForFileConflict()
            self.scanForNameConflict()


    def clearData(self):
        """remove data from both list and table"""
        rowCount = self.tbl_fileList.rowCount()

        for row in range(rowCount,0,-1) :
            self.tbl_fileList.removeRow(row-1)

        #del self.tbl_fileList.fileList[:]
        self.fileList[:] = []

        self.btn_sendToServer.setEnabled(True)

    def scanForNameConflict(self):
        """check if dropped files end up as same file"""
        destFileList = []

        for row in range(self.tbl_fileList.rowCount()):
            destFileList.append(str(self.tbl_fileList.item(row, 1).text()))

        for i in range(len(destFileList) - 1):
            for j in range(i + 1, len(destFileList)):
                if i != j:
                    if destFileList[i] == destFileList[j]:
                        self.fillInTable(i, 3, 'Duplicated', color=[215, 30, 30])
                        self.fillInTable(j, 3, 'Duplicated', color=[215, 30, 30])

    def scanForFileConflict(self):
        """check if destination files exist on server, then update Status column"""
        for i in range(self.tbl_fileList.rowCount()):
            if self.tbl_fileList.item(i, 1) != None and self.tbl_fileList.item(i, 2) != None:
                if os.path.exists(str(self.tbl_fileList.item(i, 2).text())):# + '/' + str(self.tbl_fileList.item(i, 1).text())):
                    self.fillInTable(i, 3, 'Exist', color=[255, 230, 40])
                else:
                    self.fillInTable(i, 3, 'Not Exist', color=[215, 30, 30])

    def isUniqueInput(self, filePath):
        """Check if the input filePath has already been dropped on the table"""
        for fileInfo in self.fileList:
            if filePath == fileInfo.IFilePath:
                return False

        return True

    def updateSubmitStatus(self, i=0, success=True):
        """change status after successfully copy files to destination"""
        if success:
            self.fillInTable(i, 3, 'Submitted', color = [0, 180, 55])
        else:
            self.fillInTable(i, 3, 'Failed', color = [215, 30, 30])

    def toggleUserNameEdit(self):
        
        if self.rdo_heroFile.isChecked() == True:
            self.txt_rplUser.setEnabled(False)
        else:
            self.txt_rplUser.setEnabled(True)

    def applyRenameEach(self, i=0):
        """Apply input changed on each row. See applyRename() for decision route."""
        proj = str(self.txt_proj.text())
        ep = str(self.txt_ep.text())

        if proj:
            self.fileList[i].project = proj
        if ep:
            autoCorrectConvention(self.fileList[i], ep)

        #determine new filePath first, coz we need it when check for next incremental version
        newPath = determineFilePath(self.fileList[i], self.rdo_heroFile.isChecked())
        self.fillInTable(i, 2, newPath)

        #then calculate new fileName part
        eachInfo = self.fileList[i]
        version = ''
        userName = ''

        if self.rdo_workFile.isChecked():
            #Get latest version number from related directories
            if self.fileList[i].version=='':
            	version = fileUtils.getFileVersionInfo(newPath, outputMode=1, incremental=False, extension=self.fileList[i].extension)
            else:
            	version = 'v%03d' % (int(self.fileList[i].version[1:])+1)

            if str(self.txt_rplUser.text()):
                userName = self.txt_rplUser.text()
            else:
                if eachInfo.userName == '':
                    userName = 'PT'
                else:
                    userName = eachInfo.userName

        newName = constructFileName(self.fileList[i], version, userName, self.rdo_heroFile.isChecked())
        self.fillInTable(i, 1, newName)

        self.tbl_fileList.resizeColumnsToContents()

    def applyRename(self):
        """Apply any input adjusted by user on tableView first. but not making any change to the actual files yet."""
        if self.chk_sendAll.isChecked():
            for i in range(len(self.fileList)):
                self.applyRenameEach(i)
        else:
            #selectionModel() will return QModelIndex. With this obj, u can dynamically get row and column from selectedItem with ease.
            selModel = self.tbl_fileList.selectionModel()
            modelIndexList = selModel.selectedRows(2)

            for each in modelIndexList:
                i = self.tbl_fileList.itemFromIndex(each).row()
                self.applyRenameEach(i)

        self.scanForFileConflict()
        self.scanForNameConflict()

    def renameFiles(self):
        """Rename files. This func will always check if there are any duplicated status row. If yes, files will not be renamed."""
        totalRow = self.tbl_fileList.rowCount()

        if totalRow != 0:
            count = 0

            duplicatedList = self.tbl_fileList.findItems('Duplicated', QtCore.Qt.MatchExactly)

            if duplicatedList:
                msgBox = QtGui.QMessageBox()
                msgBox.setText(str(len(duplicatedList))+" files have duplicated names. Consider rename them?")
                msgBox.setWindowTitle("Dear Production")
                msgBox.exec_()

            else:
                for rowNum in range(totalRow):
                    try:
                        src = self.fileList[rowNum].IFilePath
                        dst = self.fileList[rowNum].IFileDir+'/'+str(self.tbl_fileList.item(rowNum, 1).text())
                        fileUtils.rename(src, dst)
                        
                        self.fileList[rowNum].breakdownFileName(dst)
                        self.fillInTable(rowNum, 0, self.fileList[rowNum].IFileName)

                        count += 1
                            #Since we need to hit apply button before we reach this state, I guess we dont need to do status check anymore?
                            #self.tbl_fileList.scanForNameConflict()
                            #self.tbl_fileList.scanForFileConflict()
                    except Exception as e:
                        print "Unexpected error:", e

                msgBox = QtGui.QMessageBox()
                msgBox.setWindowTitle("Dear Production")
                msgBox.setText(str(count)+" files have been renamed.")
                msgBox.exec_()

    def copyFiles(self):
        """blaa"""
        totalRow = self.tbl_fileList.rowCount()

        if totalRow != 0:
            successCount = 0
            failCount = 0

            existList = self.tbl_fileList.findItems('Exist', QtCore.Qt.MatchExactly)

            if existList:
                msgBox = QtGui.QMessageBox()
                msgBox.setText(str(len(existList))+" files already exist. Do you want to override them?")
                msgBox.setStandardButtons(QtGui.QMessageBox.Save | QtGui.QMessageBox.Cancel)
                msgBox.setDefaultButton(QtGui.QMessageBox.Cancel)
                msgBox.setWindowTitle("Dear Production")

                if msgBox.exec_() == QtGui.QMessageBox.Cancel:
                    return 0

            for rowNum in range(totalRow):
                try:
                    src = self.fileList[rowNum].IFilePath
                    dst = str(self.tbl_fileList.item(rowNum, 2).text())+'/'+str(self.tbl_fileList.item(rowNum, 1).text())
                    fileUtils.copy(src, dst)
                    os.utime(dst, None)
                    self.updateSubmitStatus(rowNum, True)

                    successCount += 1
                except:
                    self.updateSubmitStatus(rowNum, False)
                    print "Unexpected error:", sys.exc_info()[0]
                    failCount += 1

            msgBox = QtGui.QMessageBox()
            msgBox.setWindowTitle("Dear Production")

            if failCount == 0:
                msgBox.setText("All files have been successfully submitted.")
            else:
                msgBox.setText(str(successCount)+" succeeded. "+str(failCount)+" failed. Please check the table for more details.")
            msgBox.exec_()

            self.btn_sendToServer.setEnabled(False)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
