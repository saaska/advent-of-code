package main

import (
    "fmt"
    "bufio"
    "os"
    . "strings"
    "sort"
)

func main(){
    CLOSING := [4]rune { ')', ']', '}', '>' } 
    pts := map[rune] int {')': 1, ']': 2, '}': 3, '>': 4 }
    scanner := bufio.NewScanner(os.Stdin)
    scores := []int {}
    for scanner.Scan() {
        line := scanner.Text()
        err := false
        buf, pos := make([]rune, 120), 0
        for _, ch := range line {
            if i := Index("([{<", string(ch)); i>-1 {
                buf[pos] = CLOSING[i]
                pos++
            } else {
                if pos > 0 && buf[pos-1] == ch {
                    pos--
                } else {
                    err = true
                    break
                }
            }
        }
        if !err && pos > 0{
            score := 0
            for i := pos - 1; i >= 0; i-- {
                score = 5*score + pts[buf[i]]
            }
            scores = append(scores, score)
        }
    }
    sort.Ints(scores)
    fmt.Println(scores[len(scores)/2])
}

// end: 2021-12-10T10:06:43