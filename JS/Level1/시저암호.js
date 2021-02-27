// solution 1
// arr를 새로 만들어 넣는 방식을 사용하여 비효율적
// solution2처럼 바로 answer에 추가하는 방식으로 사용하면 좋을 것 같음 
function solution(s, n) {
    var answer = '';
    let arr = s.split("")
    // console.log(arr)
    for (let i = 0; i < arr.length; i++) {
        if (s.charCodeAt(i)=== 32) {
            arr[i] = arr[i]
            continue
        }
        let acc = s.charCodeAt(i)
        let code = s.charCodeAt(i) + n
        console.log('acc',acc)
        console.log('code',code)
        if ((65 <= acc && acc <= 90 && code > 90) || (97 <= acc && acc <= 122 && code > 122))  {
            console.log(arr[i], code)
            code -= 26
            // console.log('왜 여기들어옴?', arr[i], code)
        } 
        // console.log('code', code)
        arr[i] = String.fromCharCode(code)
        console.log('찐', arr[i])
    }
    answer = arr.join('')
    // console.log(answer)
    return answer;
}

//solution 2
function solution(s, n) {
    let upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let lower = "abcdefghijklmnopqrstuvwxyz";
    let answer = '';

    for (let i = 0; i < s.length; i++) {
        let text = s[i]
        if (text == ' ') {
            answer += ' '
            continue
        }
        let textArr = upper.includes(text) ? upper : lower;
        let index = textArr.indexOf(text) + n;
        console.log(index, textArr[index])
        if (index >= textArr.length) index -= textArr.length;
        answer += textArr[index]
        console.log(index, textArr[index])

    }
    console.log(answer)
    return answer
}

solution("a B z", 4)