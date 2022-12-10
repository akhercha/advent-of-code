INPUT_FILE = "input.txt"


def part_two(lines):
    l_calories = []
    current_calories = 0
    for line in lines:
        if len(line) == 0:
            l_calories.append(current_calories)
            current_calories = 0
            continue
        current_calories += int(line)
    l_calories = sorted(l_calories)
    print(sum(l_calories[-3:]))


def part_one(lines):
    max_calories = 0
    current_calories = 0
    for line in lines:
        if len(line) == 0:
            if current_calories > max_calories:
                max_calories = current_calories
            current_calories = 0
            continue
        current_calories += int(line)
    print(max_calories)


def main():
    with open(INPUT_FILE, "r") as f:
        l_input = [line.rstrip() for line in f.readlines()]
    part_one(l_input)
    part_two(l_input)


if __name__ == "__main__":
    main()
