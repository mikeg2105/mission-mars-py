# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'opropdistdlg.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import marsmission as mmc
import rocket as mmr

class Ui_Distance(object):
    mm=[]
    mr=[]
    def setupUi(self, Distance):
        Distance.setObjectName("Distance")
        Distance.resize(396, 176)
        self.buttonBox = QtWidgets.QDialogButtonBox(Distance)
        self.buttonBox.setGeometry(QtCore.QRect(30, 130, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(Distance)
        self.groupBox.setGeometry(QtCore.QRect(39, 19, 311, 101))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 50, 71, 16))
        self.label.setObjectName("label")
        self.txted_dist = QtWidgets.QTextEdit(self.groupBox)
        self.txted_dist.setGeometry(QtCore.QRect(160, 40, 101, 31))
        self.txted_dist.setObjectName("txted_dist")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(280, 50, 31, 16))
        self.label_2.setObjectName("label_2")
        self.txted_sat = QtWidgets.QTextEdit(self.groupBox)
        self.txted_sat.setEnabled(False)
        self.txted_sat.setGeometry(QtCore.QRect(80, 40, 71, 31))
        self.txted_sat.setObjectName("txted_sat")

        self.retranslateUi(Distance)
        self.buttonBox.accepted.connect(Distance.accept)
        self.buttonBox.rejected.connect(Distance.reject)
        QtCore.QMetaObject.connectSlotsByName(Distance)

    def retranslateUi(self, Distance):
        _translate = QtCore.QCoreApplication.translate
        Distance.setWindowTitle(_translate("Distance", "Distance"))
        self.groupBox.setTitle(_translate("Distance", "Rocket Distance"))
        self.label.setText(_translate("Distance", "Distance from"))
        self.label_2.setText(_translate("Distance", "Mm"))
        self.txted_sat.setHtml(_translate("Distance", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">satellite</span></p></body></html>"))


    def setmm(self, mm,mr,sat_select):
        self.mm=mm
        self.mr=mr
        xc=0.0
        yc=0.0
        if sat_select=='earth':
            xc=self.mm.state[mmc.st.XE]
            yc=self.mm.state[mmc.st.YE]           
        elif sat_select=='moon':
            xc=self.mm.state[mmc.st.XM]
            yc=self.mm.state[mmc.st.YM]
        elif sat_select=='sun':
            xc=self.mm.state[mmc.st.XS]
            yc=self.mm.state[mmc.st.YS]
        elif sat_select=='rocket':
            xc=self.mm.state[mmc.st.X]
            yc=self.mm.state[mmc.st.Y]             
        elif sat_select=='mars':
            xc=self.mm.state[mmc.st.XMA]
            yc=self.mm.state[mmc.st.YMA]             
        else:
            xc=0.0
            yc=0.0
            
        sep=mm.dist(xc, yc, self.mm.state[mmc.st.X] , self.mm.state[mmc.st.Y])/1.0e6
        self.txted_sat.setText(sat_select)	
        self.txted_dist.setText(str(format(sep,'.3f')))	

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Distance = QtWidgets.QDialog()
    ui = Ui_Distance()
    ui.setupUi(Distance)
    Distance.show()
    sys.exit(app.exec_())

