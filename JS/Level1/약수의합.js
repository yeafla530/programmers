//solution 1
function solution(n) {
    var answer = 0;
    if (n === 0) return answer = 0
    for (let i = 1; i <= n; i++) {
        if (!(n % i)) {
            answer += i
        }
    }
    return answer;
}

//solution 2
//약수는 자기자신의 절반까지의 값 + 자기자신
function solution(n) {
    let answer = n;
    for (let i = 1; i <= parseInt(n/2); i++) {
        if (!(n % i)) {
            answer += i
        }
    }
    return answer;
}