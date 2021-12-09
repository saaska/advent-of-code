package main

import (
    "bufio"
    "os"
    "sort"
    "fmt"
    . "strings"
)

const SEVEN = "abcdefg"

func sortedchars(s string) string{
    q1 := SplitAfter(Trim(s, " "), "")
    sort.Strings(q1)
    return Join(q1,"")
}   

func without(s string, r rune) string {
    return Replace(s, string(r), "", 1)
}

func remove(possible map[rune]string, wire, displaysegment rune){
    possible[wire] = without(possible[wire], displaysegment)
}

func processCorrespondence(wires string, display string, possible map[rune]string){
    // if a wire combination, eg. wires = "ag" 
    // triggers certain display segments eg. display="cf", then
    // 1) THESE wires cannot trigger OTHER display segs, 
    //    so neither a nor g can trigger a/b/d/e/g 
    // 2) OTHER wires cannot trigger THESE display segs, 
    //    so b/c/d/e/f cannot trigger c or f    
    for _, wire := range(wires) {
        for _, displaysegment := range SEVEN {
            if !ContainsRune(display, displaysegment) {
                remove(possible, wire, displaysegment)
            } 
        }
    }
    for _, wire := range SEVEN {                    
        if !ContainsRune(wires, wire) {
            for _, displaysegment := range(display) {
                remove(possible, wire, displaysegment)
            } 
        }
    }
}

func main() {
    sum := 0

    // we sort both display and wire combinations by length 
    // and combinations themselves alphabetically
    displaydigits := [...]string {
        "abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg",
    } 
    displaycomb := make([]string, 10)
    copy(displaycomb, displaydigits[:])
    sort.Slice(displaycomb, func(i, j int) bool { return len(displaycomb[i])< len(displaycomb[j]) })
    scanner := bufio.NewScanner(os.Stdin)

    for scanner.Scan() {
        words := SplitAfter(scanner.Text(), " ")
        for i, s := range words { words[i] = sortedchars(s) }
        wirecomb, fired := words[0:10], words[11:]
        sort.Slice(wirecomb, func(i, j int) bool { return len(wirecomb[i])< len(wirecomb[j]) })

        // Possible corresponding display segs for each wire. Initially all seven
        possible := make(map[rune]string)
        for _, wire := range(SEVEN){ possible[wire] = SEVEN }

        // for every combination that fires a unique number of wires, process it
        // against the unique display combination with than number of segments
        for i, wcomb := range wirecomb {
            if i == 0 || len(wcomb) != len(wirecomb[i-1]) && 
               i != 9 && len(wcomb) != len(wirecomb[i+1]) {
                processCorrespondence(wcomb, displaycomb[i], possible)
            }
        }
        
        // group all other combinations by number L of wires fired
        // count the number of times each wire appears in the group
        // process all the wires that appear equal number of times 
        // against all the display segments that appear the same number of times
        combs := [][]string { displaycomb, wirecomb }
        for i,next := 0,1; i<9; i = next {
            L := len(displaycomb[i])
            for next = i+1; len(displaycomb[next])==L; { next++ }
            charfreq := make([]map[int] string, 2)
            for kind:=0; kind<2; kind++ {
                charfreq[kind] = make(map[int] string)
                charfreq[kind][0] = SEVEN
                lengthLCombs := ""
                for j:=i; j<next; j++ { lengthLCombs += combs[kind][j] }
                freq := map[rune] int {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0}
                for _, ch := range lengthLCombs {
                    fr := freq[ch]
                    charfreq[kind][fr] = without(charfreq[kind][fr], ch)
                    charfreq[kind][fr+1] += string(ch)
                    freq[ch]++
                }
            }
            for fr:=1; fr<=3; fr++ {
                processCorrespondence(charfreq[1][fr], charfreq[0][fr], possible)
            }
        }

        // should have just a single possible display segment for each wire by now
        // reconstruct digits corresponding to wire combinations
        value := make(map[string] int)
        for _, wcomb := range wirecomb {
            dcomb := ""
            for _, wire := range wcomb {
                dcomb += possible[wire]
            }
            dcomb = sortedchars(dcomb)
            for digit, displayed := range displaydigits{
                if displayed == dcomb {
                    value[wcomb] = digit
                    break
                }
            }
        }

        var number, deg10 int = 0, 1
        for i := len(fired)-1; i>=0; i-- {
            number += value[fired[i]] * deg10
            deg10 *= 10
        }
        sum += number
    }
    fmt.Println(sum)
}
