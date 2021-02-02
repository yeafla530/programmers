//solution 1
function solution(s) {
    var answer = '';
    let length = parseInt(s.length / 2);
    console.log(length)
    //홀수개
    if (s.length % 2) {
        // 01234 5 
        answer = s[length] 
    } else {
        answer = s[length-1] + s[length]
    }
    return answer;
}

//solution2
function solution(s) {
    const mid = Math.floor(s.length / 2)
    return s.length % 2 ? s[mid] : s[mid-1] + s[mid]
}