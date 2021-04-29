// 다른사람 풀이
function solution(n, arr1, arr2) {
    // 비트 연산자를 이용
    return arr1.map((v, i) => addZero(n, (v | arr2[i]).toString(2).replace(/1|0/g, a => +a ? '#' : ' ')))

}

const addZero = (n, s) => {
    return '0'.repeat(n - s.length) + s;
}
// 내 풀이 (무식)
function solution(n, arr1, arr2) {
    var answer = Array(n).fill('');
    // 1. 모든 줄 2진수로 변환
    let new_arr1 = arr1.map((num) => num.toString(2))
    let new_arr2 = arr2.map((num) => num.toString(2))
    // console.log(new_arr1[1][1]) // string은 literal
    // 2. 만약 길이가 n이 안되면 앞에 0추가 해주기
    console.log(new_arr1.length)
    console.log(new_arr1)
    for (let i = 0; i < n; i++) {
        if (new_arr1[i].length !== n || new_arr2[i].length !== n) {
            while (new_arr1[i].length < n) {
                new_arr1[i] = '0' + new_arr1[i]
            }
            while (new_arr2[i].length < n) {
                new_arr2[i] = '0' + new_arr2[i]
            }
        } 
    }
    // console.log(new_arr1[0].map((n) => n+1))
    for (let i = 0; i < n; i++) {
        for (let j =0; j < n; j++) {
            let sum_arr = parseInt(new_arr1[i][j]) + parseInt(new_arr2[i][j])
            sum_arr = sum_arr.toString()
            // console.log(sum_arr)
            
            if (sum_arr === '0') {
                answer[i] += ' '
            }
            else {
                answer[i] += '#'
            }
        }
    }
    console.log(new_arr1, new_arr2)
    return answer;
    
}

