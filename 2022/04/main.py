INPUT_FILE = "input.txt"


def part_two(lines):
    useless_pairs = 0
    for assigments in lines:
        pairs = assigments.split(",")
        s1, e1 = map(int, pairs[0].split("-"))
        set1 = set(range(s1, e1 + 1))
        s2, e2 = map(int, pairs[1].split("-"))
        set2 = set(range(s2, e2 + 1))
        if len(set1.intersection(set2)) > 0:
            useless_pairs += 1
    print(useless_pairs)


def part_one(lines):
    useless_pairs = 0
    for assigments in lines:
        pairs = assigments.split(",")
        s1, e1 = map(int, pairs[0].split("-"))
        set1 = set(range(s1, e1 + 1))
        s2, e2 = map(int, pairs[1].split("-"))
        set2 = set(range(s2, e2 + 1))
        if set1.issubset(set2) or set2.issubset(set1):
            useless_pairs += 1
    print(useless_pairs)


def main():
    with open(INPUT_FILE, "r") as f:
        l_input = [line.rstrip() for line in f.readlines()]
    part_one(l_input)
    part_two(l_input)


if __name__ == "__main__":
    main()
