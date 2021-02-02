//solution 1
function solution(a, b) {
    var answer = 0;
    for (let i = 0; i < a.length; i++) {

        answer += a[i] * b[i]
    }
    return answer;
}

solution([1,2,3,4], [-3,-1,0,2])

//solution 2
function solution(a, b) {
    var answer = a.reduce((acc, cur, idx) => acc += cur*b[idx], 0)
    return answer
}

solution([1,2,3,4], [-3,-1,0,2])