import sys
import json
from PyQt6.QtCore import Qt, QAbstractTableModel
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QApplication, QMainWindow, QPushButton, QMessageBox, QPlainTextEdit, QGridLayout, QTableView, QDialog, QComboBox, QDateEdit, QListWidget, QDialogButtonBox
from clinic.controller import Controller, DuplicateLoginException, InvalidLoginException, IllegalAccessException, NoCurrentPatientException, IllegalOperationException

class ClinicGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.controller = Controller(autosave = True)

        self.setWindowTitle('Medical Clinic System')
        self.setGeometry(300, 300, 400, 200)  # Width: 400, Height: 200

     # Setup the main widget for the login screen
        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)

        # Create the layout and add widgets for login screen
        layout = QVBoxLayout()

        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Enter username")

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setPlaceholderText("Enter password")

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.handle_login)

        self.quit_button = QPushButton("Quit")
        self.quit_button.clicked.connect(self.quit_button_clicked)

        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.quit_button)

        # Set the layout for the widget
        self.widget.setLayout(layout)

    def handle_login(self):

        try:
            username = self.username_input.text()
            password = self.password_input.text()

            is_successful = self.controller.login(username, password)

            if is_successful:
                self.open_main_window()
            else:
                QMessageBox.warning(self, "Login Failed", "Invalid Login Credentials")

        except InvalidLoginException as e:
            QMessageBox.warning(self, "Login Failed", "Wrong Username or Password")
        except DuplicateLoginException as e:
            QMessageBox.warning(self, "Login Failed", "Already Logged In")

        self.username_input.setText("")
        self.password_input.setText("")

    def open_main_window(self):
        """Opens the main clinic window after login"""
        self.main_window = MainWindow(self.controller)
        self.main_window.show()
        self.close()  # Close the login window

    def quit_button_clicked(self):
        ''' quit the program '''
        # TODO: find the command to quit the program
        QApplication.instance().quit()

class MainWindow(QWidget):
    def __init__(self, controller):
        super().__init__()

                # Set up the main menu window after successful login
        self.controller = controller # Store the controller here
        self.setWindowTitle("Clinic Main Menu")
        self.setGeometry(300, 300, 400, 300)

        # Layout for the main window
        layout = QVBoxLayout()

        #set up menu option buttons
        #Setting up appointment button to handle patient notes
        self.set_appointment_button = QPushButton("Set Patient Appointment")
        self.set_appointment_button.clicked.connect(self.handle_appointment)
        layout.addWidget(self.set_appointment_button)

        # Setting up patient management button to perform operations on the patients
        self.patient_management_button = QPushButton("Manage Patients")
        self.patient_management_button.clicked.connect(self.handle_patients)
        layout.addWidget(self.patient_management_button)

    # Logout button
        self.logout_button = QPushButton("Logout")
        layout.addWidget(self.logout_button)
        self.logout_button.clicked.connect(self.handle_logout)

        self.setLayout(layout)

    def handle_logout(self):
        """
        Handles logging out and returning to the login window
        """
        self.close()
        self.login_window = ClinicGUI()
        self.login_window.show()

    def open_search_window(self):
        """
        Method to open the search window after a successful login
        """
        self.search_window = SearchWindow(self.controller) # Pass the controller to the search window
        self.search_window.show() # Show the search window

        # Optionally, close the main login window
        self.close() # Close the login window after successful login

    def display_message(self, title, message):
        """
        Displays a simple QMessageBox with a custom title and message
        """
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()

    def handle_patients(self):
        # Opens the patient management menu
        self.open_patients_menu()

    def open_patients_menu(self):
        # Shows the patient management window
        self.patient_menu = PatientsMenu(self.controller)
        self.patient_menu.show()
        self.close
    def handle_appointment(self):
            # Opens the appointment menu
        self.open_notes_menu()

    def open_notes_menu(self):
            # Shows the appointment menu
        self.notes_menu = NotesMenu(self.controller)
        self.notes_menu.show()
        #self.close

