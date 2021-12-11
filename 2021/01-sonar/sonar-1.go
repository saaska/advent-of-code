// start: 2021-12-11T15:47:44Z

package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
)

func main(){
    scanner := bufio.NewScanner(os.Stdin)
    scanner.Scan()
    n, _ := strconv.Atoi(scanner.Text())  
    count := 0
    for scanner.Scan() {
        m,_ := strconv.Atoi(scanner.Text())  
        if m > n {
            count++
        }
        n = m
    }
    fmt.Println(count)
}
// end: 2021-12-11T15:51:50Z
