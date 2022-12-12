from string import ascii_uppercase

INPUT_FILE = "input.txt"


def initialize_stacks(lines):
    l_stacks = [[] for _ in range(int(lines[-1][-2]))]
    crates_idx_in_strt = list(range(1, len(l_stacks) * 4 + 1, 4))
    for line in lines:
        for i, idx in enumerate(crates_idx_in_strt):
            if line[idx] in ascii_uppercase:
                l_stacks[i].insert(0, line[idx])
    return l_stacks


def get_numbers_from_procedure(line_op):
    return list(map(int, [elt for elt in line_op.split(" ") if elt.isdigit()]))


def part_two(lines):
    border_stacks_procedures = lines.index("")
    l_stacks = initialize_stacks(lines[:border_stacks_procedures])
    for procedure in lines[border_stacks_procedures + 1 :]:
        nb_to_move, start, end = get_numbers_from_procedure(procedure)
        to_move = l_stacks[start - 1][-nb_to_move:]
        l_stacks[start - 1] = l_stacks[start - 1][:-nb_to_move]
        l_stacks[end - 1] += to_move
    print("".join(elements[-1] for elements in l_stacks if len(elements) > 0))


def part_one(lines):
    border_stacks_procedures = lines.index("")
    l_stacks = initialize_stacks(lines[:border_stacks_procedures])
    for procedure in lines[border_stacks_procedures + 1 :]:
        nb_to_move, start, end = get_numbers_from_procedure(procedure)
        to_move = l_stacks[start - 1][-nb_to_move:]
        l_stacks[start - 1] = l_stacks[start - 1][:-nb_to_move]
        l_stacks[end - 1] += reversed(to_move)
    print("".join(elements[-1] for elements in l_stacks if len(elements) > 0))


def main():
    with open(INPUT_FILE, "r") as f:
        l_input = [line[: len(line) - 1] for line in f.readlines()]
    part_one(l_input)
    part_two(l_input)


if __name__ == "__main__":
    main()