class PatientsMenu(QWidget):
    def __init__(self,controller):
        super().__init__()

        # Set up the patients window 
        self.controller = controller # Store the controller here
        self.setWindowTitle("Patient Management Menu")
        self.setGeometry(300, 300, 400, 300)

        # Layout for the main window
        layout = QVBoxLayout()

    # Create New Patient Button
        self.create_patient_button = QPushButton("Create New Patient")
        self.create_patient_button.clicked.connect(self.handle_patient_creation)
        layout.addWidget(self.create_patient_button)

        # List all Patients Button
        self.list_all_patients_button = QPushButton("List All Patients")
        layout.addWidget(self.list_all_patients_button)
        self.list_all_patients_button.clicked.connect(self.handle_patient_list)

        # Search Patient Button
        self.search_patient_button = QPushButton("Search Patient")
        self.search_patient_button.clicked.connect(self.handle_patient_search)
        layout.addWidget(self.search_patient_button)

        # Update Patient Information Button
        self.update_patient_button = QPushButton("Update Existing Patient")
        self.update_patient_button.clicked.connect(self.handle_patient_update)
        layout.addWidget(self.update_patient_button)

        # Delete Patient Button
        self.delete_patient_button = QPushButton("Delete Existing Patient")
        self.delete_patient_button.clicked.connect(self.handle_patient_delete)
        layout.addWidget(self.delete_patient_button)

        # Choose Current Patient Button
        self.choose_current_patient_button = QPushButton("Choose Current Patient")
        self.choose_current_patient_button.clicked.connect(self.handle_patient_choose)
        layout.addWidget(self.choose_current_patient_button)

        # Retrieve Patients Button
        self.retrieve_patients_button = QPushButton("Retrieve Existing Patients")
        self.retrieve_patients_button.clicked.connect(self.handle_patient_retrieve)
        layout.addWidget(self.retrieve_patients_button)

        self.setLayout(layout)

     def handle_patient_creation(self):
        # Show the create patient dialog
        self.create_patient_dialog = CreatePatientDialog(self.controller)
        self.create_patient_dialog.exec() # This blocks until the dialog is closed

    def handle_patient_list(self):
        # Show the list all patients dialog
        self.list_all_patients_dialog = ListAllPatientsDialog(self.controller)
        self.list_all_patients_dialog.exec() # This blocks until the dialog is closed

    def handle_patient_search(self):
        # Show the search patients dialog
        self.search_patients_dialog = SearchPatientDialog(self.controller)
        self.search_patients_dialog.exec() # This blocks until the dialog is closed

    def handle_patient_update(self):
        # Show the update patients dialog
        self.update_patients_dialog = UpdatePatientDialog(self.controller)
        self.update_patients_dialog.exec() # This blocks until the dialog is closed

    def handle_patient_delete(self):
        # Show the delete patient dialog
        self.delete_patient_dialog = DeletePatientDialog(self.controller)
        self.delete_patient_dialog.exec() # This blocks until the dialog is closed

    def handle_patient_choose(self):
        # Show the choose current patient dialog
        self.choose_current_patient_dialog = ChooseCurrentPatientDialog(self.controller)
        self.choose_current_patient_dialog.exec() # Block until the dialog is closed
    def handle_patient_retrieve(self):
        # Show the retrieve patients dialog
        self.retrieve_patients_dialog = RetrievePatientsDialog(self.controller)
        self.retrieve_patients_dialog.exec() # Block until the dialog is closed

class CreatePatientDialog(QDialog):
    def __init__(self, controller):
        super().__init__()

                # Set up the create patient window
        self.controller = controller # Store the controller here
        self.setWindowTitle("Create New Patient")
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()

        # PHN
        self.phn_input = QLineEdit(self)
        self.phn_input.setPlaceholderText("Enter PHN")
        layout.addWidget(self.phn_input)

        # Name
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Enter name")
        layout.addWidget(self.name_input)

        # Birth Date
        self.birth_date_input = QDateEdit(self)
        self.birth_date_input.setCalendarPopup(True)
        layout.addWidget(self.birth_date_input)

        # Phone Number
        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Enter phone number")
        layout.addWidget(self.phone_input)

        # Email Address
        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Enter email address")
        layout.addWidget(self.email_input)

        # Address
        self.address_input = QLineEdit(self)
        self.address_input.setPlaceholderText("Enter home address")
        layout.addWidget(self.address_input)

        # Dialog buttons (Ok and Cancel)
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        layout.addWidget(button_box)

        button_box.accepted.connect(self.create_patient)
        button_box.rejected.connect(self.reject)

        self.setLayout(layout)

    def create_patient(self):
        phn = int(self.phn_input.text())
        name = self.name_input.text()
        birth_date = self.birth_date_input.date().toString("yyyy-MM-dd")  # format the date
        phone = self.phone_input.text()
        email = self.email_input.text()
        address = self.address_input.text()

        if not phn or not name or not birth_date or not phone or not email or not address:
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
            return

        try:
            # Call the controller's create_patient method
            self.controller.create_patient(phn, name, birth_date, phone, email, address)
            QMessageBox.information(self, "Patient Created", "New patient created successfully!")
            # Manually save the patients after creating a new one
            # self.controller.patient_dao.save_patients()
            self.accept()  # Close the dialog
        except IllegalAccessException:
            QMessageBox.warning(self, "Error", f"Failed to create patient")
            self.reject()  # Close the dialog


