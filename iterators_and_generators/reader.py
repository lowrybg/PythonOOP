def read_next(*args):
    for el in args:
        for p in el:
            yield p


for item in read_next("string", (2,), {"d": 1, "I": 2, "c": 3, "t": 4}):
    print(item, end='')
