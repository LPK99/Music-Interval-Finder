
from note import NoteLinkedList

# Dictionary of music intervals
interval = {
    'm2': 1,
    'M2': 2,
    'm3': 3,
    'M3': 4,
    'P4': 5,
    'TT': 6,
    'P5': 7,
    'm6': 8,
    'M6': 9,
    'm7': 10,
    'M7': 11,
    'Octave': 12
}

notes = NoteLinkedList()
notes.append("C")
notes.append("C#")
notes.append("D")
notes.append("D#")
notes.append("E")
notes.append("F")
notes.append("F#")
notes.append("G")
notes.append("G#")
notes.append("A")
notes.append("A#")
notes.append("B")

def main():
    while True:
        first_note = input('Enter your first note : ')
        second_note = input('Enter your second note : ')
        distance = notes.find_distance(first_note, second_note)
        
        print(f'Your interval is {list(interval.keys())[list(interval.values()).index(distance)]}')

if __name__ == '__main__':
    main()