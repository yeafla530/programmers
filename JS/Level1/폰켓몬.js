function solution(nums) {
    //멍청했다, 조합문제가 아니다
    // 그냥 중복을없애고, 종류가 N/2보다 많으면 N/2가 최대니까 N/2를 반환하고
    // 종류가 N/2보다 적으면 그 개수를 return 하면된다
    let set1 = new Set()

    
    for (const n of nums) {
        set1.add(n)
    }
    console.log(set1.size)
    if (set1.size < nums.length/2) {
        return set1.size
    } else {
        return nums.length/2
    }
    
}

// 다른 풀이
function solution(nums) {
    let set1 = [...new Set(nums)]
    console.log(set1)
    return set1.length < nums.length / 2 ? set1.length : nums.length / 2
}