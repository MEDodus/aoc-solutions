def main():
    with open("map.txt", "r") as file:
        map = []
        for line in file:
            map.append(list(line.strip()))

        # print_state_of_map(map)

        # Find initial guard position
        guard_position = (-1, -1, "N")
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == "^":
                    guard_position = (i, j, "N")
                    break

        # Uncomment one part at a time to run and comment the other part
        # Part 1
        part_1(map, guard_position)

        # Part 2
        # part_2(map, guard_position)


def part_1(map, guard_position):
    while guard_is_in_map(map, guard_position):
        # print_state_of_map(map)
        map[guard_position[0]][guard_position[1]] = "X"
        guard_position = move_forward(map, guard_position)
    # print_state_of_map(map)

    distinct_positions = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "X":
                distinct_positions += 1
    print(distinct_positions)


def part_2(map, guard_position):
    paradox_count = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == ".":
                map[i][j] = "#"
                new_map = [row[:] for row in map]
                if is_guard_stuck_in_loop(new_map, guard_position):
                    paradox_count += 1
                map[i][j] = "."
    print(paradox_count)


def is_guard_stuck_in_loop(map, guard_position):
    step_count, match_count = 0, -1
    stuck_in_loop = False
    while guard_is_in_map(map, guard_position):
        if match_count == step_count:
            # print("Guard is stuck in loop")
            return True
        if map[guard_position[0]][guard_position[1]] == "X":
            if match_count == -1:
                match_count = 0
                # print("Guard is stepping on previous step start counting, if we match " + str(step_count) + " steps, then guard is stuck in loop")
            match_count += 1
        else:
            map[guard_position[0]][guard_position[1]] = "X"
            step_count += 1
        guard_position = move_forward(map, guard_position)
    return stuck_in_loop


def guard_is_in_map(map, position):
    row, col, direction = position
    return row >= 0 and row < len(map) and col >= 0 and col < len(map[0])


def print_state_of_map(map):
    for row in map:
        print(row)
    print()


def inbound(map, row, col):
    return row >= 0 and row < len(map) and col >= 0 and col < len(map[0])


def move_forward(map, position):
    row, col, direction = position
    if direction == "N":
        if inbound(map, row - 1, col) and map[row - 1][col] == "#":
            position = (row, col, "E")
            return move_forward(map, position)
        row -= 1
    elif direction == "S":
        if inbound(map, row + 1, col) and map[row + 1][col] == "#":
            position = (row, col, "W")
            return move_forward(map, position)
        row += 1
    elif direction == "W":
        if inbound(map, row, col - 1) and map[row][col - 1] == "#":
            position = (row, col, "N")
            return move_forward(map, position)
        col -= 1
    elif direction == "E":
        if inbound(map, row, col + 1) and map[row][col + 1] == "#":
            position = (row, col, "S")
            return move_forward(map, position)
        col += 1
    return (row, col, direction)


if __name__ == "__main__":
    main()
