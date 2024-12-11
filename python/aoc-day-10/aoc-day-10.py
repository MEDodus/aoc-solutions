# Bad practice but it does the job
visited = set()


def main():
    with open("topo-map.txt", "r") as file:
        topo_map = [list(line.strip()) for line in file]
    # print(topo_map)

    # Part 1
    part_1(topo_map)

    # Part 2
    part_2(topo_map)


def part_1(topo_map):
    possible_trails = 0
    for i in range(len(topo_map)):
        for j in range(len(topo_map[i])):
            if topo_map[i][j] == "0":
                # Reset the visited 9s set
                visited.clear()
                dfs_map = topo_map[:]
                trails = dfs_with_set(topo_map, i, j, 0)
                possible_trails += trails

    print(possible_trails)


def part_2(topo_map):
    possible_trails = 0
    for i in range(len(topo_map)):
        for j in range(len(topo_map[i])):
            if topo_map[i][j] == "0":
                dfs_map = topo_map[:]
                trails = dfs(topo_map, i, j, 0)
                possible_trails += trails

    print(possible_trails)


def dfs(topo_map, i, j, index):
    if i < 0 or j < 0 or i >= len(topo_map) or j >= len(topo_map[i]):
        return 0
    if topo_map[i][j] != str(index):
        return 0
    elif topo_map[i][j] == "9":
        return 1
    else:
        # Same reasoning as in dfs_with_set
        topo_map[i][j] = "X"
        possible_trails = 0

        # Check all possible directions if they are in bounds for next number in sequence (index + 1)
        possible_trails += dfs(topo_map, i - 1, j, index + 1)
        possible_trails += dfs(topo_map, i + 1, j, index + 1)
        possible_trails += dfs(topo_map, i, j - 1, index + 1)
        possible_trails += dfs(topo_map, i, j + 1, index + 1)

        # Unvisit the node
        topo_map[i][j] = str(index)
        return possible_trails


def dfs_with_set(topo_map, i, j, index):
    if i < 0 or j < 0 or i >= len(topo_map) or j >= len(topo_map[i]):
        return 0
    if topo_map[i][j] != str(index):
        return 0
    elif topo_map[i][j] == "9" and (i, j) not in visited:
        # Visit the node, no more trail from this distince 0 node can lead to this distinct 9 node
        visited.add((i, j))
        return 1
    else:
        # Mark the node as visited, not this is not the same as the visited set
        # Since we are using recursive dfs, we need to mark for sake of not
        # having a stack overflow, visited set makes sure we don't count a 9 node twice
        topo_map[i][j] = "X"
        possible_trails = 0

        # Check all possible directions if they are in bounds for next number in sequence (index + 1)
        possible_trails += dfs_with_set(topo_map, i - 1, j, index + 1)
        possible_trails += dfs_with_set(topo_map, i + 1, j, index + 1)
        possible_trails += dfs_with_set(topo_map, i, j - 1, index + 1)
        possible_trails += dfs_with_set(topo_map, i, j + 1, index + 1)

        # Unvisit the node
        topo_map[i][j] = str(index)
        return possible_trails


if __name__ == "__main__":
    main()
