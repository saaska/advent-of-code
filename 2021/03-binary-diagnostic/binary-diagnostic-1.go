package main

import (
    "fmt"
    "bufio"
    "os"
    . "strings"
)

func main(){   
    var D [][]uint8
    bin := map[string] uint8 {"1":1}
    H, W := 0, 0
    reader := bufio.NewReader(os.Stdin)
    scn := bufio.NewScanner(reader)
    for scn.Scan() {
        line := SplitAfter(scn.Text(), "")
        W = len(line)
        dline := make([]uint8, W)
        for i, bit := range(line) {
            dline[i] = bin[bit]
        }
        D = append(D, dline)
    }
    H = len(D)
    x, y := 0, 0
    pow2 := 1
    for j:=W-1; j>=0; j-- {
        sum:=0
        for i:=0; i<H; i++ {
            sum += int(D[i][j])
        }
        if sum > H/2 {
            x += pow2
        }
        pow2 *= 2
    }
    y = pow2 - x - 1 
    fmt.Println(x*y)
}