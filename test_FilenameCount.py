import pytest


def test_find_file_names():
    with open("small.dat", mode="r") as f:
        count = 0
        f.seek(0)
        line = f.readline()
        while True:
            if line == '':
                break
            else:
                ls = line.rstrip().split(" ")
                for s in ls:
                    if s.startswith("T") or s.endswith("S"):
                        print(s)
                        count += 1
            line = f.readline()
    print("total count of files = {}".format(count))


#test_find_file_names()
