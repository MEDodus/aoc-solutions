package main

import "fmt"

func learning_go() {
	fmt.Println("Hello, World!")
	fmt.Println(concat("Hello, ", "World!"))

	var arr [10]int = [10]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	fmt.Println(arr)
}

func concat(a string, b string) string {
	return a + b
}
