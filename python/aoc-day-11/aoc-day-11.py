import time

memoize = {}


def main():
    stones = []
    with open("stones.txt", "r") as file:
        for line in file:
            stones += line.strip().split()
    print(stones)

    # Recursive solution using map to memoize
    time_taken = time.time()
    sum = 0
    for stone in stones:
        new_stone = stone[:]
        sum += recursive_blink(new_stone, 75)
    print(sum)
    print(f"Time taken for recursive solution: {time.time() - time_taken}")

    # Iterative solution
    time_taken = time.time()
    stone_map = {}
    for stone in stones:
        # add 1 to key if it exists, else add key to map
        if stone in stone_map:
            stone_map[stone] += 1
        else:
            stone_map[stone] = 1

    for _ in range(75):
        stone_map = part_2(stone_map)
    # print(stone_map)
    print(sum(stone_map.values()))
    print(f"Time taken for iterative solution: {time.time() - time_taken}")

    # Part 1
    # part_1(stones, 75)


def recursive_blink(stone, blinks):
    if (stone, blinks) in memoize:
        return memoize[(stone, blinks)]
    if blinks == 0:
        memoize[(stone, blinks)] = 1
        return 1  # base case we are at a leaf node in the recursion tree
    elif stone == "0":
        memoize[(stone, blinks)] = recursive_blink("1", blinks - 1)
        return memoize[(stone, blinks)]
    elif len(stone) % 2 == 0:
        first_half = stone[: len(stone) // 2]
        second_half = stone[len(stone) // 2 :]
        if second_half[0] == "0":
            second_half = remove_leading_zeros(second_half)
        memoize[(stone, blinks)] = recursive_blink(
            first_half, blinks - 1
        ) + recursive_blink(second_half, blinks - 1)
        return memoize[(stone, blinks)]
    else:
        num = int(stone)
        num *= 2024
        memoize[(stone, blinks)] = recursive_blink(str(num), blinks - 1)
        return memoize[(stone, blinks)]


def part_1(stones, blinks):
    for i in range(blinks):
        start_time = time.time()
        new_stones = []
        for j in range(len(stones)):
            if stones[j] == "0":
                new_stones.append("1")
            elif len(stones[j]) % 2 == 0:
                first_half = stones[j][: len(stones[j]) // 2]
                second_half = stones[j][len(stones[j]) // 2 :]
                if second_half[0] == "0":
                    second_half = remove_leading_zeros(second_half)
                new_stones.append(first_half)
                new_stones.append(second_half)
            else:
                num = int(stones[j])
                num *= 2024
                new_stones.append(str(num))
        print(f"Time taken for iteration {i + 1}: {time.time() - start_time}")
        stones = new_stones

    print(len(stones))


def part_2(stone_map):
    new_map = {}

    for key, value in stone_map.items():
        # Rule 1 check for 0's
        if key == "0":
            if "1" not in new_map:
                new_map["1"] = 0
            new_map["1"] += value
        elif len(str(key)) % 2 == 0:  # Rule 2 check for even length nums
            first_half = key[: len(key) // 2]
            second_half = remove_leading_zeros(key[len(key) // 2 :])
            if first_half not in new_map:
                new_map[first_half] = 0
            if second_half not in new_map:
                new_map[second_half] = 0
            new_map[first_half] += value
            new_map[second_half] += value
        else:  # Rule 3 f(x) = x * 2024
            new_key = str(int(key) * 2024)
            if new_key not in new_map:
                new_map[new_key] = 0
            new_map[new_key] += value

    return new_map


def remove_leading_zeros(num):
    for i in range(len(num)):
        if num[i] != "0":
            return num[i:]
    return "0"


if __name__ == "__main__":
    main()
