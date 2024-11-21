import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout

from clinic.controller import Controller, DuplicateLoginException, InvalidLoginException


class ClinicGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        # Continue here with your code!
        self.controller = Controller()
        self.setWindowTitle("Medical Clinic System")

        layout = QGridLayout()
        label_username = QLabel("Username")
        self.text_username = QLineEdit()
        label_password = QLabel("Password")
        self.text_password = QLineEdit()
        self.text_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.text_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.button_login = QPushButton("Login")
        self.button_quit = QPushButton("Quit")

        layout.addWidget(label_username, 0, 0)
        layout.addWidget(self.text_username, 0, 1)
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.text_password, 1, 1)
        layout.addWidget(self.button_login, 2, 0)
        layout.addWidget(self.button_quit, 2, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # connect the buttons' clicked signals to the slots below
        self.button_login.clicked.connect(self.login_button_clicked)
        self.button_quit.clicked.connect(self.quit_button_clicked)


    def login_button_clicked(self):
        ''' 'handles controller login '''

        # TODO: get the username and password from the widgets
        try:
            username = self.text_username.text()
            password = self.text_password.text()
            is_login_successful = self.controller.login(username,password)
                     if is_login_successful:
                QMessageBox.information(self, "Login Success", "Welcome!")
            else:
                QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

            self.text_username.setText("")
            self.text_password.setText("")

        except DuplicateLoginException as e:
            QMessageBox.warning(self, "Already Logged In", f"Error: {str(e)}")
        except InvalidLoginException as e:
            QMessageBox.warning(self, "Ivalid Username or Password", f"Error: {str(e)}")




    def quit_button_clicked(self):
        ''' quit the program '''
        # TODO: find the command to quit the program
        QApplication.instance().quit()



def main():
    app = QApplication(sys.argv)
    window = ClinicGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
