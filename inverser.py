from formalizer import *
from dictionary import *
from math import *


def estimate_sigma(raw_chord : list) -> float: # raw chord!!!
    average = sum(raw_chord) / len(raw_chord)
    sqr_sum = 0
    for note in raw_chord:
        sqr_sum += (average - note) ** 2
    return (sqr_sum / len(raw_chord)) ** 0.5

def estimate_little_sigma(little_chord):
    return estimate_sigma(formalizer.convert_little_to_raw(little_chord))

def generate_note_variation(note, octave_number):
    return range(note - 12 * octave_number, note + 12 * (octave_number + 1), 12)

def generate_inversions_recursive_step(chord : list, this_step : int, inversions : list, octave_number : int) -> None:
    if this_step == len(chord) - 1:
        temp_step = chord[this_step]
        for new_step in generate_note_variation(chord[this_step], octave_number):
            chord[-1] = new_step
            inversions.append(chord[:])
        chord[this_step] = temp_step

    else:
        temp_step = chord[this_step]
        for new_step in generate_note_variation(chord[this_step], octave_number):
            chord[this_step] = new_step
            generate_inversions_recursive_step(chord, this_step + 1, inversions, octave_number)
        chord[this_step] = temp_step


def tidied_inversions(inversions : list) -> list:
    res = set()
    result = []
    for inv in inversions:
        this_raw_chord = inv
        this_little_chord = tuple(convert_raw_to_little(this_raw_chord)[1])
        res.add(this_little_chord)
    for inv in res:
        result.append(list(inv))

    return result


def generate_inversions(little_form : list, octaves : int = INF) -> list: # Little form -> little form
    raw_form = formalizer.convert_little_to_raw(little_form)
    diapason = little_form[-1]
    octave_number = ceil(diapason / 12) if octaves == INF else octaves

    inversions = []
    generate_inversions_recursive_step(raw_form, 0, inversions, octave_number)
    return tidied_inversions(inversions)


def are_inversions(chord1, chord2):
    d1 = chord1[-1]
    d2 = chord2[-1]
    o1 = ceil(d1 / 12)
    o2 = ceil(d2 / 12)
    summary_octaves = o1 + 2
    inversions1 = generate_inversions(chord1, o1 + o2)
    return chord2 in inversions1

def get_chord_main_form(chord : list) -> list: # From little to little form
    variations = generate_inversions(chord)
    best_result = INF
    best_variation = None

    for variation in variations:
        this_result = estimate_little_sigma(variation)
        # print(variation, ":", this_result)
        if this_result < best_result:
            best_result = this_result
            best_variation = variation
    return best_variation

def recursive_generate_all_shuffles(prefix : tuple, n, result: set, target) -> None:
    if n == 0:
        result.add(prefix)
        return
    new_data = list(prefix)
    new_data.append(None)
    for next_num in range(target):
        new_data[-1] = next_num
        recursive_generate_all_shuffles(tuple(new_data), n - 1, result, target)

def recursive_generate_all_choices(prefix : tuple, n, result: set, target) -> None:
    if n == 0:
        result.add(prefix)
        return
    new_data = list(prefix)
    new_data.append(None)
    for next_num in range(target):
        if next_num in prefix:
            continue
        new_data[-1] = next_num
        recursive_generate_all_choices(tuple(new_data), n - 1, result, target)


def generate_all_k_permutations(data, length):
    indexes = set()
    recursive_generate_all_choices(tuple(), length, indexes, len(data))
    res = []
    for ind_set in indexes:
        this_res = []
        for index in ind_set:
            this_res.append(data[index])
        res.append(this_res)
    return res


def generate_all_permutations(data, length):
    indexes = set()
    recursive_generate_all_shuffles(tuple(), length, indexes, len(data))
    print(sorted(list(indexes)))
    res = []
    for ind_set in indexes:
        this_res = []
        for index in ind_set:
            this_res.append(data[index])
        res.append(this_res)
    return res


def C_n_k(n, k):
    return factorial(n)  / (factorial(k) * factorial(n - k))

def P_n(n):
    return factorial(n)

def A_n_k(n, k):
    return n ** k

def my_func(n, k):
    return int(factorial(n) / factorial(n - k))

if __name__ == "__main__":
    data = [1, 2, 3, 98, 13, 13, 42, 13]
    k = 2
    choices = sorted(generate_all_permutations(data, k))
    print(A_n_k(len(data), k), len(choices), choices)

    print("Len =", len(generate_inversions([88, 91])))
    print(estimate_little_sigma([28, 31]))
    print(get_chord_by_little_form(get_chord_main_form([28, 31])))
    print(are_inversions([88, 91], [3, 7]))

