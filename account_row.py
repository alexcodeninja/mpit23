# Form implementation generated from reading ui file '.\account_row.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(688, 60)
        Form.setStyleSheet("font: 12pt \"Roboto\";")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_comp_name = QtWidgets.QLabel(parent=self.frame)
        self.lbl_comp_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_comp_name.setObjectName("lbl_comp_name")
        self.verticalLayout_3.addWidget(self.lbl_comp_name)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_name = QtWidgets.QLabel(parent=self.frame_2)
        self.lbl_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_name.setObjectName("lbl_name")
        self.verticalLayout_2.addWidget(self.lbl_name)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(parent=Form)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_logo = QtWidgets.QLabel(parent=self.frame_3)
        self.lbl_logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_logo.setObjectName("lbl_logo")
        self.verticalLayout.addWidget(self.lbl_logo)
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(parent=Form)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lbl_login_password = QtWidgets.QLabel(parent=self.frame_4)
        self.lbl_login_password.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_login_password.setObjectName("lbl_login_password")
        self.verticalLayout_4.addWidget(self.lbl_login_password)
        self.horizontalLayout.addWidget(self.frame_4)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_comp_name.setText(_translate("Form", "comp name"))
        self.lbl_name.setText(_translate("Form", "name"))
        self.lbl_logo.setText(_translate("Form", "logo"))
        self.lbl_login_password.setText(_translate("Form", "login/password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())