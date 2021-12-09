package main

import (
    "fmt"
    "encoding/csv"
    "os"
    "strconv"
    "math"
    "sort"
)

func main1() {
    reader := csv.NewReader(os.Stdin)
    row, _ := reader.Read()
    n := len(row)

    var pos []int
    for _, v := range row {
        var x,_ = strconv.Atoi(v)
        pos = append(pos, x)
    }

    sort.Slice(pos, func(i, j int) bool {
        return pos[i] < pos[j]
    })

    var median int
    if n%2 == 1 {
        median = pos[n/2-1]
    } else {
        median = (pos[n/2 - 1] + pos[n/2]) / 2
    }

    dist := 0.0
    for _, p := range pos {
        dist += math.Abs(float64(p-median))
    }
    
    fmt.Println(int32(dist))
}