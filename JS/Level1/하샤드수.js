function solution(x) {
    var answer = true;
    x = x.toString()
    let num = 0
    for (let i = 0; i < x.length; i++) {
        num += x[i] * 1
    }
    // console.log(10 % 2)
    if (x % num !== 0) {
        answer = false
    }
    
    return answer;
}

//재밌는 풀이 방식
function solution(x) {
    return x % eval([...x.toString()].join("+")) ? false : true
}