INPUT_FILE = "input.txt"

MOVES_OPPONENT = ["A", "B", "C"]
MOVES_ME = ["X", "Y", "Z"]


def round_result(opponent, me):
    me_idx = MOVES_ME.index(me)
    op_idx = MOVES_OPPONENT.index(opponent)
    my_shape_score = me_idx + 1
    outcome_score = 3 if op_idx == me_idx else 0
    if MOVES_ME[(op_idx + 1) % len(MOVES_ME)] == me:
        outcome_score = 6
    return my_shape_score + outcome_score


def part_two(lines):
    score = 0
    for line in lines:
        opponent, me = line.split(" ")
        me = MOVES_ME[
            (MOVES_OPPONENT.index(opponent) + MOVES_ME.index(me) - 1)
            % len(MOVES_OPPONENT)
        ]
        score += round_result(opponent, me)
    print(score)


def part_one(lines):
    score = 0
    for line in lines:
        opponent, me = line.split(" ")
        score += round_result(opponent, me)
    print(score)


def main():
    with open(INPUT_FILE, "r") as f:
        l_input = [line.rstrip() for line in f.readlines()]
    part_one(l_input)
    part_two(l_input)


if __name__ == "__main__":
    main()
