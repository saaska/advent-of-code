package main
// start: 2021-12-10T08:28:19Z
import (
    "fmt"
    "bufio"
    "os"
    . "strings"
    // "sort"
)

func main(){
    val := map[rune] int {')': 3, ']': 57, '}': 1197, '>': 25137 }
    score := 0
    scanner := bufio.NewScanner(os.Stdin)
    for scanner.Scan() {
        line := scanner.Text()
        buf, pos := make([]rune, 120), 0
        for _, ch := range line {
            if i:=Index("([{<", string(ch)); i>-1 {
                buf[pos]= rune(")]}>"[i])
                pos++
            } else {
                if pos>0 && buf[pos-1]==ch {
                    pos--
                } else {
                    score += val[ch]
                    break   
                }
            }
        }
    }
    fmt.Println(score)
}

// end: 2021-12-10T09:34:34Z