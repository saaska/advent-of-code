package main
// start: 2021-12-09T15:04:17Z

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
	. "strings"
)

func main1(){
	sumRisk:=0
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

    for i:=1; i<H+1; i++ {
	    for j:=1; j<W+1; j++ {
	    	if depths[i][j] < depths[i][j+1] &&
	    	   depths[i][j] < depths[i][j-1] &&
	    	   depths[i][j] < depths[i+1][j] &&
	    	   depths[i][j] < depths[i-1][j] {
	    	   	risk := 1 + depths[i][j]
	    	   	sumRisk += int(risk)
	    	}
	    }
    }
    fmt.Println(sumRisk)
}

// end: 2021-12-09T15:43:03Z