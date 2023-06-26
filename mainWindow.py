# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\allinMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pdfForm(object):
    def setupUi(self, pdfForm):
        pdfForm.setObjectName("pdfForm")
        pdfForm.resize(810, 355)
        pdfForm.setMinimumSize(QtCore.QSize(810, 355))
        pdfForm.setMaximumSize(QtCore.QSize(810, 355))
        self.gbSelectFiles = QtWidgets.QGroupBox(pdfForm)
        self.gbSelectFiles.setGeometry(QtCore.QRect(10, 5, 500, 261))
        self.gbSelectFiles.setObjectName("gbSelectFiles")
        self.lNameFileSource = QtWidgets.QLineEdit(self.gbSelectFiles)
        self.lNameFileSource.setGeometry(QtCore.QRect(10, 50, 350, 25))
        self.lNameFileSource.setObjectName("lNameFileSource")
        self.lblNameSourceFile = QtWidgets.QLabel(self.gbSelectFiles)
        self.lblNameSourceFile.setGeometry(QtCore.QRect(10, 30, 150, 16))
        self.lblNameSourceFile.setObjectName("lblNameSourceFile")
        self.btnSelectFile = QtWidgets.QPushButton(self.gbSelectFiles)
        self.btnSelectFile.setGeometry(QtCore.QRect(380, 50, 110, 25))
        self.btnSelectFile.setObjectName("btnSelectFile")
        self.groupBox_3 = QtWidgets.QGroupBox(self.gbSelectFiles)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 90, 351, 101))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 21, 263, 76))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rbCopyPages = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbCopyPages.setObjectName("rbCopyPages")
        self.verticalLayout.addWidget(self.rbCopyPages)
        self.rbDeletePages = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbDeletePages.setObjectName("rbDeletePages")
        self.verticalLayout.addWidget(self.rbDeletePages)
        self.rbCopyToCopy = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbCopyToCopy.setObjectName("rbCopyToCopy")
        self.verticalLayout.addWidget(self.rbCopyToCopy)
        self.lblNameFiletoCopy = QtWidgets.QLabel(self.gbSelectFiles)
        self.lblNameFiletoCopy.setGeometry(QtCore.QRect(10, 200, 331, 16))
        self.lblNameFiletoCopy.setObjectName("lblNameFiletoCopy")
        self.lNameFiletoCopy = QtWidgets.QLineEdit(self.gbSelectFiles)
        self.lNameFiletoCopy.setGeometry(QtCore.QRect(10, 220, 350, 25))
        self.lNameFiletoCopy.setObjectName("lNameFiletoCopy")
        self.btnSelectFileToCopy = QtWidgets.QPushButton(self.gbSelectFiles)
        self.btnSelectFileToCopy.setGeometry(QtCore.QRect(380, 220, 110, 25))
        self.btnSelectFileToCopy.setObjectName("btnSelectFileToCopy")
        self.gbPages = QtWidgets.QGroupBox(pdfForm)
        self.gbPages.setGeometry(QtCore.QRect(519, 5, 281, 261))
        self.gbPages.setObjectName("gbPages")
        self.lblSelectPages = QtWidgets.QLabel(self.gbPages)
        self.lblSelectPages.setGeometry(QtCore.QRect(10, 30, 221, 16))
        self.lblSelectPages.setObjectName("lblSelectPages")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.gbPages)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 50, 141, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rbDiapazon = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.rbDiapazon.setObjectName("rbDiapazon")
        self.verticalLayout_2.addWidget(self.rbDiapazon)
        self.rbNumberItem = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.rbNumberItem.setObjectName("rbNumberItem")
        self.verticalLayout_2.addWidget(self.rbNumberItem)
        self.labelPages = QtWidgets.QPlainTextEdit(self.gbPages)
        self.labelPages.setEnabled(False)
        self.labelPages.setGeometry(QtCore.QRect(8, 105, 271, 41))
        self.labelPages.setFrameShape(QtWidgets.QFrame.Box)
        self.labelPages.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.labelPages.setLineWidth(0)
        self.labelPages.setMidLineWidth(0)
        self.labelPages.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.labelPages.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.labelPages.setReadOnly(True)
        self.labelPages.setOverwriteMode(True)
        self.labelPages.setObjectName("labelPages")
        self.lNumberPages = QtWidgets.QLineEdit(self.gbPages)
        self.lNumberPages.setGeometry(QtCore.QRect(10, 150, 110, 25))
        self.lNumberPages.setObjectName("lNumberPages")
        self.lblFileToCopy = QtWidgets.QLabel(self.gbPages)
        self.lblFileToCopy.setGeometry(QtCore.QRect(10, 200, 261, 16))
        self.lblFileToCopy.setWordWrap(True)
        self.lblFileToCopy.setObjectName("lblFileToCopy")
        self.lNumberPageDest = QtWidgets.QLineEdit(self.gbPages)
        self.lNumberPageDest.setGeometry(QtCore.QRect(10, 220, 110, 25))
        self.lNumberPageDest.setObjectName("lNumberPageDest")
        self.gbDestinationFile = QtWidgets.QGroupBox(pdfForm)
        self.gbDestinationFile.setGeometry(QtCore.QRect(10, 266, 500, 81))
        self.gbDestinationFile.setObjectName("gbDestinationFile")
        self.lNameSaveFile = QtWidgets.QLineEdit(self.gbDestinationFile)
        self.lNameSaveFile.setEnabled(False)
        self.lNameSaveFile.setGeometry(QtCore.QRect(10, 40, 350, 25))
        self.lNameSaveFile.setObjectName("lNameSaveFile")
        self.lblSaveFile = QtWidgets.QLabel(self.gbDestinationFile)
        self.lblSaveFile.setGeometry(QtCore.QRect(10, 20, 311, 16))
        self.lblSaveFile.setObjectName("lblSaveFile")
        self.btnNewName = QtWidgets.QPushButton(self.gbDestinationFile)
        self.btnNewName.setGeometry(QtCore.QRect(380, 40, 110, 25))
        self.btnNewName.setObjectName("btnNewName")
        self.btnRun = QtWidgets.QPushButton(pdfForm)
        self.btnRun.setGeometry(QtCore.QRect(640, 273, 160, 30))
        self.btnRun.setObjectName("btnRun")
        self.btnCancel = QtWidgets.QPushButton(pdfForm)
        self.btnCancel.setGeometry(QtCore.QRect(706, 316, 95, 30))
        self.btnCancel.setObjectName("btnCancel")
        self.btnAbout = QtWidgets.QToolButton(pdfForm)
        self.btnAbout.setGeometry(QtCore.QRect(640, 316, 27, 30))
        self.btnAbout.setObjectName("btnAbout")

        self.retranslateUi(pdfForm)
        QtCore.QMetaObject.connectSlotsByName(pdfForm)

    def retranslateUi(self, pdfForm):
        _translate = QtCore.QCoreApplication.translate
        pdfForm.setWindowTitle(_translate("pdfForm", "Работа с PDF"))
        self.gbSelectFiles.setTitle(_translate("pdfForm", "Выбор файлов"))
        self.lblNameSourceFile.setText(_translate("pdfForm", "Имя исходного файла:"))
        self.btnSelectFile.setText(_translate("pdfForm", "Выбрать файл"))
        self.groupBox_3.setTitle(_translate("pdfForm", "Что вы хотите сделать с файлом"))
        self.rbCopyPages.setText(_translate("pdfForm", "Скопировать страницу(ы) из файла"))
        self.rbDeletePages.setText(_translate("pdfForm", "Удалить страницу(ы) из файла"))
        self.rbCopyToCopy.setText(_translate("pdfForm", "Копировать страницу(ы) в другой файл"))
        self.lblNameFiletoCopy.setText(_translate("pdfForm", "Имя файла в который нужно скопировать страницы:"))
        self.btnSelectFileToCopy.setText(_translate("pdfForm", "Выбрать файл"))
        self.gbPages.setTitle(_translate("pdfForm", "Страницы"))
        self.lblSelectPages.setText(_translate("pdfForm", "Выбрать страницы исходного файла:"))
        self.rbDiapazon.setText(_translate("pdfForm", "Диапазон страниц"))
        self.rbNumberItem.setText(_translate("pdfForm", "Перечень страниц"))
        self.labelPages.setPlaceholderText(_translate("pdfForm", "Вводите диапазон страниц через дефис \"-\". Перечень - через запятую без пробелов."))
        self.lblFileToCopy.setText(_translate("pdfForm", "Страница, после которой добавить:"))
        self.gbDestinationFile.setTitle(_translate("pdfForm", "Сохранение"))
        self.lblSaveFile.setText(_translate("pdfForm", "Результат будет сохранён в той же папке, в файле:"))
        self.btnNewName.setText(_translate("pdfForm", "Переименовать"))
        self.btnRun.setText(_translate("pdfForm", "Выполнить"))
        self.btnCancel.setText(_translate("pdfForm", "Закрыть"))
        self.btnAbout.setText(_translate("pdfForm", "?"))