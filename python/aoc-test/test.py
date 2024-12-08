def main():
    word_count = {}
    with open("input.txt", "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    for word, count in word_count.items():
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
