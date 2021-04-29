function solution(absolutes, signs) {
    absolutes = absolutes.map((x, i) => signs[i] ? +x : -x)
    let answer = 0
    absolutes.forEach(x => answer += x)
    return answer
}