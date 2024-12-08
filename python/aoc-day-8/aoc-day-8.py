def main():
    board = []
    with open("board.txt", "r") as file:
        board = [list(line.strip()) for line in file]

    # Part 1
    part_1(board)

    # Part 2
    part_2(board)


def part_1(board):
    # For each row in matches, have coordinates for each matching frequency antenna
    matches = get_matches(board)
    # print(matches)

    # Iterate across all combinations of antennas of the same type and check for antinodes
    # Since we need them to be unique, we will use a set to check for duplicates
    antinodes = set()
    antinode_count = 0
    for match_list in matches:
        for i in range(len(match_list)):
            for j in range(i + 1, len(match_list)):
                # Get the coordinates of the two antennas
                (x1, y1) = match_list[i]
                (x2, y2) = match_list[j]

                # Get the distance between the two antennas
                dx = x2 - x1
                dy = y2 - y1

                # Check antinodes by extending the line in both directions
                ax1, ay1 = x1 - dx, y1 - dy
                ax2, ay2 = x2 + dx, y2 + dy

                if (
                    0 <= ax1 < len(board)
                    and 0 <= ay1 < len(board[0])
                    and (ax1, ay1) not in antinodes
                ):
                    antinodes.add((ax1, ay1))
                    antinode_count += 1
                if (
                    0 <= ax2 < len(board)
                    and 0 <= ay2 < len(board[0])
                    and (ax2, ay2) not in antinodes
                ):
                    antinodes.add((ax2, ay2))
                    antinode_count += 1
    print(antinode_count)


def part_2(board):
    # For each row in matches, have coordinates for each matching frequency antenna
    matches = get_matches(board)
    # print(matches)

    # Iterate across all combinations of antennas of the same type and check for antinodes
    # Since we need them to be unique, we will use a set to check for duplicates
    antinodes = set()
    antinode_count = 0
    for match_list in matches:
        for i in range(len(match_list)):
            for j in range(i + 1, len(match_list)):
                # Get the coordinates of the two antennas
                (x1, y1) = match_list[i]
                (x2, y2) = match_list[j]

                # Repeatedly extend the line in both directions until we reach the edge of the board
                antinode_count += get_line_antinodes(board, x1, y1, x2, y2, antinodes)

    # Since all antennas are guaranteed to have a pair, they are all antinodes add them
    for match_list in matches:
        antinode_count += len(match_list)

    print(antinode_count)


def get_line_antinodes(board, x1, y1, x2, y2, antinodes):
    antinode_count = 0

    # Get the distance between the two antennas
    dx = x2 - x1
    dy = y2 - y1

    # Check antinodes by extending the line in both directions
    ax1, ay1 = x1 - dx, y1 - dy
    ax2, ay2 = x2 + dx, y2 + dy

    while 0 <= ax1 < len(board) and 0 <= ay1 < len(board[0]):
        # For simplicity, only add antinodes where an antenna does not exist
        if (ax1, ay1) not in antinodes and board[ax1][ay1] == ".":
            antinodes.add((ax1, ay1))
            antinode_count += 1
        ax1 -= dx
        ay1 -= dy

    while 0 <= ax2 < len(board) and 0 <= ay2 < len(board[0]):
        # For simplicity, only add antinodes where an antenna does not exist
        if (ax2, ay2) not in antinodes and board[ax2][ay2] == ".":
            antinodes.add((ax2, ay2))
            antinode_count += 1
        ax2 += dx
        ay2 += dy

    return antinode_count


def get_matches(board):
    matches = []
    visited_matches = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            # Check we are at an antenna and haven't visited any of it's type yet
            if board[i][j] != "." and (i, j) not in visited_matches:
                match = bfs(board, i, j)
                matches.append(match)
                # Add all antenna of the same type to visited_matches
                visited_matches.update(match)

    return matches


# Breadth-first search to find all matching antennas
def bfs(board, i, j):
    visited = set()
    queue = [(i, j)]
    match_char = board[i][j]
    match_list = []

    # While we have nodes left to visit
    while queue:
        x, y = queue.pop(0)
        if 0 <= x < len(board) and 0 <= y < len(board[0]) and (x, y) not in visited:

            # Add all neighbors, 4 total neighbors for any given node
            queue.append((x + 1, y))
            queue.append((x - 1, y))
            queue.append((x, y + 1))
            queue.append((x, y - 1))

            # Visit the node
            visited.add((x, y))

            # If the node is a match, add it to the match list
            if board[x][y] == match_char:
                match_list.append((x, y))

    return match_list


if __name__ == "__main__":
    main()
