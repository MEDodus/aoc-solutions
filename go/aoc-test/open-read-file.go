package main

import (
	"fmt"
	"os"
)

func open_read_file() {
	data, err := os.ReadFile("files/test.txt")
	if err != nil {
		fmt.Println("File reading error: ", err)
		return
	}
	fmt.Println("Contents of file:", string(data))
}
