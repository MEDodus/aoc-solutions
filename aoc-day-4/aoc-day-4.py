def main():
    with open("xword.txt", "r") as file:
        xword, xmas, directions = (
            [],
            ["X", "M", "A", "S"],
            ["U", "D", "L", "R", "UL", "UR", "DL", "DR"],
        )

        for line in file:
            xword.append(list(line.strip()))

        # Part 1
        part_1(xword, xmas, directions)

        # Part 2
        part_2(xword, xmas, directions)


def part_1(xword, xmas, directions):
    count = 0
    r, c = len(xword), len(xword[0])
    for i in range(r):
        for j in range(c):
            if xword[i][j] == "X":
                for direction in directions:
                    if dfs(xword, i, j, direction, xmas, 0):
                        count += 1
    print(count)


def dfs(xword, i, j, direction, xmas, index):
    r, c = len(xword), len(xword[0])
    if i < 0 or i >= r or j < 0 or j >= c:
        return False

    if index == 3 and xword[i][j] == xmas[index]:
        return True
    elif index < 3 and xword[i][j] == xmas[index]:
        row_col = calc_row_col(direction, i, j)
        return dfs(xword, row_col[0], row_col[1], direction, xmas, index + 1)
    return False


def calc_row_col(direction, i, j):
    if direction == "U":
        return i - 1, j
    elif direction == "D":
        return i + 1, j
    elif direction == "L":
        return i, j - 1
    elif direction == "R":
        return i, j + 1
    elif direction == "UL":
        return i - 1, j - 1
    elif direction == "UR":
        return i - 1, j + 1
    elif direction == "DL":
        return i + 1, j - 1
    elif direction == "DR":
        return i + 1, j + 1


def part_2(xword, xmas, directions):
    count = 0
    r, c = len(xword), len(xword[0])
    for i in range(1, r - 1):
        for j in range(1, c - 1):
            if xword[i][j] == "A":
                if diag_lower(xword, i, j) and diag_upper(xword, i, j):
                    count += 1
    print(count)


def diag_lower(xword, i, j):
    if (
        xword[i - 1][j + 1] == "M"
        and xword[i + 1][j - 1] == "S"
        or xword[i - 1][j + 1] == "S"
        and xword[i + 1][j - 1] == "M"
    ):
        return True
    return False


def diag_upper(xword, i, j):
    if (
        xword[i - 1][j - 1] == "M"
        and xword[i + 1][j + 1] == "S"
        or xword[i - 1][j - 1] == "S"
        and xword[i + 1][j + 1] == "M"
    ):
        return True
    return False


if __name__ == "__main__":
    main()
