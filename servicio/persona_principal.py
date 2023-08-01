from PySide6 import QtGui
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QMainWindow

from UI.vnt_principal import Ui_vtn_Principal
from dominio.docente import Docente
from dominio.estudiante import Estudiante


class PersonaPrincipal(QMainWindow):

    def __init__(self):
        super(PersonaPrincipal, self).__init__()
        self.ui = Ui_vtn_Principal()
        self.ui.setupUi(self)
        self.ui.btn_grabar.clicked.connect(self.grabar)
        self.ui.txt_cedula.setValidator(QtGui.QIntValidator())

        correo_exp = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b'
        validator = QRegularExpressionValidator(correo_exp, self)
        self.ui.txt_email.setValidator(validator)

    def grabar(self):
            tipo = self.ui.cb_tipo.currentText()
            if tipo == "Docente" :
                persona = Docente()
                persona.nombre = self.ui.txt_nombre.text()
                persona.apellido = self.ui.txt_apellido.text()
                persona.cedula = self.ui.txt_cedula.text()
                persona.email = self.ui.txt_email.text()

            if(self.ui.txt_nombre.text() == " " ):
                print("completar datos")
            if (self.ui.txt_apellido.text() == " "):
                print("completar datos")
            if (self.ui.txt_cedula.text() == " "):
                print("completar datos")
            elif(self.ui.txt_email.text() == " "):
                print("completar datos")

            else:
                persona = Estudiante()
                persona.nombre = self.ui.txt_nombre.text()
                persona.apellido = self.ui.txt_apellido.text()
                persona.cedula = self.ui.txt_cedula.text()
                persona.email = self.ui.txt_email.text()
            archivo = open("archivo.txt" , mode= "a")
            archivo.write(persona.__str__())
            archivo.write("\n")
            self.ui.txt_nombre.setText(" ")
            self.ui.txt_apellido.setText(" ")
            self.ui.txt_cedula.setText(" ")
            self.ui.txt_email.setText(" ")