class PatientTableModel(QAbstractTableModel):
    """
    Model for displaying patient data in the table view for list all patients and retrieve patients
    """
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.patients = []

    def set_patients(self, patients):
        """
        Method to update the list of patients in the model
        """
        self.beginResetModel()  # Notify the view that the data is being reset
        self.patients = patients
        self.endResetModel()  # Notify the view that the data has been reset

    def rowCount(self, parent=None):
        return len(self.patients)

    def columnCount(self, parent=None):
        return 6  # Number of columns (Name, PHN, Birth Date, Phone, Email, Address)

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            patient = self.patients[index.row()]
            if index.column() == 0:
                return patient.name
            elif index.column() == 1:
                return patient.phn
            elif index.column() == 2:
                return patient.birth_date
            elif index.column() == 3:
                return patient.phone
            elif index.column() == 4:
                return patient.email
            elif index.column() == 5:
                return patient.address
        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            headers = ['Name', 'PHN', 'Birth Date', 'Phone', 'Email', 'Address']
            return headers[section]
        return super().headerData(section, orientation, role)

class ListAllPatientsDialog(QDialog):
    def __init__(self, controller):
        super().__init__()

            # Set up the list all patients window
        self.controller = controller # Store the controller here
        self.setWindowTitle("List All Patients")
        self.setGeometry(300, 300, 800, 600)

            # Create the QTableView to display the list of patients
        self.patient_table_view = QTableView(self)

        # Button box with OK button
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        button_box.accepted.connect(self.accept)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.patient_table_view)
        layout.addWidget(button_box)

        self.setLayout(layout)

        # Initialize the patient model and load data
        self.patient_model = PatientTableModel(controller)
        self.patient_table_view.setModel(self.patient_model)

        # Initially populate the table with data
        self.list_all_patients()


    def list_all_patients(self):
        """
        Retrieve all patients and set the model for QTableView.
        """
        patients = self.controller.list_patients()  # Get all patients from the controller
        self.patient_model.set_patients(patients)

        if not patients:
            self.patient_table_view.setEnabled(False)
        else:
            self.patient_table_view.setEnabled(True)

        # Adjust column widths for better presentation
        self.patient_table_view.setColumnWidth(0, 200)  # Adjust columns as needed
        self.patient_table_view.setColumnWidth(1, 150)
        self.patient_table_view.setColumnWidth(2, 150)

