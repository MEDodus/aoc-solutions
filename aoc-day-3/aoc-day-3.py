import re


def main():
    # Read corrupted instructions
    with open("instructions.txt", "r") as file:
        corrupted_instructions = []
        for line in file:
            corrupted_instructions.append(line.strip())

    # Part 1
    part_1(corrupted_instructions)

    # Part 2
    part_2(corrupted_instructions)


def part_1(corrupted_instructions):
    instructions = []
    for corrupted_line in corrupted_instructions:
        # Find all valid instructions and append them to instructions list
        instructions += re.findall(r"mul\(\d{1,3},\d{1,3}\)", corrupted_line)

    multiplication_result = 0
    for instruction in instructions:
        # Find the two numbers in the instruction
        numbers = re.findall(r"\d{1,3}", instruction)
        multiplication_result += int(numbers[0]) * int(numbers[1])
    print(multiplication_result)


def part_2(corrupted_instructions):
    instructions = []
    for corrupted_line in corrupted_instructions:
        # Find all valid instructions and append them to instructions list
        instructions += re.findall(
            r"mul\(\d{1,3},\d{1,3}\)|\bdo\(\)|don't\(\)", corrupted_line
        )

    multiplication_result, index = 0, 0
    while index < len(instructions):
        instruction = instructions[index]
        if instruction == "don't()":
            # Skip mul() instructions after don't()
            index = skip_to_next_do(instructions, index)
        elif instruction == "do()":
            index += 1
        else:
            # Find the two numbers in the instruction
            numbers = re.findall(r"\d{1,3}", instruction)
            multiplication_result += int(numbers[0]) * int(numbers[1])
            index += 1
    print(multiplication_result)


def skip_to_next_do(instructions, i):
    while i < len(instructions):
        if instructions[i] == "do()":
            return i + 1
        i += 1
    return i


if __name__ == "__main__":
    main()
