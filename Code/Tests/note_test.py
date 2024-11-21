import unittest
from datetime import datetime
from clinic.note import Note  # Replace 'your_module' with the actual module name where the Note class is defined.

class TestNote(unittest.TestCase):

    def setUp(self):
        """Set up a Note instance for testing."""
        self.note = Note(1, "This is a test note.")

    def test_initialization_valid(self):
        """Test that the Note is initialized correctly with valid inputs."""
        self.assertEqual(self.note.code, 1)
        self.assertEqual(self.note.text, "This is a test note.")
        self.assertIsInstance(self.note.timestamp, datetime)

    def test_initialization_empty_code(self):
        """Test initialization with an empty code."""
        note = Note(1, "No code provided.")
        self.assertEqual(note.code, 1)
        self.assertEqual(note.text, "No code provided.")

    def test_initialization_empty_text(self):
        """Test initialization with an empty text."""
        note = Note(2, "")
        self.assertEqual(note.code, 2)
        self.assertEqual(note.text, "")

    def test_initialization_both_empty(self):
        """Test initialization with both empty code and text."""
        note = Note("", "")
        self.assertEqual(note.code, "")
        self.assertEqual(note.text, "")

    def test_equality(self):
        """Test the equality method."""
        note2 = Note(1, "This is a test note.")
        note3 = Note(2, "This is another note.")
        note4 = Note(3, "This is a different note.")

        self.assertEqual(self.note, note2)  # Should be equal
        self.assertNotEqual(self.note, note3)  # Should not be equal
        self.assertNotEqual(self.note, note4)  # Different text, should not be equal

    def test_str(self):
        """Test the string representation of the Note."""
        self.assertEqual(str(self.note), "Note(1: This is a test note.)")

    def test_note_timestamp(self):
        """Test that the timestamp is set upon initialization."""
        timestamp = self.note.timestamp
        self.assertIsInstance(timestamp, datetime)
        self.assertLessEqual(timestamp, datetime.now())  # Ensure timestamp is not in the future

    def test_equality_with_different_type(self):
        """Test equality with a non-Note object."""
        self.assertNotEqual(self.note, "Not a Note")  # Should not be equal

    def test_note_properties_mutability(self):
        """Test that attributes can be modified after initialization."""
        self.note.text = "Updated note text."
        self.assertEqual(self.note.text, "Updated note text.")
        self.note.code = 3
        self.assertEqual(self.note.code, 3)

if __name__ == "__main__":
    unittest.main()