class SearchPatientDialog(QDialog):
    def __init__(self, controller):
        super().__init__()

        # Set up search patients window
        self.controller = controller # Store the controller here 
        self.setWindowTitle("Search for a Patient")
        self.setGeometry(300, 300, 400, 200)

        layout = QVBoxLayout()

        # PHN or Name input for searching
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Enter PHN to Search")
        layout.addWidget(self.search_input)

        # Search Button
        self.search_button = QPushButton("Search", self)
        self.search_button.clicked.connect(self.search_patient)
        layout.addWidget(self.search_button)

        # Result Display Area
        self.result_label = QLabel(self)
        layout.addWidget(self.result_label)

        # Dialog Buttons (Ok and Cancel)
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Cancel)
        layout.addWidget(button_box)

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        self.setLayout(layout)

    def search_patient(self):
        query = self.search_input.text()

        if not query:
           QMessageBox.warning(self, "Input Error", "Please enter a PHN to search.")
           return

        # Check if the input is numeric (valid PHN format)
        if not query.isdigit():
           QMessageBox.warning(self, "Input Error", "PLease enter a valid numeric PHN.")
           return

        # Convert the PHN to an integer
        phn_int = int(query)

     # Perform the search (search by PHN as a string)
        patient = self.controller.search_patient(phn_int)

        # print("search result:", patient)

        if patient:
           # Display the patient information if found
           patient_info = (f"Name: {patient.name}\n"
                           f"PHN: {patient.phn}\n"
                           f"Birth Date: {patient.birth_date}\n"
                           f"Phone: {patient.phone}\n"
                           f"Email: {patient.email}\n"
                           f"Address: {patient.address}")
           QMessageBox.information(self, "Patient Found", patient_info)

        else:
            # If no patient is found
            QMessageBox.warning(self, "No Patient Found", "No patient found with that PHN.")

class UpdatePatientDialog(QDialog):
    def __init__(self, controller):
        super().__init__()

        # Set up update patient window
        self.controller = controller
        self.setWindowTitle("Update Patient Information")
        self.setGeometry(300, 300, 400, 400)

        self.patient = None  # Will hold the patient object after lookup

        layout = QVBoxLayout()

        # PHN Input (to search for the patient)
        self.phn_input = QLineEdit(self)
        self.phn_input.setPlaceholderText("Enter PHN to search for patient")
        layout.addWidget(self.phn_input)

        # Search Button
        self.search_button = QPushButton("Search Patient", self)
        layout.addWidget(self.search_button)
        self.search_button.clicked.connect(self.search_patient_by_phn)

        self.setLayout(layout)

    def search_patient_by_phn(self):
        phn = self.phn_input.text()
        if not phn:
            QMessageBox.warning(self, "Input Error", "Please enter a PHN.")
            return

        # Convert PHN input to integer, assuming it's a valid number
        try:
            phn_int = int(phn)  # Convert PHN input to integer
        except ValueError:
            QMessageBox.warning(self, "Invalid PHN", "Please enter a valid numeric PHN.")
            return

        # Try to find the patient by PHN
        patient = self.controller.search_patient(phn_int)
        if patient:
            self.patient = patient  # Store the found patient
            self.show_patient_details()  # Show the patient's details in the form
        else:
            QMessageBox.warning(self, "Patient Not Found", "No patient found with that PHN.")

    def show_patient_details(self):
        """Once the patient is found, display the editable fields."""
        # Clear the layout and show the patient details form
        layout = self.layout()
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # Patient Details for Editing
        self.name_input = QLineEdit(self)
        self.name_input.setText(self.patient.name)
        layout.addWidget(self.name_input)

        self.birth_date_input = QDateEdit(self)
        self.birth_date_input.setCalendarPopup(True)
        layout.addWidget(self.birth_date_input)

        self.phone_input = QLineEdit(self)
        self.phone_input.setText(self.patient.phone)
        layout.addWidget(self.phone_input)

        self.email_input = QLineEdit(self)
        self.email_input.setText(self.patient.email)
        layout.addWidget(self.email_input)

        self.address_input = QLineEdit(self)
        self.address_input.setText(self.patient.address)
        layout.addWidget(self.address_input)

        # Dialog buttons
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        layout.addWidget(button_box)
        button_box.accepted.connect(self.update_patient)
        button_box.rejected.connect(self.reject)

    def update_patient(self):
        """Retrieve and update patient data."""
        name = self.name_input.text()
        birth_date = self.birth_date_input.date().toString("yyyy-MM-dd")
        phone = self.phone_input.text()
        email = self.email_input.text()
        address = self.address_input.text()

        # Ensure that all fields are filled in
        if not name or not birth_date or not phone or not email or not address:
           QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
           return

    # Update the patient data by calling the controller's method
        try:
            self.controller.update_patient(
                self.patient.phn,  # This is the key (the original PHN)
                phn=self.patient.phn,  # Keep the same PHN if it's not being updated
                name=name,
                birth_date=birth_date,
                phone=phone,
                email=email,
                address=address
           )

            QMessageBox.information(self, "Success", "Patient information updated successfully!")
            self.controller.patient_dao.save_patients()  # Save changes to database
            self.accept()  # Close the dialog
        except Exception as e:
            # If there is an error updating the patient, show an error message
            QMessageBox.warning(self, "Update Failed", str(e))
            self.reject()  # Close the dialog if there's an error

