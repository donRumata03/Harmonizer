# from dictionary import *

INF = 1 << 30

def convert_raw_to_little(data : list): # [1, 2, 6, 9] -> [4, 7] it means 0, delta1 = ...
    sdata = sorted(data)
    res = []
    base = sdata[0]
    for note in sdata[1:]:
        res.append(note - base)
    return base, res

def convert_delta_to_little(data : list) -> list:
    prepared = []
    summ = 0
    for v in data:
        summ += v
        prepared.append(summ)
    return prepared

def convert_little_to_raw(data : list, offset = INF) -> list:
    o = 0 if offset == INF else offset
    result = [o]
    for note in data:
        result.append(note + o)
    return sorted(result)


def convert_little_to_delta(data : list) -> list: # [4, 7] -> [4, 3]
    last = data[0]
    res = [data[0]]
    for i in data[1:]:
        res.append(i - last)
        last = i
    return res

def convert_raw_to_delta(data : list):
    return convert_little_to_delta(convert_raw_to_little(data)[1])


def convert_delta_to_raw(data : list) -> list:
    return convert_little_to_raw(convert_delta_to_little(data))

def are_raw_chords_same(c1 : list, c2 : list): # Raw form
    return convert_raw_to_delta(c1) == convert_raw_to_delta(c2)

if __name__ == "__main__":
    print(convert_little_to_raw([-8, -5]))
