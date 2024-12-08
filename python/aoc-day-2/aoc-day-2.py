def main():
    with open("reports.txt", "r") as file:
        reports = []
        for line in file:
            reports.append(line.strip().split())

        # Part 1
        part_1(reports)

        # Part 2
        part_2(reports)


def part_1(reports):
    safe_reports = 0
    for report in reports:
        if check_report(report):
            safe_reports += 1
    print(safe_reports)


def part_2(reports):
    safe_reports = 0
    for report in reports:
        if remove_level(report):
            safe_reports += 1
    print(safe_reports)


def check_report(report):
    increasing_flag = None
    for i in range(len(report) - 1):
        level = int(report[i])
        next_level = int(report[i + 1])

        # Check if the difference is within bounds
        difference = abs(level - next_level)
        if difference < 1 or difference > 3:
            return False

        # Determine increasing or decreasing trend
        if increasing_flag is None:
            increasing_flag = level < next_level
        elif increasing_flag != (level < next_level):
            return False

    return True


def remove_level(report):
    for i in range(len(report)):
        removed_report = report[:i] + report[i + 1 :]
        if check_report(removed_report):
            return True
    return False


if __name__ == "__main__":
    main()
