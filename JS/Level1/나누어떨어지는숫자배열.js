//solution 1
function solution(arr, divisor) {
    var answer = [];
    let array = arr.filter(num => !(num % divisor))  
    if (array.length) {
        return array.sort((a, b) => a-b)
    } else {
        return [-1]
    }
}

//solution 2
function solution(arr, divisor) {
    let array = arr.filter(num => !(num % divisor))  
    array.length == 0 ? [-1] : array.sort((a-b) => a-b)
}