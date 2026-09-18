func twoSum(nums []int, target int) []int {
    indices := make(map[int]int)

    for i,n := range nums{
        indices[n] = i
    }

    for i,n := range nums{
        diff := target - n
        if value, found := indices[diff]; found && value != i {
            return []int{i,value}
        } 
    }

    return []int{}
}
