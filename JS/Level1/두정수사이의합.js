//solution 1
function solution(a, b) {
    var answer = 0;
    let min1 = Math.min(a,b)
    let max1 = Math.max(a,b)
    for (let i = min1; i <= max1; i++) {
        answer += i
    }
    return answer;
}

//solution 2
//왜? 
function adder(a, b){
    var result = 0
    //함수를 완성하세요


    return (a+b)*(Math.abs(b-a)+1)/2;
}