INPUT_FILE = "input.txt"


def part_two(lines):
    pass


def part_one(lines):
    pass


def main():
    with open(INPUT_FILE, "r") as f:
        l_input = [line.rstrip() for line in f.readlines()]
    part_one(l_input)
    part_two(l_input)


if __name__ == "__main__":
    main()
