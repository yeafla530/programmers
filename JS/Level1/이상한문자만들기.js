function solution(s) {
    var answer = '';
    let new_arr = s.split(' ')
    console.log(new_arr)
    new_arr.forEach((x, i) => {
        for (let i = 0; i < x.length; i++) {
            if ((i+1) % 2) { //홀수면
                answer += x[i].toUpperCase()    
            }
            else {
                answer += x[i].toLowerCase()
            }
        }
        if (i != new_arr.length-1) {
            answer += ' '    
        }
        
    })
    
    return answer;
}

//다른 사람 풀이
function solution(s) {
    var answer = '';
    let num = 1
    for (let i = 0; i < s.length; i++) {
        if (s[i] == ' ') {
            num = 1
            answer += ' '
            continue
        }
        
        if (num % 2 == 0) {
            answer += s[i].toLowerCase()
            num ++
        }
        else {
            answer += s[i].toUpperCase()
            num ++
        }
    }
    
    
    return answer;
}