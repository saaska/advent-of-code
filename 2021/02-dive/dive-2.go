package main

import (
    "fmt"
    "bufio"
    "os"
)

func main() {
    reader := bufio.NewReader(os.Stdin)
    scn := bufio.NewScanner(reader)
    scn.Scan()
    fmt.Println("Hello, World!")
}