// start: 2021-12-12T07:10:27Z

package main

import (
    "fmt"
    "bufio"
    "os"
    . "strings"
    "sort"
)

const (
	UC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	TASK = 2
)

func dfs(A map[string][]string, v string, visited map[string]int, twice bool) int {
	if v == "end" {
		return 1
	}
	visited[v] = visited[v] + 1
	paths := 0	
	for _, u := range A[v] {
		if Contains(UC, string(u[0])) || visited[u] == 0 {
			paths += dfs(A, u, visited, twice)
		} else {
			if TASK==2 && u != "start" && !twice {
				paths += dfs(A, u, visited, true)
			}
		}
	}
	visited[v]--
	return paths
}

func main() {
	reader := bufio.NewReader(os.Stdin)
    scn := bufio.NewScanner(reader)
	A := make(map[string][]string)
    for scn.Scan() {
    	pair := SplitN(scn.Text(), "-", -1)
    	for i:=0; i<2; i++ {
    		u, v := pair[i], pair[1-i]
	    	neighbors, exists := A[u]
	    	if exists {
	    		A[u] = append(neighbors, v)
	    	} else {
	    		A[u] = make([]string, 1)
	    		A[u][0] = v
	    	}
	    }
    }
    for v, _ := range A {
    	sort.Strings(A[v])
    }
    fmt.Println(dfs(A, "start", make(map[string]int), false))

// end: 2021-12-12T15:03:59Z stupid mistake left out some letters from UC!!!>:\