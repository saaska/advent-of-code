//start: 2021-12-14T13:9:57Z

package main

import (
    "fmt"
    "bufio"
    "os"
    . "strings"
    "strconv"
    "sort"
)

func sortltr(pts [][2]int){
    sort.Slice(pts, func(i, j int) bool {
        return pts[i][1] <  pts[j][1] || 
               pts[i][1] == pts[j][1] && pts[i][0] < pts[j][0]
    })
}

func main(){
    reader := bufio.NewReader(os.Stdin)
    scn := bufio.NewScanner(reader)
    var pts [][2]int
    for scn.Scan() && len(scn.Text())>1 {
        pair := SplitN(scn.Text(), ",", -1)
        var p [2]int
        p[0], _ = strconv.Atoi(pair[0])
        p[1], _ = strconv.Atoi(pair[1])
        pts = append(pts, p)
    }
    dotcount, n := 0, len(pts)
    var lastfold [2]int
    for scn.Scan() {
        pair := SplitN(scn.Text(), "=", -1)
        axis := Index("xy", SplitN(pair[0], " ", -1)[2])
        foldpos, _ := strconv.Atoi(pair[1])
        lastfold[axis] = foldpos
        for i, coord := range pts {
            if t:=coord[axis]; t > foldpos {
                pts[i][axis] = foldpos - (t-foldpos)
            }
        }
        if dotcount == 0 {
            sortltr(pts)
            dotcount = 1
            for i:=1; i<n; i++ {
                if pts[i]!=pts[i-1]{
                    dotcount++;
                }
            }
            fmt.Println("Part 1:", dotcount)
        }
    }
    fmt.Println("Part 2:")
    sortltr(pts)
    i := 0
    for y := 0; y < lastfold[1]; y++ {
        for x := 0; x < lastfold[0]; x++{
            if i == n || y != pts[i][1] || x != pts[i][0] {
                fmt.Print(".")
            } else {
                fmt.Print("#")
                i++
                for i<n && pts[i]==pts[i-1] {
                    i++
                }
            }
        }
        fmt.Print("\n")
    }
}
//end: 2021-12-14T16:19:07Z