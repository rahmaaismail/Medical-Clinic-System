from clinic.note import Note

class Controller:

    def __init__(self):

        self.is_logged_in = None #login status to help with double login
        self.patient_record = {} #list to hold Patient instances
        self.current_patient = None #current patient isnt chosen by default        


    def login(self, username, password):

        users = {"user": "clinic2024"}

        if self.is_logged_in is not None: # if user already logged in
            return False

        if username in users  and users[username] == password:
            self.is_logged_in = username
           # print("User successfully logged in")  # Debugging line
            return True
        else:
           # print("Login failed")  # Debugging line
            return False


    def logout(self):
        if self.is_logged_in is None: #not logged in
            return False
        else:
            if self.is_logged_in is not None:
                self.is_logged_in = None
                return True


    def search_patient(self, phn):
        """
        Search for a patient by their PHN

        """
        patient = self.patient_record.get(phn)
        return patient


    def create_patient(self, phn, name, birth_date, phone, email, address):
        """Create a new patient if they don't exist and add them to the patient records.

        """
        #compare entered phn so all patients in all patients dict to see if they already exist
        if not self.is_logged_in:
                     return None

        if phn in self.patient_record:
            return None  # Prevent creation of a duplicate patient

        new_patient = Patient(phn, name, birth_date,phone,email,address)
        self.patient_record[phn] = new_patient
        return new_patient


    def retrieve_patients(self, query):
        """
        Retrieve all patients in the patient record
        """
        if  not self.is_logged_in:
            return None
        retrieved = []
        for patients in self.patient_record.values():
            if query.lower() in patients.name.lower():
                retrieved.append(patients)
        return retrieved


    def update_patient(self, key , phn, name, birth_date, phone, email, address):
        """
        Update details of an existing patient
        """
        if not self.is_logged_in: #need to login to work the method
            return False

        # Check if the patient exists
        if self.current_patient:
            return False #cannot update if current Patient is set

        if key not in self.patient_record:
            return False

        # Check for duplicate new PHN
        if phn in self.patient_record and phn != key:
            return False

        # Update patient details
        patient = self.patient_record[key]
        patient.phn = phn
        patient.name = name
        patient.birth_date= birth_date
        patient.phone = phone
        patient.email = email
        patient.address = address

        # Change the key if PHN is updated
              if phn != key:
            del self.patient_record[key]  # Remove old entry
            self.patient_record[phn] = patient  # Add new entry with new PHN

        return True



    def delete_patient(self, phn):
        """
        Delete a patient from the record based on their PHN
        """
        if self.current_patient: #current patient is set
            return False #cannot delete current patient
        if phn in self.patient_record:
            self.patient_record.pop(phn)
            return True

        else:
            return False



    def list_patients(self):
        """
        List all patients currently in the record
        """
        if not self.is_logged_in:
            return None
        all_patients = list(self.patient_record.values())
        return all_patients



    def get_current_patient(self):
        """
        Retrieve the current patient by PHN
        """
        if not self.is_logged_in:
            return None #will not proceed unless logged in 

        get_patient = self.current_patient #return current patient is set

        return get_patient


    def set_current_patient(self, phn):
        """
        Directly set the details of an existing patient by PHN
         """
        if phn in self.patient_record: #search phn in patient
            self.current_patient = self.patient_record[phn] # set current patient the patient instance found connected to the phn
            return f"Patient with PHN {phn} set successfully."

        else:
            return f"Patient with PHN {phn} not found."


    def unset_current_patient(self):
         """
         Unset the current patient by PHN.
         If the current patient matches the provided PHN, it will be unset.
         """
         if self.current_patient is not None: #if current patient is set
             self.current_patient = None # Reset current patient


    def create_note(self, text):
        if not self.is_logged_in:
            return None

        # Check if there is a current patient
        if self.current_patient is None:
            return None

        # If both conditions are met, proceed with note creation
        return self.current_patient.record.add_note(text)


    def retrieve_notes(self, text):
        if self.current_patient is not None: # if current_patient is set
            return self.current_patient.record.retrieve_note_list(text) #method to access current_patient record field


    def update_note(self, code, updated_txt):
        if not self.is_logged_in:
            return False
        if self.current_patient is None: #current Patient not set
            return False
        return self.current_patient.record.update(code, updated_txt)


    def search_note(self, code):
        return self.current_patient.record.search_for_note(code)


    def delete_note(self, code):
        if  not self.is_logged_in:
            return False

        if self.current_patient is not None:
            success = self.current_patient.record.remove_note(code)
            return success

        else:
            return False


    def list_notes(self):
        if not self.is_logged_in: #will not proceed if user is not logged in
            return None

        if self.current_patient is not None: # current patient is set
            return self.current_patient.record.list_record()


