//solution 1 - 나의 풀이,,,
function solution(new_id) {
    var answer = [];
    //1. 소문자 변환
    new_id = new_id.toLowerCase()
    //2.,3. 소문자, 숫자, -, _, .빼기 && .연속되면 빼기
    for (let i = 0; i < new_id.length; i++) {
        //숫자 범위 주의
        if (new_id[i].match(/^[a-z]$/) || (Number(new_id[i]) >= 0 && Number(new_id[i]) <= 9) || new_id[i] === '.' || new_id[i] === '-' || new_id[i] === '_' ) {
            if (answer && answer[answer.length-1] === '.' && new_id[i] ==='.') {
                continue;    
            }
            answer.push(new_id[i])
        } 
    }
    //4. .이 맨 첨이나 끝에 있으면 빼기
    console.log(answer)
    if (answer[0] === '.') {
        answer.splice(0,1)
    } 
    if (answer[answer.length-1] === '.') {
        answer.pop()
    }
    //5. 빈 문자열이면 new_id에 'a'를 대입
    if (answer.length === 0) {
        answer.push('a')
    }
    //6. 글자길이 16이상이면 15개를 제외한 문자 모두 제거 후 끝에 .이면 그것도 제거
    if (answer.length >= 16) {
        answer.splice(15)    
    }
    
    if (answer[answer.length-1] === '.') {
        answer.pop()
    }
    //7. new_id의 길이가 2자 이하라면, 마지막 문자를 반복
    if (answer.length <= 2) {
        while(answer.length !== 3) {
            answer.push(answer[answer.length-1])
        }
    }
    answer = answer.join('')
    
    return answer;
}

//solution 2 - 정규표현식 사용
function solution(new_id) {
    const answer = new_id
        .toLowerCase() // 1
        .replace(/[^\w-_.]/g, '') // 2
        .replace(/\.+/g, '.') // 3
        .replace(/^\.|\.$/g, '') // 4
        .replace(/^$/, 'a') // 5
        .slice(0, 15).replace(/\.$/, ''); // 6
    const len = answer.length;
    return len > 2 ? answer : answer + answer.charAt(len - 1).repeat(3 - len);
}
