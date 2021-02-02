//solution 1
//다른사람 풀이
function solution(answers) {
    let answer = []
    let a1 = [1, 2, 3, 4, 5];
    let a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    let a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    
    let a1c = answers.filter((a, i) => a === a1[i%a1.length]).length
    let a2c = answers.filter((a, i) => a === a2[i%a2.length]).length
    let a3c = answers.filter((a, i) => a === a3[i%a3.length]).length
    
    //최대값 알아내기 
    let max = Math.max(a1c, a2c, a3c)
    //차례로 값 비교 후 무엇을 넣을지 
    if (a1c === max) {answer.push(1)}
    if (a2c === max) {answer.push(2)}
    if (a3c === max) {answer.push(3)}

    return answer
}

function solution(answers) {
    var answer = [];
    const man1 = [1, 2, 3, 4, 5];
    const man2 = [2, 1, 2, 3, 2, 4, 2, 5];
    const man3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    let count = [0, 0, 0];

    for(let i = 0; i < answers.length; i++) {
        if(answers[i] == man1[i % man1.length]) count[0]++;
        if(answers[i] == man2[i % man2.length]) count[1]++;
        if(answers[i] == man3[i % man3.length]) count[2]++;
    }

    const max = Math.max(count[0], count[1], count[2]);
    for(let i = 0; i < count.length; i++) {
        if(max == count[i]) answer.push(i + 1);
    }

    return answer;
}

//solution 2
//ㅋㅋㅋㅋ 더럽지만 풀었다...
function solution(answers) {
    var answer = [];
    let student1 = "12345".repeat(Math.ceil(answers.length/5)) 
    let student2 = "21232425".repeat(Math.ceil(answers.length/8))
    let student3 = "3311224455".repeat(Math.ceil(answers.length/10))
    
    console.log(student1,student2,student3)
    let count1 = 0
    let count2 = 0
    let count3 = 0
    
    let i = 0
    while (i <= answers.length - 1) {
        if (answers[i] === parseInt(student1[i])) {
            count1 += 1
        } 
        if (answers[i] === parseInt(student2[i])) {
            count2 += 1
        } 
        if (answers[i] === parseInt(student3[i])) {
            count3 += 1
        }
        console.log(count1, count2, count3)
        i++
    }
    
    let max = 0
    let max_idx = 0
    
    //크기비교
    if (count1 >= count2) {
        if (count1 === count2) {
            if(count1 > count3) {
                answer.push(1)
                answer.push(2)
            } else {
                answer.push(3)
            }    
        } 
        else {
             if(count1 > count3) {
                answer.push(1)
            } else if (count1 < count3){
                answer.push(3)
            } 
        } 
    }
    if (count2 >= count3) {
        if (count2 === count3) {
            if(count2 > count1) {
                answer.push(2)
                answer.push(3)
            } else {
                answer.push(1)
            }    
        } 
        else {
             if(count2 > count1) {
                answer.push(2)
            } else {
                answer.push(1)
            }    
        } 
    }
    if (count3 >= count1) {
        if (count3 === count1) {
            if(count3 > count2) {
                answer.push(1)
                answer.push(3)
            } else {
                answer.push(2)
            }    
        } 
        else {
             if(count3 > count2) {
                answer.push(3)
            } else {
                answer.push(2)
            }    
        } 
    }
    
    return [...new Set(answer.sort((a, b) => a - b))];
}