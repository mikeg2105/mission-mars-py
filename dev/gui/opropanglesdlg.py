# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'opropanglesdlg.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OrbitalAngle(object):
    def setupUi(self, OrbitalAngle):
        OrbitalAngle.setObjectName("OrbitalAngle")
        OrbitalAngle.resize(400, 233)
        self.buttonBox = QtWidgets.QDialogButtonBox(OrbitalAngle)
        self.buttonBox.setGeometry(QtCore.QRect(30, 170, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(OrbitalAngle)
        self.groupBox.setGeometry(QtCore.QRect(50, 40, 341, 101))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 50, 71, 16))
        self.label.setObjectName("label")
        self.txted_angle = QtWidgets.QTextEdit(self.groupBox)
        self.txted_angle.setEnabled(False)
        self.txted_angle.setGeometry(QtCore.QRect(160, 40, 101, 31))
        self.txted_angle.setObjectName("txted_angle")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(280, 50, 51, 16))
        self.label_2.setObjectName("label_2")
        self.txted_sat = QtWidgets.QTextEdit(self.groupBox)
        self.txted_sat.setEnabled(False)
        self.txted_sat.setGeometry(QtCore.QRect(80, 40, 71, 31))
        self.txted_sat.setObjectName("txted_sat")

        self.retranslateUi(OrbitalAngle)
        self.buttonBox.accepted.connect(OrbitalAngle.accept)
        self.buttonBox.rejected.connect(OrbitalAngle.reject)
        QtCore.QMetaObject.connectSlotsByName(OrbitalAngle)

    def retranslateUi(self, OrbitalAngle):
        _translate = QtCore.QCoreApplication.translate
        OrbitalAngle.setWindowTitle(_translate("OrbitalAngle", "Orbital Angle"))
        self.groupBox.setTitle(_translate("OrbitalAngle", "Orbital Angle"))
        self.label.setText(_translate("OrbitalAngle", "Orbital angle"))
        self.label_2.setText(_translate("OrbitalAngle", "degrees"))
        self.txted_sat.setHtml(_translate("OrbitalAngle", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">satellite</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OrbitalAngle = QtWidgets.QDialog()
    ui = Ui_OrbitalAngle()
    ui.setupUi(OrbitalAngle)
    OrbitalAngle.show()
    sys.exit(app.exec_())

