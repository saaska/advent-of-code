// start: 2021-12-11T10:14:48Z

package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
)

func main(){
	TASK := 1
	var E [][]int

    scanner := bufio.NewScanner(os.Stdin)
    for scanner.Scan() {
        line := scanner.Text()
        row := make([]int, len(line))
        for j, ch := range line {
        	row[j],_ = strconv.Atoi(string(ch))
        }
        E = append(E, row)
    }
    
    H, W := len(E), len(E[0])
    flashes, zeros, steps := 0, 0, 0
    
    for (TASK==1 && steps<100) || (TASK==2 && zeros<H*W) {
    	steps++
    	zeros = 0
    	var flashcoords [][]int

		for i,row := range E {
			for j,_ := range row {
				E[i][j]++
				if E[i][j] > 9 {
					pair := []int{i, j}
					flashcoords = append(flashcoords, pair)
				}
			}
		}

		for len(flashcoords) > 0 {
			for _, coords := range flashcoords {
				i, j := coords[0], coords[1]
				E[i][j] = 0
				zeros++
				for di:=-1; di<=1; di++ {
					for dj:=-1; dj<=1; dj++ {
						if (di!=0 || dj!=0) && i+di>=0 && j+dj>=0 &&
						  i+di<H && j+dj<W && E[i+di][j+dj]>0 {
						  	E[i+di][j+dj]++
						}
					}
				}
			}
			flashcoords = make([][]int ,0)
			for i,row := range E {
				for j,_ := range row {
					if E[i][j] > 9 {
						pair := []int{i, j}
						flashcoords = append(flashcoords, pair)
					}
				}
			}
		}

		flashes += zeros
	}
    fmt.Println((2-TASK)*flashes + (TASK-1)*steps)
}
// end: 2021-12-11T13:28:50Z