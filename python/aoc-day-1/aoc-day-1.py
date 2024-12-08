def main():
    totalDiff = 0
    a, b = [], []

    # Read numbers to each list
    with open("list.txt", "r") as file:
        for line in file:
            left, right = line.split()
            a.append(int(left))
            b.append(int(right))

    # Sort the lists
    a.sort()
    b.sort()

    # Part 1
    part_1(a, b, totalDiff)

    # Part 2
    part_2(a, b)


def part_1(a, b, totalDiff):
    for i in range(len(a)):
        totalDiff += abs(b[i] - a[i])
    print(totalDiff)


def part_2(a, b):
    repeatMap = {}
    for i in range(len(a)):
        repeatCount = 0
        num = a[i]
        repeatMap[num] = 0
        for j in range(len(a)):
            num2 = b[j]
            if num == num2:
                repeatCount += 1
        repeatMap[num] += repeatCount
    result = [key * value for key, value in repeatMap.items() if value > 0]
    print(sum(result))


if __name__ == "__main__":
    main()
