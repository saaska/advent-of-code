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
    dist := map[string] int { "up ":0, "down ":0, "forward ":0 }
    for scn.Scan() {
        move:= SplitAfter(scn.Text()," ")
        d,_ := strconv.Atoi(move[1])
        dist[move[0]] += d
    }
    fmt.Print((dist["down "]-dist["up "])*dist["forward "])
}