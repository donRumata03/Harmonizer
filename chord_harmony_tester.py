from harmonizer import *

def test_two(c1, c2):
    print(get_disharmony_degree(c1))
    print(get_disharmony_degree(c2))


def find_harmonic_chords(get_main_form = True):
    data = set()
    for note1 in range(1, 15):
        for note2 in range(note1 + 1, 14):
            if get_main_form:
                this_chord = tuple(get_chord_main_form([note1, note2]))
            else:
                this_chord = (note1, note2)
            if this_chord[0] < this_chord[1] and this_chord[0] != 0:
                data.add((this_chord, get_disharmony_degree(list(this_chord))))
    res = sorted(data, key=lambda x: x[1])
    return res

harm = find_harmonic_chords()

index = 0
print(str(index) + ") Ох! Ох! ОХ!")
for chord, val in harm:
    index += 1
    print(str(index) + ")", chord, ":", val, ";", get_chord_by_little_form(chord))
