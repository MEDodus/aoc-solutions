def main():
    with open("input.txt", "r") as file:
        file_list = []
        for line in file:
            file_list += list(line.strip())

    # Part 1
    part_1(file_list)

    # Part 2
    part_2(file_list)


def part_1(file_list):
    memory = []

    # Technically a list, but the location in the list is a key of sorts, and the value is the index
    free_space_map = []
    file_location_map = []
    for i in range(len(file_list)):
        if i % 2 == 0:  # Get the file count for current file
            file_count = int(file_list[i])
            id = i // 2
            for _ in range(file_count):
                memory.append(str(id))
                # append index of file to file_location_map
                file_location_map.append(len(memory) - 1)
        else:  # Get the free space count between files
            free_space = int(file_list[i])
            for _ in range(free_space):
                memory.append(".")
                # append index of free space to free_space_map
                free_space_map.append(len(memory) - 1)

    # Shift files to free space until all files are to the left of the first free space
    while not shifted(free_space_map, file_location_map):
        memory = shift(memory, free_space_map, file_location_map)

    print_checksum(memory)


def part_2(file_list):
    memory = []
    free_space_map = []
    file_location_map = []
    for i in range(len(file_list)):
        if i % 2 == 0:  # Get the file count for current file
            file_count = int(file_list[i])
            id = i // 2
            for _ in range(file_count):
                memory.append(str(id))
            # append tuple containing start and end index of file to file_location_map
            file_location_map.append((len(memory) - file_count, len(memory) - 1))
        else:  # Get the free space count between files
            free_space = int(file_list[i])
            for _ in range(free_space):
                memory.append(".")
            # append tuple containing start and end index of free space to free_space_map
            free_space_map.append((len(memory) - free_space, len(memory) - 1))

    # Try shifting last file, remove it, and repeat
    while len(file_location_map) > 0:
        memory = shift_file(memory, free_space_map, file_location_map)

    print_checksum(memory)


def print_checksum(memory):
    checksum = 0
    # Could optimize for part 1 by ending once we reach the first free space, but I'm lazy
    for i in range(len(memory)):
        if memory[i] == ".":
            continue
        checksum += i * int(memory[i])
    print(checksum)


def shift_file(memory, free_space_map, file_location_map):
    # Get next rightmost file to check if it can be shifted to free space
    file_location = file_location_map.pop(len(file_location_map) - 1)
    file_size = file_location[1] - file_location[0] + 1

    for i in range(len(free_space_map)):

        free_space_location = free_space_map[i]

        # Check if file can be shifted to free space
        if can_shift(file_location, free_space_location):
            for j in range(file_size):
                # Swap file with free space
                memory[free_space_location[0] + j], memory[file_location[0] + j] = (
                    memory[file_location[0] + j],
                    memory[free_space_location[0] + j],
                )

            # Update free space by reducing file size from beginning of free space chunk
            free_space_map[i] = (
                free_space_location[0] + file_size,
                free_space_location[1],
            )
            return memory
    return memory


def can_shift(file_location, free_space_location):
    file_size, free_space_size = (
        file_location[1] - file_location[0] + 1,
        free_space_location[1] - free_space_location[0] + 1,
    )
    return file_size <= free_space_size and file_location[0] > free_space_location[0]


def shifted(free_space_map, file_location_map):
    # Get last file location and first free space location
    free_space_location = free_space_map[0]
    file_location = file_location_map[len(file_location_map) - 1]

    # Since free space should be contiguous, we can check that all files occur before the first free space location
    return file_location < free_space_location


def shift(memory, free_space_map, file_location_map):
    free_space_location = free_space_map.pop(0)
    file_location = file_location_map.pop(len(file_location_map) - 1)
    memory[free_space_location] = memory[file_location]
    memory[file_location] = "."
    return memory


if __name__ == "__main__":
    main()
