def main():
    with open("board.txt", "r") as file:
        board = []
        for line in file:
            board.append(list(line.strip()))
    print(count_x(board))
    print(count_x_bfs(board))


def count_x_bfs(board):
    count = 0
    visited = set()
    queue = [(0, 0)]
    while queue:
        x, y = queue.pop(0)
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or (x, y) in visited:
            continue
        elif board[x][y] == "X":
            count += 1
        queue.append((x + 1, y))
        queue.append((x - 1, y))
        queue.append((x, y + 1))
        queue.append((x, y - 1))
        visited.add((x, y))
    return count


def count_x(board):
    count = 0
    for row in board:
        count += row.count("X")
    return count


if __name__ == "__main__":
    main()