class DeletePatientDialog(QDialog):
    def __init__(self, controller):
        super().__init__()

                # Set up delete patient window
        self.controller = controller  # Store the controller here
        self.setWindowTitle("Delete a Patient")
        self.setGeometry(300, 300, 400, 200)

        layout = QVBoxLayout()

        # PHN input for deleting a patient
        self.phn_input = QLineEdit(self)
        self.phn_input.setPlaceholderText("Enter PHN of the patient to delete")
        layout.addWidget(self.phn_input)

        # Delete Button
        self.delete_button = QPushButton("Delete", self)
        self.delete_button.clicked.connect(self.delete_patient)
        layout.addWidget(self.delete_button)

        # Dialog Buttons (Ok and Cancel)
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Cancel)
        layout.addWidget(button_box)

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        self.setLayout(layout)

    def delete_patient(self):
        phn = self.phn_input.text().strip()  # Remove extra spaces

        if not phn:
            QMessageBox.warning(self, "Input Error", "Please enter the PHN of the patient.")
            return

        # Check if the PHN input is numeric (valid PHN format)
        if not phn.isdigit():
            QMessageBox.warning(self, "Input Error", "Please enter a valid numeric PHN.")
            return

        # Convert the PHN to an integer
        phn_int = int(phn)

        try:
            # Attempt to delete the patient with the given PHN
            success = self.controller.delete_patient(phn_int)
            if success:
                QMessageBox.information(self, "Patient Deleted", f"Patient with PHN {phn_int} deleted successfully!")
                self.accept()  # Close the dialog
            else:
                QMessageBox.warning(self, "Error", f"No patient found with PHN {phn_int}.")
                self.reject()  # Close the dialog

        except Exception as e:
            print(f"Unexpected error: {e}")  # Log unexpected errors
            QMessageBox.critical(self, "Unexpected Error", f"An unexpected error occurred: {e}")
            self.reject()  # Close the dialog gracefully

class ChooseCurrentPatientDialog(QDialog):
    def __init__(self, controller):
        super().__init__()

                # Set up chooose current patient window
        self.controller = controller  # Store the controller
        self.notes_menu = NotesMenu  # Pass the NotesMenu instance for updating the current patient info
        self.setWindowTitle("Choose Current Patient")
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()

        # Dropdown menu to select a patient by PHN
        self.patient_selector = QComboBox(self)
        self.populate_patient_list()
        layout.addWidget(self.patient_selector)

        # Label to show the current patient
        self.current_patient_label = QLabel("No patient selected", self) # Initialize label
        layout.addWidget(self.current_patient_label)

        # Set as Current Patient Button
        self.set_current_button = QPushButton("Set as Current Patient", self)
        self.set_current_button.clicked.connect(self.choose_current_patient)
        layout.addWidget(self.set_current_button)

        # Cancel Button
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Cancel)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

        self.setLayout(layout)

        # If there's already a current patient, display them
        self.update_current_patient_display()

    def populate_patient_list(self):
        """Populates the dropdown with the list of patients."""
        self.patient_selector.clear()
        patients = self.controller.patient_dao.patients

        if not patients:
            QMessageBox.warning(self, "No Patients", "There are currently no patients to choose from.")
            self.reject()
            return

        for patient in patients:
            self.patient_selector.addItem(f"{patient.name} ({patient.phn})", patient.phn)

    def choose_current_patient(self):
        """Sets the selected patient as the current patient."""
        selected_phn = self.patient_selector.currentData()  # Get the PHN from the dropdown
        if selected_phn:
            try:
                # Set the current patient in the controller
                self.controller.set_current_patient(selected_phn)  # Ensure phn is passed
                QMessageBox.information(self, "Success", f"Patient with PHN {selected_phn} is now the current patient!")


                # After setting the current patient, update the NotesMenu display
                self.notes_menu.update_current_patient_display(self)

                self.accept()  # Close the dialog
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to set patient as current: {str(e)}")
        else:
            QMessageBox.warning(self, "Error", "No patient was selected.")

    def update_current_patient_display(self):
        """Update the display to show the current patient's information."""
        if self.controller.current_patient:
            self.current_patient_label.setText(f"Current Patient: {self.controller.current_patient.name} ({self.controller.current_patient.phn})")

