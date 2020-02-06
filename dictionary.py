import formalizer
import json

test_chords = {
    "Major ( C )" : [4, 3],
    "Minor ( Cm )" : [3, 4],

    "Decreased ( aka Cdim )" : [3, 3],
    "Increased ( aka Caug )" : [4, 4],

    "Big major sept ( aka Cmaj7 )" : [4, 3, 4],
    "Little major sept ( aka C7 )" : [4, 3, 3],

    "Little minor sept ( aka Cm7 )" : [3, 4, 3],
    "Big minor sept ( aka Cm#7 )" : [3, 4, 4],

    "Little decreased sept ( aka Cm7b5 )" : [3, 3, 4],
    "Decreased sept ( aka Cdim7 )" : [3, 3, 3],
    "Increased sept ( aka Caug7 )" : [4, 4, 3],

    "Sus 2 ( aka Csus2 )" : [2, 5],
    "Sus 4 ( aka Csus2 )" : [5, 2],

    "Nonachord ( aka Cmaj9 )" : [4, 3, 4, 3]
}

def print_as_json(data):
    print(json.dumps(data, indent=3, ensure_ascii=False))

def get_chord_by_delta_form(delta_form):
    from inverser import generate_inversions, get_chord_main_form
    proper_name = "Unknown"
    for name in test_chords:
        poss_chord = test_chords[name]
        if poss_chord == delta_form:
            proper_name = name
            break

    little_form = formalizer.convert_delta_to_little(delta_form)

    return \
        {"name" : proper_name,
            "little form" : little_form,
            "delta form" : delta_form,
            "raw form" : formalizer.convert_delta_to_raw(delta_form),
            "main form" : get_chord_main_form(little_form),
            "inversions" : generate_inversions(little_form)
        }

def get_chord_by_little_form(little_form):
    return get_chord_by_delta_form(formalizer.convert_little_to_delta(little_form))

def get_chord_by_raw_form(raw_form):
    return get_chord_by_delta_form(formalizer.convert_raw_to_delta(raw_form))


if __name__ == "__main__":
    print_as_json(get_chord_by_raw_form([17, 21]))