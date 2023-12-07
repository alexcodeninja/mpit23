from PyQt5 import QtCore, QtGui, QtWidgets
import ctypes
import sys
import os

from PyQt5.QtGui import QFont, QIcon

import main_win_adm
import login
import account_row
import main_win_usr
import report_row
import all_row

import connect


# standard message show function in app
def show_base_msg(text="None", title="B8 analitics"):
    msg = QtWidgets.QMessageBox()
    msg.setText(text)
    msg.setWindowTitle(title)
    msg.setFont(QFont("Roboto", 10))
    # msg.setWindowIcon(QIcon(":/images/assets/logo.svg"))
    msg.exec_()

class win_login(QtWidgets.QWidget, login.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb_enter.clicked.connect(self.auth)

    def auth(self):
        if not connect.is_connected():
            show_base_msg("Отстутсвует подключение к интернету, проверьте соединение и повторите попытку")
        elif len(self.le_login.text()) == 0 or len(self.le_password.text()) == 0:
            show_base_msg("Все поля являются обязательными к заполнению")
        elif not connect.get_data(f"/users/{self.le_login.text()}"):
            show_base_msg("Логин или пароль были введены неправильно, проверьте валидность введных данных и повторите попытку")
        else:
            user = connect.get_data(f"users/{self.le_login.text()}")
            if str(user["pwd"]) != self.le_password.text():
                show_base_msg("Логин или пароль были введены неправильно, проверьте валидность введных данных и повторите попытку")
            elif self.le_login.text() == "admin":
                self.win = WinMainAdm()
                self.win.show()
                self.close()
            else:
                self.win = WinMainUsr()
                self.win.show()
                self.close()

class WinMainUsr(QtWidgets.QWidget, main_win_usr.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb_change_account.clicked.connect(self.logout)

    def logout(self):
        self.win = win_login()
        self.win.show()
        self.close()

class WinMainAdm(QtWidgets.QWidget, main_win_adm.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(4)


        self.pb_to_ready_reports.pressed.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pb_to_all_reports.pressed.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pb_to_create_account.pressed.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.pb_to_accounts.pressed.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.pb_change_account.clicked.connect(self.logout)

        for i in range(30):
            wid = RowAll()
            wid.lbl_name.setText(str(i))
            wid.lbl_status.setText(str(i))
            self.vl_all.addWidget(wid)

    def logout(self):
        self.win = win_login()
        self.win.show()
        self.close()

class RowAll(QtWidgets.QWidget, all_row.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class RowAccount(QtWidgets.QWidget, account_row.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class RowReport(QtWidgets.QWidget, report_row.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

#setting icon in taskbar
if sys.platform == "win32":
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("mpit.hack.b8")

app = QtWidgets.QApplication([])
#adding fonts
for i in os.listdir("assets/Roboto"):
    QtGui.QFontDatabase.addApplicationFont("assets/Roboto/"+i)
QtGui.QFontDatabase.addApplicationFont("assets/fonts/vsd_mono.ttf")
win = win_login()
win.show()
app.exec_()