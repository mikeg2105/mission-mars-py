# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'opropspeeddlg.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import marsmission as mmc
import rocket as mmr

class Ui_Dialog(object):
    mm=[]
    mr=[]
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 335)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 280, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 30, 311, 231))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 90, 71, 16))
        self.label.setObjectName("label")
        self.txted_speed = QtWidgets.QTextEdit(self.groupBox)
        self.txted_speed.setEnabled(False)
        self.txted_speed.setGeometry(QtCore.QRect(130, 80, 101, 31))
        self.txted_speed.setObjectName("txted_speed")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(250, 90, 31, 16))
        self.label_2.setObjectName("label_2")
        self.txted_sat = QtWidgets.QTextEdit(self.groupBox)
        self.txted_sat.setEnabled(False)
        self.txted_sat.setGeometry(QtCore.QRect(20, 30, 71, 31))
        self.txted_sat.setObjectName("txted_sat")
        self.txted_relspeed = QtWidgets.QTextEdit(self.groupBox)
        self.txted_relspeed.setEnabled(False)
        self.txted_relspeed.setGeometry(QtCore.QRect(130, 130, 101, 31))
        self.txted_relspeed.setObjectName("txted_relspeed")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(250, 140, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(40, 140, 71, 16))
        self.label_4.setObjectName("label_4")
        self.txted_orbspeed = QtWidgets.QTextEdit(self.groupBox)
        self.txted_orbspeed.setEnabled(False)
        self.txted_orbspeed.setGeometry(QtCore.QRect(130, 180, 101, 31))
        self.txted_orbspeed.setObjectName("txted_orbspeed")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(250, 190, 31, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(40, 190, 71, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Orbital Speed"))
        self.groupBox.setTitle(_translate("Dialog", "Rocket Orbital Speeds"))
        self.label.setText(_translate("Dialog", "Speed"))
        self.label_2.setText(_translate("Dialog", "km/s"))
        self.txted_sat.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">satellite</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "km/s"))
        self.label_4.setText(_translate("Dialog", "Relative speed"))
        self.label_5.setText(_translate("Dialog", "km/s"))
        self.label_6.setText(_translate("Dialog", "Orbital speed"))
        
    def setmm(self, mm,mr,sat_select):
        self.mm=mm
        self.mr=mr

        xc=0.0
        yc=0.0
        vxc=0.0
        vyc=0.0
        
        if sat_select=='earth':
            xc=self.mm.state[mmc.st.XE]
            yc=self.mm.state[mmc.st.YE]
            vxc=self.mm.state[mmc.st.VXE]
            vyc=self.mm.state[mmc.st.VYE] 
            mass=self.mm.const[mmc.cnst.ME]
        elif sat_select=='moon':
            xc=self.mm.state[mmc.st.XM]
            yc=self.mm.state[mmc.st.YM]
            vxc=self.mm.state[mmc.st.VXM]
            vyc=self.mm.state[mmc.st.VYM] 
            mass=self.mm.const[mmc.cnst.MM]
        elif sat_select=='sun':
            xc=self.mm.state[mmc.st.XS]
            yc=self.mm.state[mmc.st.YS]
            vxc=self.mm.state[mmc.st.VXS]
            vyc=self.mm.state[mmc.st.VYS]
            mass=self.mm.const[mmc.cnst.MS]
        elif sat_select=='rocket':
            xc=self.mm.state[mmc.st.X]
            yc=self.mm.state[mmc.st.Y]
            vxc=self.mm.state[mmc.st.VX]
            vyc=self.mm.state[mmc.st.VY]
            mass=self.mr.updatemass()
        elif sat_select=='mars':
            xc=self.mm.state[mmc.st.XMA]
            yc=self.mm.state[mmc.st.YMA]
            vxc=self.mm.state[mmc.st.VXMA]
            vyc=self.mm.state[mmc.st.VYMA]
            mass=self.mm.const[mmc.cnst.MMARS]            
        else:
            xc=0.0
            yc=0.0
            vxc=0.0
            vyc=0.0

        orbspeed={}
        orbspeed=mm.orbitalspeed(self.mm.state[mmc.st.X],self.mm.state[mmc.st.Y], self.mm.state[mmc.st.VX], self.mm.state[mmc.st.VY],xc,yc,vxc,vyc,mass)
        self.txted_sat.setText(sat_select)	
        self.txted_speed.setText(str(format(orbspeed[0]/1e3,'.3f')))
        self.txted_orbspeed.setText(str(format(orbspeed[1]/1e3,'.3f')))
        self.txted_relspeed.setText(str(format(orbspeed[2]/1e3,'.3f')))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

