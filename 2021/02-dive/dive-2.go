package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
    . "strings"
)

func main() {
    reader := bufio.NewReader(os.Stdin)
    scn := bufio.NewScanner(reader)
    aim, x, y := 0, 0, 0
    for scn.Scan() {
        move:= SplitAfter(scn.Text()," ")
        d,_ := strconv.Atoi(move[1])
        switch move[0] {
        case "up ": 
            aim -= d
        case "down ": 
            aim += d
        case "forward ":
            x += d
            y += d*aim
        }
    }
    fmt.Println(x*y)
}