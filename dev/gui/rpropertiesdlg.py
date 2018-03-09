# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rpropertiesdlg.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(373, 296)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 311, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 30, 311, 191))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 71, 16))
        self.label.setObjectName("label")
        self.txted_mass = QtWidgets.QTextEdit(self.groupBox)
        self.txted_mass.setEnabled(False)
        self.txted_mass.setGeometry(QtCore.QRect(130, 30, 101, 31))
        self.txted_mass.setObjectName("txted_mass")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(250, 40, 31, 16))
        self.label_2.setObjectName("label_2")
        self.txted_nrock = QtWidgets.QTextEdit(self.groupBox)
        self.txted_nrock.setEnabled(False)
        self.txted_nrock.setGeometry(QtCore.QRect(130, 80, 101, 31))
        self.txted_nrock.setObjectName("txted_nrock")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(250, 90, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 101, 16))
        self.label_4.setObjectName("label_4")
        self.txted_powerrock = QtWidgets.QTextEdit(self.groupBox)
        self.txted_powerrock.setEnabled(False)
        self.txted_powerrock.setGeometry(QtCore.QRect(130, 130, 101, 31))
        self.txted_powerrock.setObjectName("txted_powerrock")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(250, 140, 31, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 140, 101, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Rocket Properties"))
        self.groupBox.setTitle(_translate("Dialog", "Rocket Properties"))
        self.label.setText(_translate("Dialog", "Mass"))
        self.label_2.setText(_translate("Dialog", "kg"))
        self.label_3.setText(_translate("Dialog", "km/s"))
        self.label_4.setText(_translate("Dialog", "Number of Rockets"))
        self.label_5.setText(_translate("Dialog", "N"))
        self.label_6.setText(_translate("Dialog", "Power per Rocket"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

