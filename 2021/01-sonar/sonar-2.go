// start: 2021-12-11T15:54:15Z

package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
)

func main(){
    scanner := bufio.NewScanner(os.Stdin)
    s := 0
    var x [4]int
    for i:=0; i<3; i++ {
        scanner.Scan()
        x[i], _ = strconv.Atoi(scanner.Text()); s += x[i]
    }
    count := 0
    fmt.Println(x)
    for scanner.Scan() {
        x[3], _  = strconv.Atoi(scanner.Text())  
        if x[0]+x[1]+x[2] < x[1]+x[2]+x[3] {
            count++
        }
        x[0], x[1], x[2] = x[1], x[2], x[3]
    }
    fmt.Println(count)
}
// end: 2021-12-11T16:08:46Z

