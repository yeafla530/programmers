//solution1
function solution(numbers) {
    var answer = [];
    //하나는 고정 
    //나머지 움직이기
    //0 => 1234
    //1 => 234
    //2 => 34 ..
    for (let i = 0; i < numbers.length-1; i++) {
        for (let j = i+1; j < numbers.length; j ++) {
            let sum = numbers[i] + numbers[j]
            if (!answer.includes(sum)) {
                answer.push(sum)
            }
        }
    } 
    answer.sort((a,b) => a-b)
    return answer;
}

//solution2
function solution(numbers) {
    var answer = [];
    for (let i = 0; i < numbers.length-1; i++) {
        for (let j = i+1; j < numbers.length; j ++) {
            let sum = numbers[i] + numbers[j]
            if (answer.indexOf(sum) === -1) {
                answer.push(sum)
            }
        }
    } 
    answer.sort((a,b) => a-b)
    return answer;
}


//solution3
function solution(numbers) {
    const temp = []
    for (let i = 0; i < numbers.length; i++) {
        for (let j = i + 1; j < numbers.length; j++) {
            temp.push(numbers[i] + numbers[j])
        }
    }

    const answer = [...new Set(temp)]

    return answer.sort((a, b) => a - b)
}

solution([2, 1, 3, 4, 1])