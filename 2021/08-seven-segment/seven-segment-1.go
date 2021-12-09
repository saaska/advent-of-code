package main

import (
    "bufio"
    "fmt"
    "os"
    "strings"
)

func main1() {
    scanner := bufio.NewScanner(os.Stdin)
    count := 0
    for scanner.Scan() {
        l := scanner.Text()
        parts := strings.SplitAfter(strings.Trim(strings.SplitAfter(l , "|")[1], " "), " ")
        for _, p := range parts {
            p = strings.Trim(p, " ")
            if len(p)==2 || len(p)==4 || len(p)==3 || len(p)==7 {
                count++
            }
        }
    }
    fmt.Println(count)
}