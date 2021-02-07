function solution(prices){

    let answer = Array.from({length: prices.length}, () => 0)
    let stack = new Array();
    // console.log(answer)
    for (let i = 0; i < prices.length; i++) {
        while (stack.length && prices[i] < prices[stack[stack.length -1]]) {
            let j = stack.pop()
            answer[j] = i - j
        } 
        stack.push(i)
    }
    while (stack.length) {
        let idx = stack.pop()
        answer[idx] = prices.length - idx - 1
    }
    return console.log(answer)

}

solution([1,2,3,2,3])