class RetrievePatientsDialog(QDialog):
    def __init__(self, controller):
        super().__init__()

                # Set up retrieve patients window
        self.controller = controller  # Store the controller here
        self.setWindowTitle("Retrieve Existing Patients")
        self.setGeometry(300, 300, 800, 600)

        layout = QVBoxLayout()

        # Search Bar to search patients by name
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Enter name to search.")
        layout.addWidget(self.name_input)

        # Button to initiate the search
        self.search_button = QPushButton("Search", self)
        layout.addWidget(self.search_button)

        # Create a QTableView to display the patient data
        self.patient_table_view = QTableView(self)
        layout.addWidget(self.patient_table_view)

        # Button box with Ok to close the dialog
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        layout.addWidget(button_box)

        button_box.accepted.connect(self.accept)

        self.setLayout(layout)


        # Initialize the model with an empty list of patients
        self.model = PatientTableModel(self.controller)
        self.patient_table_view.setModel(self.model)

        # Connect search button to search function
        self.search_button.clicked.connect(self.retrieve_patient)

    def retrieve_patient(self):
        # Get the name from the input field
        name_text = self.name_input.text().strip()

        if not name_text:  # Handle empty input
            QMessageBox.warning(self, "Invalid Search", "Please enter a name to search.")
            return

        # Retrieve the patients based on the name using the controller's retrieve_patients method
        patients = self.controller.retrieve_patients(name_text)

        if patients:
            # Set the model with the retrieved patients (can be multiple)
            self.model.set_patients(patients)
        else:
            # If no patients are found, clear the model and show a message
            self.model.set_patients([])
            QMessageBox.information(self, "No Results", "No patients found with the provided name.")

class NotesMenu(QWidget):
    def __init__(self, controller):
        super().__init__()

        # Set up the appointment (notes) window 
        self.controller = controller # passed controller from ClinicGUI

        self.setWindowTitle("Patient Appointment Menu")
        self.setGeometry(300, 300, 400, 300)

        # Layout for the main window
        layout = QVBoxLayout()

        # Label to display the current patient
        self.current_patient_label = QLabel("No patient selected")
        layout.addWidget(self.current_patient_label)

        self.create_note_button = QPushButton("Create New Note")
        layout.addWidget(self.create_note_button)
        self.create_note_button.clicked.connect(self.open_create_note)

        self.retrieve_notes_button = QPushButton("Retrieve Notes")
        layout.addWidget(self.retrieve_notes_button)
        self.retrieve_notes_button.clicked.connect(self.handle_note_retrieving)

        self.update_note_button = QPushButton("Update Note")
        layout.addWidget(self.update_note_button)
        self.update_note_button.clicked.connect(self.handle_note_updating)

        self.delete_note_button = QPushButton("Delete Note")
        layout.addWidget(self.delete_note_button)
        self.delete_note_button.clicked.connect(self.handle_note_deleting)

        self.list_note_button = QPushButton("List Notes")
        layout.addWidget(self.list_note_button)
        self.list_note_button.clicked.connect(self.handle_note_listing)

        # Add the End Appointment button
        self.end_appointment_button = QPushButton("End Appointment")
        layout.addWidget(self.end_appointment_button)
        self.end_appointment_button.clicked.connect(self.end_appointment)

        self.setLayout(layout)
        # If there's already a current patient, display them
        self.update_current_patient_display()

    def update_current_patient_display(self):
        """Update the display to show the current patient's information."""
        if self.controller.current_patient:
            self.current_patient_label.setText(f"Current Patient: {self.controller.current_patient.name} ({self.controller.current_patient.phn})")
        else:
            self.current_patient_label.setText("Current Patient: None")

    def end_appointment(self):
                """Unsets the current patient, updates the UI, and returns to the patient management menu."""
                try:
                   self.controller.unset_current_patient()  # Unset the current patient
                   self.update_current_patient_display()    # Update the display

                   # Show success message
                   QMessageBox.information(self, "Success", "The appointment has ended. No current patient.")

                   # Close the current appointment window
                   self.close()

                except Exception as e:
                   # Show error message if something goes wrong
                   QMessageBox.warning(self, "Error", f"Failed to end the appointment: {str(e)}")

    def open_create_note(self):

        try:
            current_patient = self.controller.current_patient
            self.create_note_dialog = CreateNoteDialog(self.controller, current_patient)
            self.create_note_dialog.exec() #this blocks until the dialog is closed
        except ValueError:
            QMessageBox.warning(self, "Setting Patient Error", "Invalid PHN")

    def handle_note_retrieving(self):

        try:
            current_patient = self.controller.current_patient
            self.retrieve_notes_dialog = RetrieveNotesDialog(self.controller, current_patient)
            self.retrieve_notes_dialog.exec()

        except ValueError:
            QMessageBox.warning(self, "Setting Patient Error", "Invalid PHN")

    def handle_note_updating(self):

        try:
            current_patient = self.controller.current_patient
            self.update_note_dialog = UpdateNoteDialog(self.controller, current_patient)
            self.update_note_dialog.exec() #this blocks until the dialog is closed
        except ValueError:
            QMessageBox.warning(self, "Setting Patient Error", "Invalid PHN")

    def handle_note_deleting(self):

        try:
            current_patient = self.controller.current_patient
            self.delete_note_dialog = DeleteNoteDialog(self.controller, current_patient)
            self.delete_note_dialog.exec() #this blocks until the dialog is closed

        except ValueError:
            QMessageBox.warning(self, "Setting Patient Error", "Invalid PHN")

    def handle_note_listing(self):

        try:
            current_patient = self.controller.current_patient
            self.list_notes_dialog = ListNotesDialog(self.controller, current_patient)
            self.list_notes_dialog.exec() #this blocks until the dialog is closed

        except ValueError:
            QMessageBox.warning(self, "Setting Patient Error", "Invalid PHN")

