# -*- coding: utf-8 -*-



# Form implementation generated from reading ui file 'dialog.ui'

#

# Created: Mon Nov 27 15:06:37 2017

#      by: pyside-uic 0.2.15 running on PySide 1.2.4

#

# WARNING! All changes made in this file will be lost!



from tank.platform.qt import QtCore, QtGui



class Ui_Dialog(object):

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")

        Dialog.resize(355, 210)

        self.gridLayout = QtGui.QGridLayout(Dialog)

        self.gridLayout.setObjectName("gridLayout")

        self.CIBtn = QtGui.QPushButton(Dialog)

        self.CIBtn.setObjectName("CIBtn")

        self.gridLayout.addWidget(self.CIBtn, 2, 0, 1, 1)

        self.COBtn = QtGui.QPushButton(Dialog)

        self.COBtn.setObjectName("COBtn")

        self.gridLayout.addWidget(self.COBtn, 2, 1, 1, 1)

        self.textBrowser = QtGui.QTextBrowser(Dialog)

        self.textBrowser.setObjectName("textBrowser")

        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 2)



        self.retranslateUi(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)



    def retranslateUi(self, Dialog):

        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "The Current Sgtk Environment", None, QtGui.QApplication.UnicodeUTF8))

        self.CIBtn.setText(QtGui.QApplication.translate("Dialog", "Check In", None, QtGui.QApplication.UnicodeUTF8))

        self.COBtn.setText(QtGui.QApplication.translate("Dialog", "Check Out", None, QtGui.QApplication.UnicodeUTF8))

        self.textBrowser.setHtml(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"

"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"

"p, li { white-space: pre-wrap; }\n"

"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"

"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))



from . import resources_rc

