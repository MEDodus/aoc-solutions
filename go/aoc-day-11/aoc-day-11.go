package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
	"strings"
	"time"
)

type Tuple struct {
	stone  string
	blinks int
}

func main() {
	file, err := os.Open("stones.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer file.Close()

	stones := []string{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		stones = strings.Split(scanner.Text(), " ")
		// fmt.Println(stones)
	}

	start := time.Now()
	sum := 0
	memoize := make(map[Tuple]int)
	for _, stone := range stones {
		sum += get_count(stone, 75, memoize)
	}
	fmt.Println(sum)
	fmt.Println(fmt.Sprintf("Execution time: %s", time.Since(start)))
}

func get_count(stone string, blinks int, memoize map[Tuple]int) int {
	value, ok := memoize[Tuple{stone, blinks}]
	if ok {
		return value
	}

	if blinks == 0 {
		return 1
	} else if stone == "0" {
		memoize[Tuple{stone, blinks}] = get_count("1", blinks-1, memoize)
		return memoize[Tuple{stone, blinks}]
	} else if len(stone)%2 == 0 {
		first_half := stone[:len(stone)/2]
		second_half := stone[len(stone)/2:]
		second_half = remove_leading_zeros(second_half)
		memoize[Tuple{stone, blinks}] = get_count(first_half, blinks-1, memoize) + get_count(second_half, blinks-1, memoize)
		return memoize[Tuple{stone, blinks}]
	} else {
		stone_bigint := new(big.Int)
		stone_bigint, ok = stone_bigint.SetString(stone, 10)
		if !ok {
			fmt.Println("Error converting stone to big.Int")
			return 0
		}
		multiplier := big.NewInt(2024)
		stone_bigint.Mul(stone_bigint, multiplier)
		memoize[Tuple{stone, blinks}] = get_count(stone_bigint.String(), blinks-1, memoize)
		return memoize[Tuple{stone, blinks}]
	}
}

func remove_leading_zeros(stone string) string {
	for i, c := range stone {
		if c != '0' {
			return stone[i:]
		}
	}
	return "0"
}
