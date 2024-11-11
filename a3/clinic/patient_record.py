from clinic.note import Note


class PatientRecord:

    """- autocounter
    - all patients in the database
    - connected to patient noter
    """
    auto_counter = 0

    #initializing fields
    def __init__(self):
        self.patient_notes = []
        self.code = PatientRecord.auto_counter
        PatientRecord.auto_counter += 1

    def add_note(self, text):

        code = len(self.patient_notes) + 1  # Assuming patient_notes is a list
        new_note = Note(code,text)
        self.patient_notes.append(new_note)
        return new_note


    def retrieve_note_list(self, text_lookup):
        retrieved = []
         #look through current patient notes
        for notes in self.patient_notes:
            if text_lookup in notes.text:
                retrieved.append(notes)
        return retrieved

    def search_for_note(self, code):
        """Search for a note by its code."""

        index = code - 1  # Adjust for zero-based index

        if index < 0 or index >= len(self.patient_notes):
            return None  # Return None if the index is out of range

        return self.patient_notes[index]  # Return the note if index is valid



    def update(self, code, updated_txt):
        if len(self.patient_notes) == 0:
            return False #cannot update note if there are no notes in record

        updated_note = Note(code, updated_txt)
        self.patient_notes[code-1] = updated_note

        return True

     def remove_note(self,note_num):
        if (len(self.patient_notes) == 0):
            return False


        if (len(self.patient_notes) >= 1):
            index = note_num - 1
            if index < 0 or index >= len(self.patient_notes):
                return False  # Return False if the index is out of range

            self.patient_notes[index] = None
            return True

     def list_record(self):
        not_none = []
        for note in self.patient_notes:
            if note is not None:
                not_none.insert(0,note)
        return not_none
