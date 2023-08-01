# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtn_principal.ui.'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_vtn_Principal(object):
    def setupUi(self, vtn_Principal):
        if not vtn_Principal.objectName():
            vtn_Principal.setObjectName(u"vtn_Principal")
        vtn_Principal.resize(400, 273)
        self.cb_tipo = QComboBox(vtn_Principal)
        self.cb_tipo.addItem("")
        self.cb_tipo.addItem("")
        self.cb_tipo.setObjectName(u"cb_tipo")
        self.cb_tipo.setGeometry(QRect(190, 20, 111, 22))
        self.lbl_tipo = QLabel(vtn_Principal)
        self.lbl_tipo.setObjectName(u"lbl_tipo")
        self.lbl_tipo.setGeometry(QRect(90, 20, 81, 20))
        self.txt_nombre = QLineEdit(vtn_Principal)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setGeometry(QRect(190, 60, 113, 20))
        self.txt_email = QLineEdit(vtn_Principal)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(190, 180, 113, 20))
        self.txt_cedula = QLineEdit(vtn_Principal)
        self.txt_cedula.setObjectName(u"txt_cedula")
        self.txt_cedula.setGeometry(QRect(190, 140, 113, 20))
        self.txt_apellido = QLineEdit(vtn_Principal)
        self.txt_apellido.setObjectName(u"txt_apellido")
        self.txt_apellido.setGeometry(QRect(190, 100, 113, 20))
        self.lbl_nombre = QLabel(vtn_Principal)
        self.lbl_nombre.setObjectName(u"lbl_nombre")
        self.lbl_nombre.setGeometry(QRect(130, 60, 47, 13))
        self.lbl_apellido = QLabel(vtn_Principal)
        self.lbl_apellido.setObjectName(u"lbl_apellido")
        self.lbl_apellido.setGeometry(QRect(130, 100, 47, 13))
        self.lbl_cedula = QLabel(vtn_Principal)
        self.lbl_cedula.setObjectName(u"lbl_cedula")
        self.lbl_cedula.setGeometry(QRect(130, 140, 47, 13))
        self.lbl_email = QLabel(vtn_Principal)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setGeometry(QRect(140, 180, 47, 13))
        self.btn_grabar = QPushButton(vtn_Principal)
        self.btn_grabar.setObjectName(u"btn_grabar")
        self.btn_grabar.setGeometry(QRect(150, 230, 75, 23))

        self.retranslateUi(vtn_Principal)

        QMetaObject.connectSlotsByName(vtn_Principal)
    # setupUi

    def retranslateUi(self, vtn_Principal):
        vtn_Principal.setWindowTitle(QCoreApplication.translate("vtn_Principal", u"Ingreso Personal", None))
        self.cb_tipo.setItemText(0, QCoreApplication.translate("vtn_Principal", u"Docente", None))
        self.cb_tipo.setItemText(1, QCoreApplication.translate("vtn_Principal", u"Estudiante", None))

        self.lbl_tipo.setText(QCoreApplication.translate("vtn_Principal", u"Tipo de persona", None))
        self.lbl_nombre.setText(QCoreApplication.translate("vtn_Principal", u"Nombre", None))
        self.lbl_apellido.setText(QCoreApplication.translate("vtn_Principal", u"Apellido", None))
        self.lbl_cedula.setText(QCoreApplication.translate("vtn_Principal", u"Cedula", None))
        self.lbl_email.setText(QCoreApplication.translate("vtn_Principal", u"Email", None))
        self.btn_grabar.setText(QCoreApplication.translate("vtn_Principal", u"Grabar", None))
    # retranslateUi

