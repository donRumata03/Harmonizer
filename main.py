from harmonizer import *


if __name__ == "__main__":


    for chord in test_chords:
        best_form = convert_delta_to_little(test_chords[chord])

        print(chord, ":", get_disharmony_degree(best_form))

    # print(harmonize(tact))

    # print(get_incremental_disharmony_degree([4, 3]))