#Note functionality Classes/windows
class CreateNoteDialog(QDialog):
    def __init__(self, controller, current_patient):
        super().__init__()

        self.controller = controller
        self.current_patient = (current_patient)
        self.setWindowTitle("Create Patient Notes")
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()

        # Enter Note
        self.note_input = QLineEdit(self)
        self.note_input.setPlaceholderText("Enter Note")
        layout.addWidget(self.note_input)

        # Dialog buttons (Ok and Cancel)
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        layout.addWidget(button_box)

        button_box.accepted.connect(self.create_note)
        button_box.rejected.connect(self.reject)

        self.setLayout(layout)


    def create_note(self):

        note = self.note_input.text()

        try:
            self.controller.create_note(note)
            QMessageBox.information(self, "Creation Successful", "Note Created Successfully")

        except IllegalOperationException:
            QMessageBox.warning(self, "Setting Patient Error", "Invalid PHN")
        except IllegalAccessException:
            QMessageBox.warning(self, "Creation Failed", "Log in to create note")

        except NoCurrentPatientException:
            QMessageBox.warning(self, "Creation Failed", "Set valid PHN to create note")


class RetrieveNotesDialog(QDialog):
    def __init__(self, controller, current_patient):
        super().__init__()
        self.controller = controller
        self.current_patient = (current_patient)
        self.setWindowTitle("Retrieve Patient Notes")
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()



        self.text_edit = QPlainTextEdit(self) #Plain text widget to display retrived results
        self.text_edit.setReadOnly(True)
        self.search_key_input = QLineEdit(self)
        self.search_key_input.setPlaceholderText("Enter search key to retrieve notes")

        layout.addWidget(self.search_key_input)
        layout.addWidget(self.text_edit)

        # Dialog buttons (Ok and Cancel)
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        layout.addWidget(button_box)

        button_box.accepted.connect(self.retrieve_notes)
        button_box.rejected.connect(self.reject)

        self.setLayout(layout)

    def retrieve_notes(self):
        search_key = self.search_key_input.text().lower() #take the text that was put into the text box

        try:
            success = self.controller.retrieve_notes(search_key)
            list_text = "\n".join(str(note) for note in success)

            if success:
                self.text_edit.setPlainText(list_text)
            else:
                self.text_edit.setPlainText("No results found")
        except IllegalAccessException:
            QMessageBox.warning(self, "Retrieval Fail", "Log in to Retrieve Notes")
        except NoCurrentPatientException:
            QMessageBox.warning(self, "Retrieval Fail", "Need to set current patient first")


