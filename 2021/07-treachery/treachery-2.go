package main

import (
    "fmt"
    "encoding/csv"
    "os"
    "strconv"
    "math"
)

func fuel(x int, pos []int) float64{
    dist := 0.0
    for _, p := range pos {
        d := math.Abs(float64(p-x))
        dist += d*(d+1)/2.0
    }
    return dist
}

func main() {
    reader := csv.NewReader(os.Stdin)
    row, _ := reader.Read()
    var pos []int
    r,_ := strconv.Atoi(row[0])
    l := r
    for _, v := range row {
        var x,_ = strconv.Atoi(v)
        pos = append(pos, x)
        if x<l {
            l = x
        } else {
            if x>r {
                r = x
            }
        }
    }

    var best int
    if fuel(l, pos) <= fuel(l+1, pos) && fuel(l, pos) <= fuel(l-1, pos) {
        best = l
    } else {
        if fuel(r, pos) <= fuel(r+1, pos) && fuel(r, pos) <= fuel(r-1, pos) {
            best = r
        } else {
            // bisection with three-point detection 
            var m int 
            for l<r-1 {
                m = (r+l)/2
                if fuel(m-1,pos)>=fuel(m,pos) && fuel(m,pos)<=fuel(m+1,pos) {
                    break
                } else {
                    if fuel(m-1,pos)>=fuel(m,pos) && fuel(m,pos)>=fuel(m+1,pos) {
                        l = m
                    } else{
                        if fuel(m-1,pos)<=fuel(m,pos) && fuel(m,pos)<=fuel(m+1,pos) {
                            r = m
                        }
                    }
                }
                fmt.Println(l, r, m)
            }
            best = int(math.Min(fuel(m, pos), math.Min(fuel(l,pos), fuel(m,pos))))
        }
    }

    fmt.Println(best)
}