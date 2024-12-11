package main

import (
	"bufio"   // Scanner for reading file
	"fmt"     // Println, Printf, Sprintf, etc.
	"os"      // File operations
	"strconv" // Atoi, Itoa, etc.
)

type Tuple struct {
	x int
	y int
}

func main() {
	file, err := os.Open("topo-map.txt")
	if err != nil {
		fmt.Println("Error reading file: ", err)
		return
	}
	// Close the file when the function returns
	defer file.Close()

	// slice of byte slices
	matrix := [][]byte{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		// text line from the file
		text := scanner.Text()

		// convert the text line to a byte array
		row := []byte(text)

		// append the byte array to the matrix
		matrix = append(matrix, row)
	}

	// Part 1
	part_1(matrix)

	// Part 2
	part_2(matrix)
}

func part_1(matrix [][]byte) {
	trail_count := 0
	visited := make(map[Tuple]bool)
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[i]); j++ {
			// conversion from byte to char is implicit
			if matrix[i][j] == '0' {

				// clear visited map
				visited = make(map[Tuple]bool)
				trail_count += dfs_with_set(matrix, i, j, 0, visited)
			}
		}
	}
	fmt.Println("Number of trails (Part 1): ", trail_count)
}

func part_2(matrix [][]byte) {
	trail_count := 0
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[i]); j++ {
			// conversion from byte to char is implicit
			if matrix[i][j] == '0' {
				trail_count += dfs(matrix, i, j, 0)
			}
		}
	}
	fmt.Println("Number of trails (Part 2): ", trail_count)
}

func dfs_with_set(matrix [][]byte, i int, j int, index int, visited map[Tuple]bool) int {
	if i < 0 || j < 0 || i >= len(matrix) || j >= len(matrix[i]) || matrix[i][j] != strconv.Itoa(index)[0] {
		return 0
	}

	_, ok := visited[Tuple{i, j}]
	if matrix[i][j] == '9' && !ok {
		visited[Tuple{i, j}] = true
		return 1
	}

	count := 0
	count += dfs_with_set(matrix, i+1, j, index+1, visited)
	count += dfs_with_set(matrix, i-1, j, index+1, visited)
	count += dfs_with_set(matrix, i, j+1, index+1, visited)
	count += dfs_with_set(matrix, i, j-1, index+1, visited)

	return count
}

func dfs(matrix [][]byte, i int, j int, index int) int {
	if i < 0 || j < 0 || i >= len(matrix) || j >= len(matrix[i]) || matrix[i][j] != strconv.Itoa(index)[0] {
		return 0
	}

	if matrix[i][j] == '9' {
		return 1
	}

	count := 0
	count += dfs(matrix, i+1, j, index+1)
	count += dfs(matrix, i-1, j, index+1)
	count += dfs(matrix, i, j+1, index+1)
	count += dfs(matrix, i, j-1, index+1)

	return count
}
