# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qttest1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import payloaddlg as pldlg    #rocket payload dialog
import rpropertiesdlg as rprdlg   #rocket properties dialog
import opropanglesdlg as oangdlg  #orbit properties angle dialog
import opropspeeddlg as ospedlg  #orbit properties speed dialog
import opropdistdlg as odstdlg  #orbit properties dist dialog
import marsmission as mmc
import animmm as mma        #marstest animation class
import rocket as mmr

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(593, 584)
        self.infile="mmdata.txt"
        self.outfile="mmdata.txt"
        self.mm=mmc.marsmission()
        self.mr=mmr.rocket()

        self.amm=mma.animmm(self.mm)
        self.mm=self.amm.getmarsmission()
        self.mm.rocket=self.mr
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(420, 70, 120, 191))
        self.groupBox.setObjectName("groupBox")
        self.rb_sat_rocket = QtWidgets.QRadioButton(self.groupBox)
        self.rb_sat_rocket.setGeometry(QtCore.QRect(20, 90, 82, 17))
        self.rb_sat_rocket.setObjectName("rb_sat_rocket")
        self.rb_sat_mars = QtWidgets.QRadioButton(self.groupBox)
        self.rb_sat_mars.setGeometry(QtCore.QRect(20, 120, 82, 17))
        self.rb_sat_mars.setObjectName("rb_sat_mars")
        self.rb_sat_moon = QtWidgets.QRadioButton(self.groupBox)
        self.rb_sat_moon.setGeometry(QtCore.QRect(20, 60, 82, 17))
        self.rb_sat_moon.setObjectName("rb_sat_moon")
        self.rb_sat_earth = QtWidgets.QRadioButton(self.groupBox)
        self.rb_sat_earth.setGeometry(QtCore.QRect(20, 20, 82, 17))
        self.rb_sat_earth.setObjectName("rb_sat_earth")
        self.rb_sat_sun = QtWidgets.QRadioButton(self.groupBox)
        self.rb_sat_sun.setGeometry(QtCore.QRect(20, 150, 82, 17))
        self.rb_sat_sun.setObjectName("rb_sat_sun")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(430, 350, 121, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pb_sim_start = QtWidgets.QPushButton(self.groupBox_2)
        self.pb_sim_start.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.pb_sim_start.setObjectName("pb_sim_start")
        self.pb_sim_stop = QtWidgets.QPushButton(self.groupBox_2)
        self.pb_sim_stop.setGeometry(QtCore.QRect(20, 50, 75, 23))
        self.pb_sim_stop.setObjectName("pb_sim_stop")
        self.pb_sim_updatestate = QtWidgets.QPushButton(self.groupBox_2)
        self.pb_sim_updatestate.setGeometry(QtCore.QRect(20, 80, 75, 23))
        self.pb_sim_updatestate.setObjectName("pb_sim_updatestate")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(90, 320, 271, 181))
        self.groupBox_3.setObjectName("groupBox_3")
        self.txted_time = QtWidgets.QTextEdit(self.groupBox_3)
        self.txted_time.setEnabled(False)
        self.txted_time.setGeometry(QtCore.QRect(150, 30, 81, 31))
        self.txted_time.setObjectName("txted_time")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(50, 30, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 101, 20))
        self.label_2.setObjectName("label_2")
        self.txted_timestep = QtWidgets.QTextEdit(self.groupBox_3)
        self.txted_timestep.setEnabled(True)
        self.txted_timestep.setGeometry(QtCore.QRect(150, 80, 81, 31))
        self.txted_timestep.setObjectName("txted_timestep")
        self.txted_timestep.setText("0")
        self.txted_saveinterval = QtWidgets.QTextEdit(self.groupBox_3)
        self.txted_saveinterval.setEnabled(True)
        self.txted_saveinterval.setGeometry(QtCore.QRect(150, 130, 81, 31))
        self.txted_saveinterval.setObjectName("txted_saveinterval")
        self.txted_saveinterval.setText("0")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 101, 20))
        self.label_3.setObjectName("label_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(40, 50, 351, 231))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(30, 50, 21, 16))
        self.label_4.setObjectName("label_4")
        self.txted_x = QtWidgets.QTextEdit(self.groupBox_4)
        self.txted_x.setEnabled(False)
        self.txted_x.setGeometry(QtCore.QRect(50, 40, 81, 31))
        self.txted_x.setObjectName("txted_x")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(140, 50, 21, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(180, 50, 21, 16))
        self.label_6.setObjectName("label_6")
        self.txted_y = QtWidgets.QTextEdit(self.groupBox_4)
        self.txted_y.setEnabled(False)
        self.txted_y.setGeometry(QtCore.QRect(200, 40, 81, 31))
        self.txted_y.setObjectName("txted_y")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(290, 50, 21, 16))
        self.label_7.setObjectName("label_7")
        self.txted_vy = QtWidgets.QTextEdit(self.groupBox_4)
        self.txted_vy.setEnabled(False)
        self.txted_vy.setGeometry(QtCore.QRect(200, 100, 81, 31))
        self.txted_vy.setObjectName("txted_vy")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(30, 110, 21, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(180, 110, 21, 16))
        self.label_9.setObjectName("label_9")
        self.txted_vx = QtWidgets.QTextEdit(self.groupBox_4)
        self.txted_vx.setEnabled(False)
        self.txted_vx.setGeometry(QtCore.QRect(50, 100, 81, 31))
        self.txted_vx.setObjectName("txted_vx")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(140, 110, 21, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(290, 110, 21, 16))
        self.label_11.setObjectName("label_11")
        self.txted_fy = QtWidgets.QTextEdit(self.groupBox_4)
        self.txted_fy.setEnabled(True)
        self.txted_fy.setGeometry(QtCore.QRect(200, 160, 81, 31))
        self.txted_fy.setObjectName("txted_fy")
        self.txted_fy.setText("0")
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(30, 170, 21, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label_13.setGeometry(QtCore.QRect(180, 170, 21, 16))
        self.label_13.setObjectName("label_13")
        self.txted_fx = QtWidgets.QTextEdit(self.groupBox_4)
        self.txted_fx.setEnabled(True)
        self.txted_fx.setGeometry(QtCore.QRect(50, 160, 81, 31))
        self.txted_fx.setObjectName("txted_fx")
        self.txted_fx.setText("0")
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(140, 170, 21, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setGeometry(QtCore.QRect(290, 170, 21, 16))
        self.label_15.setObjectName("label_15")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 593, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSimulation = QtWidgets.QMenu(self.menubar)
        self.menuSimulation.setObjectName("menuSimulation")
        self.menuOrbitProperties = QtWidgets.QMenu(self.menubar)
        self.menuOrbitProperties.setObjectName("menuOrbitProperties")
        self.menuRocket = QtWidgets.QMenu(self.menubar)
        self.menuRocket.setObjectName("menuRocket")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionInitialise = QtWidgets.QAction(MainWindow)
        self.actionInitialise.setObjectName("actionInitialise")
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.actionDistance = QtWidgets.QAction(MainWindow)
        self.actionDistance.setObjectName("actionDistance")
        self.actionSpeeds = QtWidgets.QAction(MainWindow)
        self.actionSpeeds.setObjectName("actionSpeeds")
        self.actionAngles = QtWidgets.QAction(MainWindow)
        self.actionAngles.setObjectName("actionAngles")
        self.actionProperties = QtWidgets.QAction(MainWindow)
        self.actionProperties.setObjectName("actionProperties")
        self.actionPayload = QtWidgets.QAction(MainWindow)
        self.actionPayload.setObjectName("actionPayload")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuSimulation.addAction(self.actionInitialise)
        self.menuSimulation.addAction(self.actionReset)
        self.menuOrbitProperties.addAction(self.actionDistance)
        self.menuOrbitProperties.addAction(self.actionSpeeds)
        self.menuOrbitProperties.addAction(self.actionAngles)
        self.menuRocket.addAction(self.actionProperties)
        self.menuRocket.addAction(self.actionPayload)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSimulation.menuAction())
        self.menubar.addAction(self.menuOrbitProperties.menuAction())
        self.menubar.addAction(self.menuRocket.menuAction())
        
        self.pb_sim_start.clicked.connect(self.pb_sim_start_clicked)
        self.pb_sim_stop.clicked.connect(self.pb_sim_stop_clicked)
        self.pb_sim_updatestate.clicked.connect(self.pb_sim_updatestate_clicked)

        self.rb_sat_earth.clicked.connect(self.rb_sat_earth_clicked)
        self.rb_sat_moon.clicked.connect(self.rb_sat_moon_clicked)
        self.rb_sat_rocket.clicked.connect(self.rb_sat_rocket_clicked)
        self.rb_sat_mars.clicked.connect(self.rb_sat_mars_clicked)        
        self.rb_sat_sun.clicked.connect(self.rb_sat_sun_clicked)
        
        self.actionOpen.triggered.connect(self.actionopen_clicked)
        self.actionSave.triggered.connect(self.actionsave_clicked)
        self.actionInitialise.triggered.connect(self.actioninitialise_clicked)
        self.actionReset.triggered.connect(self.actionreset_clicked)
        self.actionDistance.triggered.connect(self.actiondistance_clicked)
        self.actionSpeeds.triggered.connect(self.actionspeeds_clicked)
        self.actionAngles.triggered.connect(self.actionangles_clicked)
        self.actionProperties.triggered.connect(self.actionproperties_clicked)
        self.actionPayload.triggered.connect(self.actionpayload_clicked)



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Satellite"))
        self.rb_sat_rocket.setText(_translate("MainWindow", "Rocket"))
        self.rb_sat_mars.setText(_translate("MainWindow", "Mars"))
        self.rb_sat_moon.setText(_translate("MainWindow", "Moon"))
        self.rb_sat_earth.setText(_translate("MainWindow", "Earth"))
        self.rb_sat_sun.setText(_translate("MainWindow", "Sun"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Sim Control"))
        self.pb_sim_start.setText(_translate("MainWindow", "Start"))
        self.pb_sim_stop.setText(_translate("MainWindow", "Stop"))
        self.pb_sim_updatestate.setText(_translate("MainWindow", "UpdateState"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Time"))
        self.label.setText(_translate("MainWindow", "Time (days)"))
        self.label_2.setText(_translate("MainWindow", "Time Step (sec)"))
        self.label_3.setText(_translate("MainWindow", "Save Interval"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Satellite Co-ordinates"))
        self.label_4.setText(_translate("MainWindow", "x"))
        self.label_5.setText(_translate("MainWindow", "Mm"))
        self.label_6.setText(_translate("MainWindow", "y"))
        self.label_7.setText(_translate("MainWindow", "Mm"))
        self.label_8.setText(_translate("MainWindow", "vx"))
        self.label_9.setText(_translate("MainWindow", "vy"))
        self.label_10.setText(_translate("MainWindow", "km/s"))
        self.label_11.setText(_translate("MainWindow", "km/s"))
        self.label_12.setText(_translate("MainWindow", "Fx"))
        self.label_13.setText(_translate("MainWindow", "Fy"))
        self.label_14.setText(_translate("MainWindow", "kN"))
        self.label_15.setText(_translate("MainWindow", "kN"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSimulation.setTitle(_translate("MainWindow", "Simulation"))
        self.menuOrbitProperties.setTitle(_translate("MainWindow", "OrbitProperties"))
        self.menuRocket.setTitle(_translate("MainWindow", "rocket"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionInitialise.setText(_translate("MainWindow", "Initialise"))
        self.actionReset.setText(_translate("MainWindow", "Reset"))
        self.actionDistance.setText(_translate("MainWindow", "distance"))
        self.actionSpeeds.setText(_translate("MainWindow", "speeds"))
        self.actionAngles.setText(_translate("MainWindow", "angles"))
        self.actionProperties.setText(_translate("MainWindow", "properties"))
        self.actionPayload.setText(_translate("MainWindow", "payload"))

    def pb_sim_start_clicked(self):
            print('start clicked')
            self.amm.startanimation()
	
    def pb_sim_stop_clicked(self):
            print('stop clicked')
		
    def pb_sim_updatestate_clicked(self):
            print('updatestate clicked')
            self.mm.control[mmc.ctl.FX]=1000*float(self.txted_fx.toPlainText())
            self.mm.control[mmc.ctl.FY]=1000*float(self.txted_fy.toPlainText())
            
            self.mm.control[mmc.ctl.DT]=float(self.txted_timestep.toPlainText())
            self.mm.control[mmc.ctl.SINT]=float(self.txted_saveinterval.toPlainText())
            #self.txted_fx.toPlainText()
            #print(self.txted_fx.toPlainText())
            self.txted_time.setText(str(format(self.mm.state[mmc.st.T]/(3600*24),'3f')))

    def rb_sat_earth_clicked(self):
            print('earth clicked')
            #self.txted_x.setText("1.0")
            self.sat_select='earth'
            self.update_satcoords(self.sat_select)
            
    def rb_sat_moon_clicked(self):
            print('moon clicked')
            self.sat_select='moon'
            self.update_satcoords(self.sat_select)
            
    def rb_sat_rocket_clicked(self):
            print('rocket clicked')
            self.sat_select='rocket'
            self.update_satcoords(self.sat_select)
            
    def rb_sat_mars_clicked(self):
            print('mars clicked')
            self.sat_select='mars'
            self.update_satcoords(self.sat_select)
            
    def rb_sat_sun_clicked(self):
            print('sun clicked')
            self.sat_select='sun'
            self.update_satcoords(self.sat_select)
            
    def actionopen_clicked(self):
            print('actionopen_clicked clicked')
            self.mm.loadmission(self.infile)
            
    def actionsave_clicked(self):
            print('actionsave_clicked clicked')
            self.mm.savemission(self.outfile)
            
    def actioninitialise_clicked(self):
            print('actioninitialise_clicked clicked') 
            self.mm=mmc.marsmission()
            self.mr=mmr.rocket()

            self.amm=mma.animmm(self.mm)
            self.mm=self.amm.getmarsmission()
            self.mm.rocket=self.mr
            
    def actionreset_clicked(self):
            print('actionreset_clicked clicked')
            self.mm=mmc.marsmission()
            self.mr=mmr.rocket()

            self.amm=mma.animmm(self.mm)
            self.mm=self.amm.getmarsmission()
            self.mm.rocket=self.mr

    def actiondistance_clicked(self):
            print('actiondistance_clicked clicked')
            Dialog = QtWidgets.QDialog()
            ui = odstdlg.Ui_Distance()
            ui.setupUi(Dialog)
            ui.setmm(self.mm, self.mr,self.sat_select)
            #Dialog.show()
            Dialog.exec_()
            
    def actionspeeds_clicked(self):
            print('actionspeeds_clicked clicked')
            Dialog = QtWidgets.QDialog()
            ui = ospedlg.Ui_Dialog()
            ui.setupUi(Dialog)
            ui.setmm(self.mm, self.mr,self.sat_select)
            #Dialog.show()
            Dialog.exec_()
            
    def actionangles_clicked(self):
            print('actionangles_clicked clicked')
            Dialog = QtWidgets.QDialog()
            ui = oangdlg.Ui_OrbitalAngle()
            ui.setupUi(Dialog)
            ui.setmm(self.mm, self.mr,self.sat_select)
            #Dialog.show()
            Dialog.exec_()
            
    def actionproperties_clicked(self):
            print('actionproperties_clicked clicked')
            Dialog = QtWidgets.QDialog()
            ui = rprdlg.Ui_Dialog()
            ui.setupUi(Dialog)
            ui.setmm(self.mm, self.mr)
            #Dialog.show()
            Dialog.exec_()
            
    def actionpayload_clicked(self):
            print('actionpayload_clicked clicked')
            #self.payloaddlg=pldlg.Ui_Dialog
            #self.payloaddlg.
            Dialog = QtWidgets.QDialog()
            ui = pldlg.Ui_Dialog()
            ui.setupUi(Dialog)
            ui.setmm(self.mm, self.mr)
            #Dialog.show()
            Dialog.exec_()
            
    def update_satcoords(self,sat_select):

            if sat_select=='earth':
                xc=self.mm.state[mmc.st.XE]
                yc=self.mm.state[mmc.st.YE]
                vxc=self.mm.state[mmc.st.VXE]
                vyc=self.mm.state[mmc.st.VYE]
                fxc=self.mm.control[mmc.ctl.FX]
                fyc=self.mm.control[mmc.ctl.FY]               
            elif sat_select=='moon':
                xc=self.mm.state[mmc.st.XM]
                yc=self.mm.state[mmc.st.YM]
                vxc=self.mm.state[mmc.st.VXM]
                vyc=self.mm.state[mmc.st.VYM]
                fxc=self.mm.control[mmc.ctl.FX]
                fyc=self.mm.control[mmc.ctl.FY] 
            elif sat_select=='sun':
                xc=self.mm.state[mmc.st.XS]
                yc=self.mm.state[mmc.st.YS]
                vxc=self.mm.state[mmc.st.VXS]
                vyc=self.mm.state[mmc.st.VYS]
                fxc=self.mm.control[mmc.ctl.FX]
                fyc=self.mm.control[mmc.ctl.FY] 
            elif sat_select=='rocket':
                xc=self.mm.state[mmc.st.X]
                yc=self.mm.state[mmc.st.Y]
                vxc=self.mm.state[mmc.st.VX]
                vyc=self.mm.state[mmc.st.VY]
                fxc=self.mm.control[mmc.ctl.FX]
                fyc=self.mm.control[mmc.ctl.FY]                 
            elif sat_select=='mars':
                xc=self.mm.state[mmc.st.XMA]
                yc=self.mm.state[mmc.st.YMA]
                vxc=self.mm.state[mmc.st.VXMA]
                vyc=self.mm.state[mmc.st.VYMA]
                fxc=self.mm.control[mmc.ctl.FX]
                fyc=self.mm.control[mmc.ctl.FY]              
            else:
                xc=0.0
                yc=0.0
                vxc=0.0
                vyc=0.0
                fxc=0.0
                fyc=0.0
               
            xc=xc/1.0e6
            yc=yc/1.0e6
            vxc=vxc/1.0e3
            vyc=vyc/1.0e3            
            self.txted_x.setText(str(format(xc,'.3f')))
            self.txted_y.setText(str(format(yc,'.3f')))
            self.txted_vx.setText(str(format(vxc,'.3f')))
            self.txted_vy.setText(str(format(vyc,'.3f')))
            self.txted_fx.setText(str(format(fxc/1000,'.3f')))
            self.txted_fy.setText(str(format(fyc/1000,'.3f')))
            
            
            




		
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

