/********************************************************************************
** Form generated from reading UI file 'qttest1h11576.ui'
**
** Created by: Qt User Interface Compiler version 5.6.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef QTTEST1H11576_H
#define QTTEST1H11576_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionOpen;
    QAction *actionSave;
    QAction *actionInitialise;
    QAction *actionReset;
    QAction *actionDistance;
    QAction *actionSpeeds;
    QAction *actionAngles;
    QAction *actionProperties;
    QAction *actionPayload;
    QWidget *centralwidget;
    QGroupBox *groupBox;
    QRadioButton *rb_sat_rocket;
    QRadioButton *rb_sat_mars;
    QRadioButton *rb_sat_moon;
    QRadioButton *rb_sat_earth;
    QRadioButton *rb_sat_sun;
    QGroupBox *groupBox_2;
    QPushButton *pb_sim_start;
    QPushButton *pb_sim_stop;
    QPushButton *pb_sim_updatestate;
    QGroupBox *groupBox_3;
    QTextEdit *txted_time;
    QLabel *label;
    QLabel *label_2;
    QTextEdit *txted_timestep;
    QTextEdit *txted_saveinterval;
    QLabel *label_3;
    QGroupBox *groupBox_4;
    QLabel *label_4;
    QTextEdit *txted_x;
    QLabel *label_5;
    QLabel *label_6;
    QTextEdit *txted_y;
    QLabel *label_7;
    QTextEdit *txted_vy;
    QLabel *label_8;
    QLabel *label_9;
    QTextEdit *txted_vx;
    QLabel *label_10;
    QLabel *label_11;
    QTextEdit *txted_fy;
    QLabel *label_12;
    QLabel *label_13;
    QTextEdit *txted_fx;
    QLabel *label_14;
    QLabel *label_15;
    QMenuBar *menubar;
    QMenu *menuFile;
    QMenu *menuSimulation;
    QMenu *menuOrbitProperties;
    QMenu *menuRocket;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(593, 584);
        actionOpen = new QAction(MainWindow);
        actionOpen->setObjectName(QStringLiteral("actionOpen"));
        actionSave = new QAction(MainWindow);
        actionSave->setObjectName(QStringLiteral("actionSave"));
        actionInitialise = new QAction(MainWindow);
        actionInitialise->setObjectName(QStringLiteral("actionInitialise"));
        actionReset = new QAction(MainWindow);
        actionReset->setObjectName(QStringLiteral("actionReset"));
        actionDistance = new QAction(MainWindow);
        actionDistance->setObjectName(QStringLiteral("actionDistance"));
        actionSpeeds = new QAction(MainWindow);
        actionSpeeds->setObjectName(QStringLiteral("actionSpeeds"));
        actionAngles = new QAction(MainWindow);
        actionAngles->setObjectName(QStringLiteral("actionAngles"));
        actionProperties = new QAction(MainWindow);
        actionProperties->setObjectName(QStringLiteral("actionProperties"));
        actionPayload = new QAction(MainWindow);
        actionPayload->setObjectName(QStringLiteral("actionPayload"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        groupBox = new QGroupBox(centralwidget);
        groupBox->setObjectName(QStringLiteral("groupBox"));
        groupBox->setGeometry(QRect(420, 70, 120, 191));
        rb_sat_rocket = new QRadioButton(groupBox);
        rb_sat_rocket->setObjectName(QStringLiteral("rb_sat_rocket"));
        rb_sat_rocket->setGeometry(QRect(20, 90, 82, 17));
        rb_sat_mars = new QRadioButton(groupBox);
        rb_sat_mars->setObjectName(QStringLiteral("rb_sat_mars"));
        rb_sat_mars->setGeometry(QRect(20, 120, 82, 17));
        rb_sat_moon = new QRadioButton(groupBox);
        rb_sat_moon->setObjectName(QStringLiteral("rb_sat_moon"));
        rb_sat_moon->setGeometry(QRect(20, 60, 82, 17));
        rb_sat_earth = new QRadioButton(groupBox);
        rb_sat_earth->setObjectName(QStringLiteral("rb_sat_earth"));
        rb_sat_earth->setGeometry(QRect(20, 20, 82, 17));
        rb_sat_sun = new QRadioButton(groupBox);
        rb_sat_sun->setObjectName(QStringLiteral("rb_sat_sun"));
        rb_sat_sun->setGeometry(QRect(20, 150, 82, 17));
        groupBox_2 = new QGroupBox(centralwidget);
        groupBox_2->setObjectName(QStringLiteral("groupBox_2"));
        groupBox_2->setGeometry(QRect(430, 350, 121, 121));
        pb_sim_start = new QPushButton(groupBox_2);
        pb_sim_start->setObjectName(QStringLiteral("pb_sim_start"));
        pb_sim_start->setGeometry(QRect(20, 20, 75, 23));
        pb_sim_stop = new QPushButton(groupBox_2);
        pb_sim_stop->setObjectName(QStringLiteral("pb_sim_stop"));
        pb_sim_stop->setGeometry(QRect(20, 50, 75, 23));
        pb_sim_updatestate = new QPushButton(groupBox_2);
        pb_sim_updatestate->setObjectName(QStringLiteral("pb_sim_updatestate"));
        pb_sim_updatestate->setGeometry(QRect(20, 80, 75, 23));
        groupBox_3 = new QGroupBox(centralwidget);
        groupBox_3->setObjectName(QStringLiteral("groupBox_3"));
        groupBox_3->setGeometry(QRect(90, 320, 271, 181));
        txted_time = new QTextEdit(groupBox_3);
        txted_time->setObjectName(QStringLiteral("txted_time"));
        txted_time->setEnabled(false);
        txted_time->setGeometry(QRect(150, 30, 81, 31));
        label = new QLabel(groupBox_3);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(50, 30, 71, 16));
        label_2 = new QLabel(groupBox_3);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(40, 80, 101, 20));
        txted_timestep = new QTextEdit(groupBox_3);
        txted_timestep->setObjectName(QStringLiteral("txted_timestep"));
        txted_timestep->setEnabled(true);
        txted_timestep->setGeometry(QRect(150, 80, 81, 31));
        txted_saveinterval = new QTextEdit(groupBox_3);
        txted_saveinterval->setObjectName(QStringLiteral("txted_saveinterval"));
        txted_saveinterval->setEnabled(true);
        txted_saveinterval->setGeometry(QRect(150, 130, 81, 31));
        label_3 = new QLabel(groupBox_3);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setGeometry(QRect(40, 130, 101, 20));
        groupBox_4 = new QGroupBox(centralwidget);
        groupBox_4->setObjectName(QStringLiteral("groupBox_4"));
        groupBox_4->setGeometry(QRect(40, 50, 351, 231));
        label_4 = new QLabel(groupBox_4);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setGeometry(QRect(30, 50, 21, 16));
        txted_x = new QTextEdit(groupBox_4);
        txted_x->setObjectName(QStringLiteral("txted_x"));
        txted_x->setEnabled(false);
        txted_x->setGeometry(QRect(50, 40, 81, 31));
        label_5 = new QLabel(groupBox_4);
        label_5->setObjectName(QStringLiteral("label_5"));
        label_5->setGeometry(QRect(140, 50, 21, 16));
        label_6 = new QLabel(groupBox_4);
        label_6->setObjectName(QStringLiteral("label_6"));
        label_6->setGeometry(QRect(180, 50, 21, 16));
        txted_y = new QTextEdit(groupBox_4);
        txted_y->setObjectName(QStringLiteral("txted_y"));
        txted_y->setEnabled(false);
        txted_y->setGeometry(QRect(200, 40, 81, 31));
        label_7 = new QLabel(groupBox_4);
        label_7->setObjectName(QStringLiteral("label_7"));
        label_7->setGeometry(QRect(290, 50, 21, 16));
        txted_vy = new QTextEdit(groupBox_4);
        txted_vy->setObjectName(QStringLiteral("txted_vy"));
        txted_vy->setEnabled(false);
        txted_vy->setGeometry(QRect(200, 100, 81, 31));
        label_8 = new QLabel(groupBox_4);
        label_8->setObjectName(QStringLiteral("label_8"));
        label_8->setGeometry(QRect(30, 110, 21, 20));
        label_9 = new QLabel(groupBox_4);
        label_9->setObjectName(QStringLiteral("label_9"));
        label_9->setGeometry(QRect(180, 110, 21, 16));
        txted_vx = new QTextEdit(groupBox_4);
        txted_vx->setObjectName(QStringLiteral("txted_vx"));
        txted_vx->setEnabled(false);
        txted_vx->setGeometry(QRect(50, 100, 81, 31));
        label_10 = new QLabel(groupBox_4);
        label_10->setObjectName(QStringLiteral("label_10"));
        label_10->setGeometry(QRect(140, 110, 21, 16));
        label_11 = new QLabel(groupBox_4);
        label_11->setObjectName(QStringLiteral("label_11"));
        label_11->setGeometry(QRect(290, 110, 21, 16));
        txted_fy = new QTextEdit(groupBox_4);
        txted_fy->setObjectName(QStringLiteral("txted_fy"));
        txted_fy->setEnabled(true);
        txted_fy->setGeometry(QRect(200, 160, 81, 31));
        label_12 = new QLabel(groupBox_4);
        label_12->setObjectName(QStringLiteral("label_12"));
        label_12->setGeometry(QRect(30, 170, 21, 16));
        label_13 = new QLabel(groupBox_4);
        label_13->setObjectName(QStringLiteral("label_13"));
        label_13->setGeometry(QRect(180, 170, 21, 16));
        txted_fx = new QTextEdit(groupBox_4);
        txted_fx->setObjectName(QStringLiteral("txted_fx"));
        txted_fx->setEnabled(true);
        txted_fx->setGeometry(QRect(50, 160, 81, 31));
        label_14 = new QLabel(groupBox_4);
        label_14->setObjectName(QStringLiteral("label_14"));
        label_14->setGeometry(QRect(140, 170, 21, 16));
        label_15 = new QLabel(groupBox_4);
        label_15->setObjectName(QStringLiteral("label_15"));
        label_15->setGeometry(QRect(290, 170, 21, 16));
        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QStringLiteral("menubar"));
        menubar->setGeometry(QRect(0, 0, 593, 21));
        menuFile = new QMenu(menubar);
        menuFile->setObjectName(QStringLiteral("menuFile"));
        menuSimulation = new QMenu(menubar);
        menuSimulation->setObjectName(QStringLiteral("menuSimulation"));
        menuOrbitProperties = new QMenu(menubar);
        menuOrbitProperties->setObjectName(QStringLiteral("menuOrbitProperties"));
        menuRocket = new QMenu(menubar);
        menuRocket->setObjectName(QStringLiteral("menuRocket"));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QStringLiteral("statusbar"));
        MainWindow->setStatusBar(statusbar);

        menubar->addAction(menuFile->menuAction());
        menubar->addAction(menuSimulation->menuAction());
        menubar->addAction(menuOrbitProperties->menuAction());
        menubar->addAction(menuRocket->menuAction());
        menuFile->addAction(actionOpen);
        menuFile->addAction(actionSave);
        menuSimulation->addAction(actionInitialise);
        menuSimulation->addAction(actionReset);
        menuOrbitProperties->addAction(actionDistance);
        menuOrbitProperties->addAction(actionSpeeds);
        menuOrbitProperties->addAction(actionAngles);
        menuRocket->addAction(actionProperties);
        menuRocket->addAction(actionPayload);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", 0));
        actionOpen->setText(QApplication::translate("MainWindow", "Open", 0));
        actionSave->setText(QApplication::translate("MainWindow", "Save", 0));
        actionInitialise->setText(QApplication::translate("MainWindow", "Initialise", 0));
        actionReset->setText(QApplication::translate("MainWindow", "Reset", 0));
        actionDistance->setText(QApplication::translate("MainWindow", "distance", 0));
        actionSpeeds->setText(QApplication::translate("MainWindow", "speeds", 0));
        actionAngles->setText(QApplication::translate("MainWindow", "angles", 0));
        actionProperties->setText(QApplication::translate("MainWindow", "properties", 0));
        actionPayload->setText(QApplication::translate("MainWindow", "payload", 0));
        groupBox->setTitle(QApplication::translate("MainWindow", "Satellite", 0));
        rb_sat_rocket->setText(QApplication::translate("MainWindow", "Rocket", 0));
        rb_sat_mars->setText(QApplication::translate("MainWindow", "Mars", 0));
        rb_sat_moon->setText(QApplication::translate("MainWindow", "Moon", 0));
        rb_sat_earth->setText(QApplication::translate("MainWindow", "Earth", 0));
        rb_sat_sun->setText(QApplication::translate("MainWindow", "Sun", 0));
        groupBox_2->setTitle(QApplication::translate("MainWindow", "Sim Control", 0));
        pb_sim_start->setText(QApplication::translate("MainWindow", "Start", 0));
        pb_sim_stop->setText(QApplication::translate("MainWindow", "Stop", 0));
        pb_sim_updatestate->setText(QApplication::translate("MainWindow", "UpdateState", 0));
        groupBox_3->setTitle(QApplication::translate("MainWindow", "Time", 0));
        label->setText(QApplication::translate("MainWindow", "Time (hours)", 0));
        label_2->setText(QApplication::translate("MainWindow", "Time Step (sec)", 0));
        label_3->setText(QApplication::translate("MainWindow", "Save Interval", 0));
        groupBox_4->setTitle(QApplication::translate("MainWindow", "Satellite Co-ordinates", 0));
        label_4->setText(QApplication::translate("MainWindow", "x", 0));
        label_5->setText(QApplication::translate("MainWindow", "Mm", 0));
        label_6->setText(QApplication::translate("MainWindow", "y", 0));
        label_7->setText(QApplication::translate("MainWindow", "Mm", 0));
        label_8->setText(QApplication::translate("MainWindow", "vx", 0));
        label_9->setText(QApplication::translate("MainWindow", "vy", 0));
        label_10->setText(QApplication::translate("MainWindow", "km/s", 0));
        label_11->setText(QApplication::translate("MainWindow", "km/s", 0));
        label_12->setText(QApplication::translate("MainWindow", "Fx", 0));
        label_13->setText(QApplication::translate("MainWindow", "Fy", 0));
        label_14->setText(QApplication::translate("MainWindow", "N", 0));
        label_15->setText(QApplication::translate("MainWindow", "N", 0));
        menuFile->setTitle(QApplication::translate("MainWindow", "File", 0));
        menuSimulation->setTitle(QApplication::translate("MainWindow", "Simulation", 0));
        menuOrbitProperties->setTitle(QApplication::translate("MainWindow", "OrbitProperties", 0));
        menuRocket->setTitle(QApplication::translate("MainWindow", "rocket", 0));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // QTTEST1H11576_H
