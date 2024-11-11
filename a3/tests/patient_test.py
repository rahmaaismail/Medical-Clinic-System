
import unittest
from clinic.patient import Patient
from clinic.patient_record import PatientRecord

class TestPatient(unittest.TestCase):

    def setUp(self):
        """Set up a Patient instance for testing."""
        self.patient = Patient(
            phn="123456789",
            name="John Doe",
            birth_date="1990-01-01",
            phone="555-0123",
            email="john.doe@example.com",
            address="123 Main St, Anytown, USA"
        )

    def test_initialization(self):
        """Test that the Patient is initialized correctly."""
        self.assertEqual(self.patient.phn, "123456789")
        self.assertEqual(self.patient.name, "John Doe")
        self.assertEqual(self.patient.birth_date, "1990-01-01")
        self.assertEqual(self.patient.phone, "555-0123")
        self.assertEqual(self.patient.email, "john.doe@example.com")
        self.assertEqual(self.patient.address, "123 Main St, Anytown, USA")
        self.assertIsInstance(self.patient.record, PatientRecord)  # Check if record is an instance of PatientRecord

    def test_equality(self):
        """Test the equality operator."""
        patient2 = Patient(
            phn="123456789",
            name="John Doe",
            birth_date="1990-01-01",
            phone="555-0123",
            email="john.doe@example.com",
            address="123 Main St, Anytown, USA"
        )
        patient3 = Patient(
            phn="987654321",
            name="Jane Doe",
            birth_date="1995-01-01",
            phone="555-9876",
            email="jane.doe@example.com",
            address="456 Side St, Anytown, USA"
        )

        self.assertEqual(self.patient, patient2)  # Should be equal
        self.assertNotEqual(self.patient, patient3)  # Should not be equal
 def test_str(self):
        """Test the string representation of the Patient."""
        expected_str = ("Patient(PHN: 123456789, Name: John Doe, "
                        "Birth Date: 1990-01-01, Phone: 555-0123, "
                        "Email: john.doe@example.com, Address: 123 Main St, Anytown, USA)")
        self.assertEqual(str(self.patient), expected_str)

    def test_equality_with_different_type(self):
        """Test equality with a non-Patient object."""
        self.assertNotEqual(self.patient, "Not a Patient")  # Should not be equal

    def test_initialization_with_empty_fields(self):
        """Test initialization with empty fields."""
        empty_patient = Patient("", "", "", "", "", "")
        self.assertEqual(empty_patient.phn, "")
        self.assertEqual(empty_patient.name, "")
        self.assertEqual(empty_patient.birth_date, "")
        self.assertEqual(empty_patient.phone, "")
        self.assertEqual(empty_patient.email, "")
        self.assertEqual(empty_patient.address, "")

if __name__ == "__main__":
    unittest.main()
