# test_patient_record.py

import unittest
from clinic.note import Note  # Adjust the import based on where your Note class is located
from clinic.patient_record import PatientRecord  # Adjust this import based on where your PatientRecord class is located

class TestPatientRecord(unittest.TestCase):

    def setUp(self):
        """Set up a PatientRecord instance for testing."""
        self.record = PatientRecord()

    def test_add_note_creates_note(self):
        """Test that a note is added correctly."""
        note = self.record.add_note("Initial note.")
        self.assertEqual(len(self.record.patient_notes), 1)
        self.assertIsInstance(note, Note)
        self.assertEqual(note.text, "Initial note.")
        self.assertEqual(note.code, 1)  # Ensure the note has the correct code

    def test_add_multiple_notes(self):
        """Test that multiple notes can be added."""
        self.record.add_note("First note.")
        self.record.add_note("Second note.")
        self.assertEqual(len(self.record.patient_notes), 2)
        self.assertEqual(self.record.patient_notes[0].text, "First note.")
        self.assertEqual(self.record.patient_notes[1].text, "Second note.")

    def test_retrieve_note_list_with_matching_text(self):
        """Test retrieving notes that contain specific text."""
        self.record.add_note("First note.")
        self.record.add_note("Second note with health.")
        retrieved_notes = self.record.retrieve_note_list("health")
        self.assertEqual(len(retrieved_notes), 1)
        self.assertEqual(retrieved_notes[0].text, "Second note with health.")

    def test_retrieve_note_list_no_matches(self):
        """Test retrieving notes with no matching text."""
        self.record.add_note("First note.")
        self.record.add_note("Second note.")
        retrieved_notes = self.record.retrieve_note_list("health")
        self.assertEqual(len(retrieved_notes), 0)  # No matches

    def test_search_for_note_valid_code(self):
        """Test searching for a note by valid code."""
        self.record.add_note("Note 1")
        self.record.add_note("Note 2")
        note = self.record.search_for_note(1)
        self.assertIsNotNone(note)
        self.assertEqual(note.text, "Note 1")
    def test_search_for_note_invalid_code(self):
        """Test searching for a note by invalid code."""
        self.record.add_note("Note 1")
        note = self.record.search_for_note(3)  # Non-existent code
        self.assertIsNone(note)

    def test_update_note_success(self):
        """Test updating an existing note."""
        self.record.add_note("Old note.")
        self.assertTrue(self.record.update(1, "Updated note."))
        self.assertEqual(self.record.patient_notes[0].text, "Updated note.")

    def test_update_note_failure(self):
        """Test updating a non-existent note."""
        self.assertFalse(self.record.update(1, "This won't work."))  # Update on non-existent note

    def test_remove_note_success(self):
        """Test successfully removing a note."""
        self.record.add_note("Note to remove.")
        self.assertTrue(self.record.remove_note(1))
        self.assertIsNone(self.record.patient_notes[0])  # Check if the note is removed

    def test_remove_note_failure_on_empty_record(self):
        """Test removing a note when the record is empty."""
        self.assertFalse(self.record.remove_note(1))  # Try removing non-existent note

    def test_remove_note_invalid_index(self):
        """Test removing a note with an invalid index."""
        self.record.add_note("Note 1")
        self.assertFalse(self.record.remove_note(2))  # Non-existent index

    def test_list_record_excludes_none_values(self):
        """Test that the list of notes excludes None values."""
        self.record.add_note("First note.")
        self.record.add_note("Second note.")
        self.record.remove_note(1)  # Remove the first note
        notes = self.record.list_record()
        self.assertEqual(len(notes), 1)
        self.assertEqual(notes[0].text, "Second note.")

    def test_list_record_with_all_none(self):
        """Test listing when all notes are None."""
        self.assertEqual(len(self.record.list_record()), 0)

if __name__ == "__main__":
    unittest.main()
