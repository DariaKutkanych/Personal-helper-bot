from field import Note
from collections import UserDict

class NotesBook(UserDict):

    def __init__(self):
        self.data = []

    def add_note(self, note: Note):
        self.note = note.value
        self.added_note = {'id': len(self.data)+1, 'tag': '', 'note':
                           self.note}
        self.data.append(self.added_note)
        flag_tag = input("Do you want to add tag for this note? Enter y, "
                         "if yes otherwise enter n")

    def search_note(self):
        pass
