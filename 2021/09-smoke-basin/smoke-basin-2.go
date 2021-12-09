package main
// start: 2021-12-09T16:19:48.51

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
    . "strings"
    "sort"
)

func main(){
    var prodBasins int64 = 1
    scanner := bufio.NewScanner(os.Stdin)
    var depths [102][]uint8
    H, W := 0, 0
    for scanner.Scan() {
        H++
        line := SplitAfter(Trim(scanner.Text(), " \t"), "")
        W = len(line)
        depthline := make([]uint8, W+2)
        for i, ch := range(line) {
            d, _ := strconv.Atoi(ch)
            depthline[i+1] = uint8(d)
        }
        depths[H] = depthline
    }
    depths[0] = make([]uint8, W+2)
    depths[H+1] = make([]uint8, W+2)
    for j:=0; j<W+2; j++ {
        depths[0][j] = 10
        depths[H+1][j] = 10
    }
    for i:=1; i<H+1; i++ {
        depths[i][0] = 10
        depths[i][W+1] = 10
    }

    added, processed := 0, 0
    queue := make(chan int, 10000)
    basins := []int {0,}
    basinarea := []int {0,}
    var basinids[102][] int
    
    basinids[0], basinids[H+1] = make([]int, W+2), make([]int, W+2) 
    for i:=1; i<H+1; i++ {
        basinids[i] = make([]int, W+2)
        for j:=1; j<W+1; j++ {
            if depths[i][j] < depths[i][j+1] &&
               depths[i][j] < depths[i][j-1] &&
               depths[i][j] < depths[i+1][j] &&
               depths[i][j] < depths[i-1][j] {
                coords := 1000*i+j
                queue <- coords
                added++
                basinids[i][j] = len(basins)
                basinarea = append(basinarea, 1)
                basins = append(basins, coords)
            }
        }
    }
    fmt.Println("")

    for processed < added {
        coord := <- queue
        i := coord/1000
        j := coord%1000
        for di,dj,count := 1,0,0; count<4; di,dj,count=-dj,di,count+1 {
            if depths[i+di][j+dj] > depths[i][j] && depths[i+di][j+dj] < 9 && 
               basinids[i+di][j+dj]==0 {
                basinids[i+di][j+dj] = basinids[i][j]
                basinarea[basinids[i][j]]++
                queue <- (i+di)*1000 + (j+dj)
                added++
            }
        }
        processed++
    }
    close(queue)
    sort.Ints(basinarea[1:])
    for i := len(basinarea)-1; i>=len(basinarea)-3; i-- {
        prodBasins *= int64(basinarea[i])
    }
    fmt.Println(basinarea)
    fmt.Println(prodBasins)
}

// end: 2021-12-09T17:41:53Z