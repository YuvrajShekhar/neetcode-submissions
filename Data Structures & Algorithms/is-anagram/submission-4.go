func isAnagram(s string, t string) bool {
    if len(s)!=len(t) {
        return false
    }

    countS := make(map[rune]int)
    countT := make(map[rune]int)

    for _, letter := range s {
        countS[letter]++
    }

    for _, letter := range t {
    countT[letter]++
    }

    if len(countT)!=len(countS){
        return false
    }

    for letter, size := range countS {
        if countT[letter] != size{
        return false}
    }

    return true
}
