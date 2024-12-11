package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	file, err := os.Open("files/map.txt")
	if err != nil {
		fmt.Println("File opening error: ", err)
		return
	}

	// Defers closing the file resource until the end of the function, good practice in Go
	defer file.Close()

	matrix := [][]byte{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		arr := []byte(line)
		matrix = append(matrix, arr)
	}

	// Print entire matrix
	// fmt.Println(matrix)
	// Print matrix line by line
	// for i := 0; i < len(matrix); i++ {
	// 	for j := 0; j < len(matrix[i]); j++ {
	// 		fmt.Print(string(matrix[i][j]))
	// 	}
	// 	fmt.Println()
	// }

	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[i]); j++ {
			if string(matrix[i][j]) == "9" {
				matrix[i][j] = 'X'
			}
		}
	}

	// Print matrix line by line
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[i]); j++ {
			fmt.Print(string(matrix[i][j]))
		}
		fmt.Println()
	}

	// fmt.Println(matrix)
}
