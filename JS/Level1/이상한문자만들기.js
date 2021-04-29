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