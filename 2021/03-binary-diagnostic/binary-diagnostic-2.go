package main

import (
    "fmt"
    "bufio"
    "os"
    . "strconv"
)

func main(){   
    W := 0
    var nums [2][][2] int16
    for cat:=0; cat<2; cat++ {
        nums[cat] = make([][2] int16, 1)
        nums[cat][0] = [2]int16 {-1,-1}
    }
    N :=[...]int16 {0,0}
    
    var exp int16
    inf, _ := os.Open("input.txt")
    reader := bufio.NewReader(inf)
    scn := bufio.NewScanner(reader)

    for scn.Scan() {
        W = len(scn.Text())
        exp = 1 << (W-1)
        n, _ := ParseInt(scn.Text(), 2, 16)
        n16 := int16(n)
        cat := 0
        if n16 & exp > 0 { cat=1 }
        nums[cat] = append(nums[cat], [2]int16{n16,-1})
        nums[cat][N[cat]][1] = N[cat]+1
        N[cat]++
    }

    zeros, ones := N[0], N[1]
    majority_cat := 0
    if (zeros <= ones){
        majority_cat = 1
    }

    for cat:=0; cat<2; cat++ {
        cur_exp := exp
        for steps :=2; N[cat] > 1; steps++ {
            cur_exp >>= 1
            numbit := [...] int16 {0,0}
            for j:= nums[cat][0][1]; ; j=nums[cat][j][1]{
                bit:=0
                if nums[cat][j][0] & cur_exp > 0 {
                    bit = 1
                }
                numbit[bit]++
                if nums[cat][j][1] == -1 { break }
            }
            badbit:=0
            if cat==majority_cat && numbit[1]< numbit[0] || 
               cat!=majority_cat && numbit[0]<=numbit[1] {
                    badbit = 1
            }
            
            for prevj, j:= int16(0), nums[cat][0][1]; ; j=nums[cat][j][1]{
                bit:=0
                if nums[cat][j][0] & cur_exp > 0 {
                    bit = 1
                }
                if bit==badbit{
                    // remove elem j from the list
                    nums[cat][prevj][1] = nums[cat][j][1]
                    N[cat]--
                } else {
                    prevj = j
                }
                if nums[cat][j][1] == -1 { break }
            }
        }
    }
    
    fmt.Println(int32(nums[0][nums[0][0][1]][0]),int32(nums[1][nums[1][0][1]][0]))
    fmt.Println(int32(nums[0][nums[0][0][1]][0])*int32(nums[1][nums[1][0][1]][0]))
}