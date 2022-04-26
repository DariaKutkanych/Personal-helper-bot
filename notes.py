from field import Note
from collections import UserDict, UserList
import re


class NotesBook(UserList):

    def __init__(self):
        super().__init__()
        self.data = []
        self.note = ""
        self.id_note = None
        self.tag = ""

    def __str__(self):
        # need to add beautiful output like in future AddressBook
        return f"{self.data}"

    def add_note(self, note: Note, tag=""):
        self.note = note
        self.tag = tag
        self.id_note = len(self.data) + 1
        self.data.append({"id": self.id_note, "tag": self.tag,
                          "note": self.note})

    def delete_note(self, notes):
        for i in notes:
            if i in self.data:
                self.data.remove(i)

    def search_parametr_note(self, note_parametr, user_parametr):
        find_note = []
        for i in self.data:
            if str(i.get(note_parametr)) == user_parametr:
                find_note.append(i)
        return find_note

    def search_word_note(self, part_note):
        find_all_notes = []
        for i in self.data:
            if re.findall(part_note, str(i.get('note'))):
                find_all_notes.append(i)
        return find_all_notes

    def edit_note(self, note: Note):
        pass

    def sort_note(self):
        self.data = sorted(self.data, key=lambda d: d['tag'])
