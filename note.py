class Note:
    def __init__(self, name):
        self.name = name
        self.next_note = None

class NoteLinkedList:
    def __init__(self):
        self.head = None

    def append(self, name):
        new_note = Note(name)
        if not self.head:
            self.head = new_note
        else:
            current_note = self.head
            while current_note.next_note:
                current_note = current_note.next_note
            current_note.next_note = new_note

    def link_notes(self, from_note, to_note):
        current_note = self.head
        from_note_found = False

        while current_note:
            if current_note.name == from_note:
                from_note_found = True
                if current_note.next_note:
                    print(f"'{from_note}' is already linked to '{current_note.next_note.name}'")
                    break
                else:
                    current_note.next_note = Note(to_note)
                    print(f"'{from_note}' is now linked to '{to_note}'")
                    break
            current_note = current_note.next_note

        if not from_note_found:
            print(f"'{from_note}' not found in the list")
    def find_distance(self, from_note, to_note):
        semitone_distances = {
            "C": 0, "C#": 1, "D": 2, "D#": 3, "E": 4,
            "F": 5, "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11
        }

        from_semitone = semitone_distances.get(from_note)
        to_semitone = semitone_distances.get(to_note)

        if from_semitone is not None and to_semitone is not None:
            distance = (to_semitone - from_semitone) % 12
            return distance
        else:
            return None
# Create a linked list of 12 musical notes


# Define two note names


# Calculate the distance between the two notes



