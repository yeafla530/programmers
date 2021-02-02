//solution 1
function solution(n) {
    var answer = '';
    let watermelon = '수박'
    if (n % 2) {
        for (let i = 0; i < parseInt(n/2); i++) {
            answer += watermelon
        }
        answer += '수'
    } else if (n === 1) {
        answer = '수'
    } 
    else if(n % 2 === 0){
        for (let i=0; i<parseInt(n/2); i++) {
            answer += watermelon
        }
    }
    return answer;
}

//solution 2
function solution(n) {

    let watermelon = '수박'
    return n === 1 ? '수' : ( n % 2 ? watermelon.repeat(n/2) + '수' : watermelon.repeat(n/2))    

}