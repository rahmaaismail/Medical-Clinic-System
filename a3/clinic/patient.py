from clinic.patient_record import PatientRecord

class Patient:
        def __init__(self, phn, name, birth_date, phone, email, address):
            """
            Initialize a new Patient object
            
            Parameters:
            - phn: Personal Healthcare Number: a unique identifier for each patient
            - name: Patient's full name
            - age: Patient's age
            - phone: Patient's phone number
            - email: Patient's email
            - address: Patient's home address

            """
            self.phn = phn
            self.name = name
            self.birth_date = birth_date
            self.phone = phone
            self.email = email
            self.address = address
            self.record = PatientRecord()
            #patient note collection,

        def __eq__(self, other):
            if not isinstance(other, Patient):
                return NotImplemented
            return self.phn== other.phn and self.name == other.name and self.birth_date== other.birth_date and self.phone == other.phone and self.email == other.email and self.address == other.address


        def __str__(self):
            """
            Return a string representation of the Patient's information/object
            """
            return f"Patient(PHN: {self.phn}, Name: {self.name}, Birth Date: {self.birth_date}, Phone: {self.phone}, Email: {self.email}, Address: {self.address})"
