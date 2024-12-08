def main():

    # Read the input file, and store the rules and numbers
    with open("input.txt", "r") as file:
        rules, numbers = [], []
        for line in file:
            if "|" in line:
                rules.append(line.strip().split("|"))
            elif "," in line:
                numbers.append(line.strip().split(","))

        # Part 1
        part_1(rules, numbers)

        # Part 2
        part_2(rules, numbers)


def part_1(rules, numbers):
    # Get correctly ordered numbers, sum the middle number in list
    sum = 0
    for number_list in numbers:
        if check_order(rules, number_list):
            sum += int(number_list[len(number_list) // 2])
    print(sum)


def part_2(rules, numbers):
    # Get incorrectly ordered numbers, sum the middle number in list after sorting
    sum = 0
    for number_list in numbers:
        if not check_order(rules, number_list):
            sorted_list = reorder(rules, number_list)
            sum += int(sorted_list[len(sorted_list) // 2])
    print(sum)


def reorder(rules, number_list):
    # Reorder the number list until all rules are satisfied
    sorted_list = number_list[:]
    changed = True

    while changed:
        changed = False
        for rule in rules:
            before, after = rule[0], rule[1]
            if before in sorted_list and after in sorted_list:
                before_index = sorted_list.index(before)
                after_index = sorted_list.index(after)
                if before_index > after_index:
                    # Swap to enforce the rule
                    sorted_list[before_index], sorted_list[after_index] = (
                        sorted_list[after_index],
                        sorted_list[before_index],
                    )
                    changed = True
    return sorted_list


def check_order(rules, number_list):
    # Check if the number list is in the correct order
    for rule in rules:
        if not check_rule(rule, number_list):
            return False
    return True


def check_rule(rule, number_list):
    # Check if the rule is satisfied
    before_ordering = rule[0]
    after_ordering = rule[1]
    before_index = (
        number_list.index(before_ordering) if before_ordering in number_list else -1
    )
    after_index = (
        number_list.index(after_ordering) if after_ordering in number_list else -1
    )
    return before_index < after_index or before_index == -1 or after_index == -1


if __name__ == "__main__":
    main()
