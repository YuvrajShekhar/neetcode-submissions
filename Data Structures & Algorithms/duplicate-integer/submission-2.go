func hasDuplicate(nums []int) bool {
    nums_dup := make(map[int]bool)
    for _, num := range nums {
        if nums_dup[num] {
            return true
        }
        nums_dup[num] = true
    }
    return false
}