class UpdateNoteDialog(QDialog):
    def __init__(self, controller, current_patient):
        super().__init__()

        self.controller = controller
        self.current_patient = (current_patient)
        self.setWindowTitle("Update Patient Notes")
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()

        #carry the set current patient

        self.code_input = QLineEdit(self)
        self.code_input.setPlaceholderText("Enter Note Code")

        self.updated_text_input = QLineEdit(self)
        self.updated_text_input.setPlaceholderText("Enter Updated Information")

        layout.addWidget(self.code_input)
        layout.addWidget(self.updated_text_input)

        # Dialog buttons (Ok and Cancel)
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        layout.addWidget(button_box)

        button_box.accepted.connect(self.update_note)
        button_box.rejected.connect(self.reject)

        self.setLayout(layout)


    def update_note(self):

        code = int(self.code_input.text())

        updated_note = self.updated_text_input.text()

        try:
            success = self.controller.update_note(code, updated_note)
            QMessageBox.information(self, "Update Successful", f"Note({code}) updated")
        except IllegalAccessException:
            QMessageBox.warning(self, "Update Failed", "Log in to update note")
        except NoCurrentPatientException:
            QMessageBox.warning(self, "Update Failed", "Set current patient to update note")

class DeleteNoteDialog(QDialog):
    def __init__(self, controller, current_patient):
        super().__init__()

        self.controller = controller
        self.current_patient = (current_patient)
        self.setWindowTitle("Delete Patient Notes")
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()


        self.code_input = QLineEdit()
        self.code_input.setPlaceholderText("Enter Note code to delete")

        layout.addWidget(self.code_input)

        # Dialog buttons (Ok and Cancel)
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        layout.addWidget(button_box)

        button_box.accepted.connect(self.delete_note)
        button_box.rejected.connect(self.reject)

        self.setLayout(layout)

    def delete_note(self):
            code = int(self.code_input.text())  # Get the note code from input field

            try:
                # Check if the note code exists
                note_to_delete = None
                for note in self.controller.list_notes():
                    if note.code == code:
                        note_to_delete = note
                        break

                if not note_to_delete:
                    QMessageBox.warning(self, "Deletion Fail", f"Note with code {code} does not exist.")
                    return

                # Proceed to delete the note
                success = self.controller.delete_note(code)
                if success:
                    QMessageBox.information(self, "Deletion Successful", f"Note ({code}) deleted")
                else:
                     QMessageBox.warning(self, "Deletion Fail", "Failed to delete note.")
              except NoCurrentPatientException:
               QMessageBox.warning(self, "Error", "Set current patient first")
            except IllegalAccessException:
               QMessageBox.warning(self, "Deletion Fail", "Log in to delete note")

class ListNotesDialog(QDialog):
    def __init__(self, controller, current_patient):
        super().__init__()

        self.controller = controller
        self.current_patient = (current_patient)
        self.setWindowTitle("Create Patient Notes")
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()


        self.text_edit = QPlainTextEdit(self) #Plain text widget to display list of notes
        self.text_edit.setPlaceholderText("No notes for this patient")
        self.text_edit.setReadOnly(True)

        layout.addWidget(self.text_edit)

        try:
            success = self.controller.list_notes()
            list_text = "\n".join(str(note) for note in success)
            self.text_edit.setPlainText(list_text)

        except IllegalAccessException:
            QMessageBox.warning(self, "Listing Fail", "Log in to list patient notes")
        except NoCurrentPatientException:
            QMessageBox.warning(self, "Listing Fail", "Set current patient to list notes")

        # Dialog buttons (Ok and Cancel)
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Cancel)
        layout.addWidget(button_box)

        button_box.rejected.connect(self.reject)

        self.setLayout(layout)

    def display_message(self, title, message):
        """
        Displays a simple QMessageBox with a custom title and message
        """
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()

def main():
    app = QApplication(sys.argv)
    window = ClinicGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() # Show the login window
    sys.exit(app.exec_()) # Start the application loop

























