# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtn_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_vtn_principal(object):
    def setupUi(self, vtn_principal):
        if not vtn_principal.objectName():
            vtn_principal.setObjectName(u"vtn_principal")
        vtn_principal.resize(484, 378)
        self.centralwidget = QWidget(vtn_principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line_nombre = QLineEdit(self.centralwidget)
        self.line_nombre.setObjectName(u"line_nombre")
        self.line_nombre.setGeometry(QRect(190, 80, 113, 20))
        self.line_nombre.setMaxLength(50)
        self.line_apellido = QLineEdit(self.centralwidget)
        self.line_apellido.setObjectName(u"line_apellido")
        self.line_apellido.setGeometry(QRect(190, 110, 113, 20))
        self.line_apellido.setMaxLength(50)
        self.lbl_Nombre = QLabel(self.centralwidget)
        self.lbl_Nombre.setObjectName(u"lbl_Nombre")
        self.lbl_Nombre.setGeometry(QRect(130, 80, 51, 16))
        self.lbl_Apellido = QLabel(self.centralwidget)
        self.lbl_Apellido.setObjectName(u"lbl_Apellido")
        self.lbl_Apellido.setGeometry(QRect(130, 110, 51, 16))
        self.pBtton_Grabar = QPushButton(self.centralwidget)
        self.pBtton_Grabar.setObjectName(u"pBtton_Grabar")
        self.pBtton_Grabar.setGeometry(QRect(190, 220, 75, 23))
        self.cb_tipo_persona = QComboBox(self.centralwidget)
        self.cb_tipo_persona.addItem("")
        self.cb_tipo_persona.addItem("")
        self.cb_tipo_persona.setObjectName(u"cb_tipo_persona")
        self.cb_tipo_persona.setGeometry(QRect(190, 20, 121, 21))
        self.lbl_tipo_persona = QLabel(self.centralwidget)
        self.lbl_tipo_persona.setObjectName(u"lbl_tipo_persona")
        self.lbl_tipo_persona.setGeometry(QRect(130, 20, 51, 16))
        self.lbl_cedula = QLabel(self.centralwidget)
        self.lbl_cedula.setObjectName(u"lbl_cedula")
        self.lbl_cedula.setGeometry(QRect(130, 140, 51, 16))
        self.lbl_correo = QLabel(self.centralwidget)
        self.lbl_correo.setObjectName(u"lbl_correo")
        self.lbl_correo.setGeometry(QRect(130, 170, 51, 16))
        self.line_cedula = QLineEdit(self.centralwidget)
        self.line_cedula.setObjectName(u"line_cedula")
        self.line_cedula.setGeometry(QRect(190, 140, 113, 20))
        self.line_cedula.setMaxLength(10)
        self.line_email = QLineEdit(self.centralwidget)
        self.line_email.setObjectName(u"line_email")
        self.line_email.setGeometry(QRect(190, 170, 113, 20))
        self.line_email.setMaxLength(100)
        self.pBtton_buscar_cedula = QPushButton(self.centralwidget)
        self.pBtton_buscar_cedula.setObjectName(u"pBtton_buscar_cedula")
        self.pBtton_buscar_cedula.setGeometry(QRect(350, 140, 101, 23))
        vtn_principal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(vtn_principal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 484, 21))
        vtn_principal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(vtn_principal)
        self.statusbar.setObjectName(u"statusbar")
        vtn_principal.setStatusBar(self.statusbar)

        self.retranslateUi(vtn_principal)

        QMetaObject.connectSlotsByName(vtn_principal)
    # setupUi

    def retranslateUi(self, vtn_principal):
        vtn_principal.setWindowTitle(QCoreApplication.translate("vtn_principal", u"vtn_principal", None))
        self.lbl_Nombre.setText(QCoreApplication.translate("vtn_principal", u"Nombre", None))
        self.lbl_Apellido.setText(QCoreApplication.translate("vtn_principal", u"Apellido", None))
        self.pBtton_Grabar.setText(QCoreApplication.translate("vtn_principal", u"Grabar", None))
        self.cb_tipo_persona.setItemText(0, QCoreApplication.translate("vtn_principal", u"Docente", None))
        self.cb_tipo_persona.setItemText(1, QCoreApplication.translate("vtn_principal", u"Estudiante", None))

        self.lbl_tipo_persona.setText(QCoreApplication.translate("vtn_principal", u"Tipo", None))
        self.lbl_cedula.setText(QCoreApplication.translate("vtn_principal", u"Cedula", None))
        self.lbl_correo.setText(QCoreApplication.translate("vtn_principal", u"Email", None))
        self.pBtton_buscar_cedula.setText(QCoreApplication.translate("vtn_principal", u"buscar por cedula", None))
    # retranslateUi

