INPUT_FILE = "input.txt"

OFFSET_ASCII = ord("A")


def value_of_element(elt):
    useless_chars_offset = 6 if elt.isupper() else 0
    return ord(elt.swapcase()) - OFFSET_ASCII + 1 - useless_chars_offset


def part_two(lines):
    sum_priorities = 0
    for rucksacks in zip(lines[::3], lines[1::3], lines[2::3]):
        rucksacks = [set(rucksack) for rucksack in rucksacks]
        common_elt = set.intersection(*rucksacks).pop()
        sum_priorities += value_of_element(common_elt)
    print(sum_priorities)


def part_one(lines):
    sum_priorities = 0
    for rucksack in lines:
        n = len(rucksack) // 2
        first_compartment = set(rucksack[:n])
        second_compartment = set(rucksack[n:])
        common_elt = first_compartment.intersection(second_compartment).pop()
        sum_priorities += value_of_element(common_elt)
    print(sum_priorities)


def main():
    with open(INPUT_FILE, "r") as f:
        l_input = [line.rstrip() for line in f.readlines()]
    part_one(l_input)
    part_two(l_input)


if __name__ == "__main__":
    main()
