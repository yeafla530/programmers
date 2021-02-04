//solution 1
function solution(s) {
    var answer = true;
    s = s.split('') 
    let list = s.filter(n => isNaN(n))
    console.log(list)
    if (list.length === 0 && (s.length===4 ||s.length===6)) {
        answer = true
    } else {
        answer = false
    }
    return answer;
}


//splution 2
//단 16지수가 나오면 안통함
function alpha_string46(s) {
    return s.length == 4 || s.length == 6 ? s==parseInt(s) : false 
 }