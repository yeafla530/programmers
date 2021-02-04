function solution(n) {
    //3진수는 3으로 나눈 나머지로 구하는 것이다
    // 3|45
    // 3|15 ...(0)  
    // 3| 5 ...(0)
    // 3| 1 ...(2)
    //   (1)
    
    let answer = []
  
    while(n !== 0) {
        //0021이 담김
        answer.push(n%3)
        // console.log(answer)
        n = Math.floor(n/3)
        // console.log('n', n)
    }
    let result = answer.reduce((acc, cur, idx) => acc += cur*(3**(answer.length-1-idx)),0)
    return result;
}

//solution 2
function solution(n) {
    let result = [...n.toString(3)].reverse().join("")
    console.log(result)
    return parseInt(result, 3);
}