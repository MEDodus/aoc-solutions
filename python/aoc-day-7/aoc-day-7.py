def main():
    with open("calibration.txt", "r") as file:
        total_sum = 0

        # txt file is a list of numbers in format #: # # #, after the colon we can have any number of numbers
        before_colon, after_colon = [], []
        for line in file:
            numbers = line.strip().split(":")
            before_colon.append(int(numbers[0]))
            after_colon.append([int(num) for num in numbers[1].split()])

    # Part 1
    part_1(before_colon, after_colon, total_sum)

    # Part 2
    part_2(before_colon, after_colon, total_sum)


def part_1(before_colon, after_colon, total_sum):
    # For each line of numbers
    for i in range(len(before_colon)):
        # Check if the sum of the numbers after the colon is equal to the number before the colon
        numbers, index, end_index, target, current_sum = (
            after_colon[i],
            1,
            len(after_colon[i]),
            before_colon[i],
            after_colon[i][0],
        )
        if calc_add_mult(numbers, index, end_index, target, current_sum):
            # If it is, add the number before the colon to the total sum
            total_sum += before_colon[i]
    print(total_sum)


def part_2(before_colon, after_colon, total_sum):
    # For each line of numbers
    for i in range(len(before_colon)):
        # Check if the sum of the numbers after the colon is equal to the number before the colon
        numbers, index, end_index, target, current_sum = (
            after_colon[i],
            1,
            len(after_colon[i]),
            before_colon[i],
            after_colon[i][0],
        )
        if calc_add_mult_pipe(numbers, index, end_index, target, current_sum):
            # If it is, add the number before the colon to the total sum
            total_sum += before_colon[i]
    print(total_sum)


# Recursive function to check all possible combinations of addition and multiplication
def calc_add_mult(numbers, idx, end_idx, total_sum, current_sum):
    # Base case, if we have reached the end of the list of numbers, check running sum from current sum against total sum
    if idx >= end_idx:
        return current_sum == total_sum
    # Check all possible combinations of addition and multiplication, 2 ^ n possibilities
    return calc_add_mult(
        numbers, idx + 1, end_idx, total_sum, current_sum + numbers[idx]
    ) or calc_add_mult(numbers, idx + 1, end_idx, total_sum, current_sum * numbers[idx])


# Recursive function to check all possible combinations of addition, multiplication and concatenation
def calc_add_mult_pipe(numbers, idx, end_idx, total_sum, current_sum):
    # Base case, if we have reached the end of the list of numbers, check running sum from current sum against total sum
    if idx >= end_idx:
        return current_sum == total_sum
    # Check all possible combinations of addition, multiplication and concatenation, 3 ^ n possibilities
    return (
        calc_add_mult_pipe(
            numbers, idx + 1, end_idx, total_sum, current_sum + numbers[idx]
        )
        or calc_add_mult_pipe(
            numbers, idx + 1, end_idx, total_sum, current_sum * numbers[idx]
        )
        or calc_add_mult_pipe(
            numbers,
            idx + 1,
            end_idx,
            total_sum,
            int(str(current_sum) + str(numbers[idx])),
        )
    )


if __name__ == "__main__":
    main()
