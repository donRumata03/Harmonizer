import math

from formalizer import *
from dictionary import *
from inverser import *

disharmony_getter = {
    0 : 0,             # Prima
    1 : 4,             # Little second
    2 : 2.5,           # Big second
    3 : 1,             # Little tercium
    4 : 1,             # Big tercium
    5 : 0.1,           # Kvarta
    6 : 3              # Triton
}



def get_interval_disharmony(distance):
    new_distance = distance % 12
    return disharmony_getter[min(new_distance, 12 - new_distance)]


def get_disharmony_degree(chord : list): # little form!!!
    """
    if len(chord) != 2:
        print("Chord must have 3 notes")
        return
    """
    intervals = []
    norm_intervals = []
    for index1 in range(-1, len(chord)):
        for index2 in range(len(chord)):
            if index1 == index2:
                continue
            val1 = 0 if index1 == -1 else chord[index1]
            val2 = chord[index2]

            distance = abs(val1 - val2)
            intervals.append(distance)

            real_distance = min(distance % 12, 12 - distance % 12)

            norm_intervals.append(real_distance)

    interval_disharmonies = [get_interval_disharmony(interval) for interval in intervals]
    result = sum(interval_disharmonies) / (len(intervals) ** 0.3)
    print("Chord:", chord, "Intervals: ", intervals, ", Norm intervals :", norm_intervals, "Disharmonies:", interval_disharmonies, "Disharmony:", result)
    return result



def harmonize(tact : list, chord_size = 3):
    disharmonies = []
    best_disharmony = INF
    best_chord = []

    chords = generate_all_k_permutations(tact, chord_size)
    print(chords)

    """
    for bad_note_index in range(len(tact)):
        this_chord = []
        for note_index in range(len(tact)):
            if note_index != bad_note_index:
                this_chord.append(tact[note_index])
    
        this_disharmony = get_disharmony_degree(this_chord)
        disharmonies[bad_note_index] = this_disharmony

        if this_disharmony < best_disharmony:
            best_disharmony = this_disharmony
            best_chord = this_chord[:]

    print(disharmonies)
    return best_disharmony, best_chord
    """

    for chord in chords:
        little_form = convert_raw_to_little(chord)[1]
        this_disharmony = get_disharmony_degree(little_form)
        disharmonies.append(this_disharmony)

        if this_disharmony < best_disharmony:
            best_disharmony = this_disharmony
            best_chord = little_form

    # print(disharmonies)
    return best_disharmony, best_chord

if __name__ == "__main__":
    little_form = harmonize([0, 4, 7, 9])
    print(little_form)
    print("Little form :", little_form, "Info :", get_chord_by_little_form(little_form[1]))