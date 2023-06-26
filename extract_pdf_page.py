import PyPDF2 as pdf
import os, sys
from PyQt5 import QtWidgets, QtCore
import mainWindow

class CopyPages(QtCore.QThread):
    """ Поток для копирования страниц(ы)
        из pdf файла
    """
    signalCopyPages = QtCore.pyqtSignal(QtCore.QVariant)
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        self.exec_()
    
class MainWindow(QtWidgets.QWidget):
    """ Класс для главного окна приложения
    """
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        # Подключение класса формы главного окна приложения
        self.form = mainWindow.Ui_pdfForm()
        self.form.setupUi(self)

        # Переменные класса
        self.nameFileSource = None
        self.nameFileDest = None
        self.nameFileSave = None
        self.numberPagesCopyDel = []
        self.numberPageInsert = 0
        self.valueSelectProgram = 1
        self.valueSelectPages = 2
        self.__curFile = os.path.realpath(__file__)
        self.__dirName = os.path.dirname(self.__curFile)

        # Свойства элементов формы при инициализации
        self.form.lNameFiletoCopy.setEnabled(False)
        self.form.lblNameFiletoCopy.setEnabled(False)
        self.form.btnSelectFileToCopy.setEnabled(False)
        self.form.btnRun.setEnabled(False)
        self.form.btnNewName.setEnabled(False)
        self.form.gbPages.setEnabled(False)
        self.form.gbDestinationFile.setEnabled(False)
        self.form.lblFileToCopy.setEnabled(False)
        self.form.lNumberPageDest.setEnabled(False)
        self.form.rbCopyPages.setChecked(True)
        self.form.rbNumberItem.setChecked(True)
        self.form.rbCopyPages.country = 1
        self.form.rbDeletePages.country = 2
        self.form.rbCopyToCopy.country = 3
        self.form.rbDiapazon.country = 1
        self.form.rbNumberItem.country = 2

        # Обработчики событий
        self.form.btnCancel.clicked.connect(self.cancelForm)
        self.form.btnSelectFile.clicked.connect(self.selectSourceFile)
        self.form.btnSelectFileToCopy.clicked.connect(self.selectFiletoCopy)
        self.form.btnNewName.clicked.connect(self.getNewNameDestFile)
        self.form.btnRun.clicked.connect(self.runProgram)
        self.form.btnAbout.clicked.connect(self.aboutForm)
        self.form.rbCopyPages.toggled.connect(self.on_clickOperation)
        self.form.rbDeletePages.toggled.connect(self.on_clickOperation)
        self.form.rbCopyToCopy.toggled.connect(self.on_clickOperation)
        self.form.rbDiapazon.toggled.connect(self.on_clickSelectPages)
        self.form.rbNumberItem.toggled.connect(self.on_clickSelectPages)

    def cancelForm(self):
        """ Закрытие формы и приложения"""
        self.close()

    def selectSourceFile(self):
        """ Функция-обработчки для выбора
            файла, из которого нужно копировать
            или удалять страницы.
        """
        dialog_window = QtWidgets.QFileDialog()
        temp_namefile = dialog_window.getOpenFileName(self, "Открыть файл", "C:\\", "(*.pdf)")
        if temp_namefile[0] != '':
            self.nameFileSource = temp_namefile[0]
            self.form.lNameFileSource.setText(self.nameFileSource)
            self.form.gbPages.setEnabled(True)
            self.changeEnabledElementNewName()
            temp = self.getNameForSave(self.nameFileSource)
            self.setNameForSave(temp)

    def selectFiletoCopy(self):
        """ Функция-обработчик для выбора
            файла, в который нужно скопировать
            набор страниц из первого файла
        """
        dialog_window = QtWidgets.QFileDialog()
        temp_namefile = dialog_window.getOpenFileName(self, "Открыть файл", "C:\\", "(*.pdf)")
        if temp_namefile[0] != '':
            self.nameFileToCopy = temp_namefile[0]
            self.form.lNameFiletoCopy.setText(self.nameFileToCopy)
            temp = self.getNameForSave(self.nameFileToCopy)
            self.setNameForSave(temp)
            self.changeEnabledElementNewName()

    def getNewNameDestFile(self):
        """ Функция-обработчик для активации поля
            ввода, для ввода нового имени файла,
            для сохранения.
        """
        self.form.lNameSaveFile.setEnabled(True)
        self.form.btnNewName.setEnabled(False)

    def runProgram(self):
        """ Функция-обработчик для запуска
            основной программы работы с PDF
            файлами.
        """
        if self.form.lNumberPages.text() == '':
            msgbox = QtWidgets.QMessageBox()
            msgbox.setWindowTitle("Ошибка ввода данных")
            msgbox.setText("Чтобы продолжить, необходимо ввести номера страниц для копирования (удаления)")
            msgbox.setIcon(QtWidgets.QMessageBox.Information)
            msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgbox.exec_()
        else:
            self.nameFileSource = self.form.lNameFileSource.text()
            self.nameFileDest = self.form.lNameFiletoCopy.text()
            self.nameFileSave = os.path.join(os.path.dirname(self.nameFileSource), self.form.lNameSaveFile.text() + '.pdf')
            self.numberPagesCopyDel = self.getNumberPages()

            try:
                if self.valueSelectProgram == 1:
                    self.copyPages(self.nameFileSource, self.numberPagesCopyDel, self.nameFileSave)
                elif self.valueSelectProgram == 2:
                    self.deletePages(self.nameFileSource, self.numberPagesCopyDel, self.nameFileSave)
                else:
                    self.numberPageInsert = int(self.form.lNumberPageDest.text())
                    self.copyToCopyPages(self.nameFileSource, self.numberPagesCopyDel, self.nameFileDest, self.numberPageInsert, self.nameFileSave)
                self.informationProgress()
                self.setAgain()
            except:
                self.criticalMessage()
                self.setAgain()

    def copyPages(self, nameSourceFile, listNumberPage, nameSaveFile):
        """ Функция для копирования страниц(ы)
            из документа
        """
        pdfFile, pdfFileObject = self.openPdfFile(nameSourceFile)
        pdfWriter = pdf.PdfFileWriter()

        for page in listNumberPage:
            curPage = page - 1
            pageObj = pdfFile.getPage(curPage)
            pdfWriter.addPage(pageObj)

        outFile = nameSaveFile
        pdfOutFile = open(outFile, 'wb')
        pdfWriter.write(pdfOutFile)
        pdfOutFile.close()
        pdfFileObject.close()

    def deletePages(self, nameSourceFile, listNumberPage, nameSaveFile):
        """ Функция для удаления выбранных страниц из документа"""
        pdfFile, pdfFileObject = self.openPdfFile(nameSourceFile)
        pdfWriter = pdf.PdfFileWriter()

        for pageNum in range(pdfFile.numPages):
            flag = False
            for page in listNumberPage:
                currentPage = page - 1
                if pageNum == currentPage:
                    flag = True
                    break
                else:
                    pass
            if flag:
                continue
            else:
                pageObj = pdfFile.getPage(pageNum)
                pdfWriter.addPage(pageObj)

        pdfOutFile = open(nameSaveFile, 'wb')
        pdfWriter.write(pdfOutFile)
        pdfOutFile.close()
        pdfFileObject.close()

    def copyToCopyPages(self, nameSourceFile, listNumberPage, nameDestFile, numberPageDest, nameSaveFile):
        pdfFile1, pdfFileObject1 = self.openPdfFile(nameSourceFile)
        pdfFile2, pdfFileObject2 = self.openPdfFile(nameDestFile)
        pdfWriter = pdf.PdfFileWriter()

        for pageNum in range(numberPageDest):
            pageObj = pdfFile2.getPage(pageNum)
            pdfWriter.addPage(pageObj)
        for pageNum in listNumberPage:
            curPage = pageNum - 1
            pageObj = pdfFile1.getPage(curPage)
            pdfWriter.addPage(pageObj)
        for pageNum in range(numberPageDest, pdfFile2.numPages):
            if numberPageDest == pdfFile2.numPages:
                break
            pageObj = pdfFile2.getPage(pageNum)
            pdfWriter.addPage(pageObj)

        pdfOutFile = open(nameSaveFile, 'wb')
        pdfWriter.write(pdfOutFile)
        pdfOutFile.close()
        pdfFileObject1.close()
        pdfFileObject2.close()

    def aboutForm(self):
        """ Функция-обработчик для вывода
            информации о программе
        """
        msgAbout = QtWidgets.QMessageBox()
        msgAbout.resize(800, 250)
        msgAbout.setWindowTitle("Информация")
        msgAbout.setText("Эта небольшая программка позволяет без хлопот скопировать или удалить\n"+
            "произвольное количество страниц из *pdf документа, а также копировать\n"+
            "страницы из одного файла в другой.\n\n"+
            "ОБРАТИТЕ ВНИМАНИЕ!\n"+
            "1. Номера страниц нужно вводить через запятую, без пробелов, либо диапазоном через тире также без пробелов.\n"+
            "2. Рекомендую вводить номера страниц в порядке их возрастания, поскольку копироваться "+
            "они будут в том порядке, в котором вы их ввели. Для удаления это несущественно.\n"+
            "3. При копировании страниц из одного документа в другой, массив страниц будет скопирован в другой файл, "+
            "в выбранную вами позицию (после выбранной страницы), после чего так же будут идти оставшиеся страницы "+
            "исходного документа.\n\n"+
            "Благодарности и пожелания можете направлять на почту: vbogoduhov@yandex.ru\n"+
            "Все они будут прочитаны, бОльшего обещать не могу!\n\n")
        msgAbout.setIcon(QtWidgets.QMessageBox.Information)
        msgAbout.StandardButton(QtWidgets.QMessageBox.Ok)
        msgAbout.exec_()

    def getNameForSave(self, nameFile):
        splitList = nameFile.split(sep="/")
        tempNameFile = splitList[-1][:-4]

        return tempNameFile

    def setNameForSave(self, nameFile):
        self.form.lNameSaveFile.setText(nameFile+'_modify')
        self.form.gbDestinationFile.setEnabled(True)
        self.form.btnRun.setEnabled(True)

    def on_clickOperation(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            rbFlag = radioButton.country
            self.valueSelectProgram = rbFlag
            self.changeEnabledElementCopyToCopy() if self.valueSelectProgram == 3 else self.changeEnabledElementCopyToCopy(False)

    def on_clickSelectPages(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            rbFlag = radioButton.country
            self.valueSelectPages = rbFlag

    def changeEnabledElementCopyToCopy(self, flag=True):
        self.form.lblNameFiletoCopy.setEnabled(flag)
        self.form.lNameFiletoCopy.setEnabled(flag)
        self.form.btnSelectFileToCopy.setEnabled(flag)
        self.form.lblFileToCopy.setEnabled(flag)
        self.form.lNumberPageDest.setEnabled(flag)

    def changeEnabledElementNewName(self):
        self.form.lNameSaveFile.setEnabled(False)
        self.form.btnNewName.setEnabled(True)

    def openPdfFile(self, nameFile):
        """
        открытие файла *pdf
        """
        pdfFileObj = open(nameFile, 'rb')
        pdfReader = pdf.PdfFileReader(pdfFileObj, strict=False)
        return pdfReader, pdfFileObj

    def getNumberPages(self):
        """ Функция для считывания и преобразования
            номеров страниц для копирования (удаления)
        """
        tempListPages = self.form.lNumberPages.text()
        if self.valueSelectPages == 2:
            numberPagesCopyDel = [int(page) for page in tempListPages.split(sep=',')]
        else:
            temptempPages = tempListPages.split(sep='-')
            numberPagesCopyDel = [page for page in range(int(temptempPages[0]), int(temptempPages[1])+1)]

        return numberPagesCopyDel

    def informationProgress(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Операция выполнена")
        msg.setText("Операция над файлом выполнена. Итоговый файл сохранён!")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def criticalMessage(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Ошибка")
        msg.setText("В процессе выполнения операции возникла ошибка!")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setStandardButtons(QtWidgets.QMessageBox.Cancel)
        msg.exec_()

    def setAgain(self):
        self.form.lNameFileSource.clear()
        self.form.lNameFiletoCopy.clear()
        self.form.lNameSaveFile.clear()
        self.form.lNumberPages.clear()
        self.form.lNumberPageDest.clear()
        self.form.gbPages.setEnabled(False)
        self.form.lblFileToCopy.setEnabled(False)
        self.form.lblFileToCopy.setEnabled(False)
        self.form.lNumberPageDest.setEnabled(False)
        self.form.gbDestinationFile.setEnabled(False)
        self.form.lblNameFiletoCopy.setEnabled(False)
        self.form.lNameFiletoCopy.setEnabled(False)
        self.form.btnRun.setEnabled(False)
        self.form.btnNewName.setEnabled(False)
        self.form.btnSelectFileToCopy.setEnabled(False)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    sys.exit(app.exec_())