function solution(n, lost, reserve) {
    var realLost = lost.filter(a => !reserve.includes(a));
    var realReserve = reserve.filter(a => !lost.includes(a));
    
    return n - realLost.filter(a => {
        var b = realReserve.find(r => Math.abs(r-a) <= 1);
        if(!b) return true;
        realReserve = realReserve.filter(r => r !== b);
    }).length;
}

function solution(n, lost, reserve) {
    // var answer = 0;
    let lost_student = n - lost.length
    //잃어버린 학생과 여분있는 학생 비교
    reserve.forEach((num1, idx1) => {
        //빌려줬으면 빠져도돼
        console.log('다시실행?',lost)
        for (let i = 0; i <= lost.length; i++) {
            //여분있는 학생이 도난당했을 경우 체육활동할 수있는 학생 + 1
            console.log(num1)
            if (num1 === lost[i]) {
                lost_student += 1
                reserve.splice(idx1,1)
                lost.splice(i,1)
                console.log('reserve1', idx1, i, lost, reserve)
                break;
            } else if (lost[i] === num1 -1 || lost[i] === num1 +1) {
                lost_student += 1
                reserve.splice(idx1,1)
                lost.splice(lost[i],1)
                console.log(i)
                console.log('reserve2', idx1, lost[i], lost, reserve)
                break;
            }
        }
    })
    //여분있는 학생은 잃어버린학생한테 체육복 빌려줄 수 있음
    //그리고 다른 학생들한테 빌려줄 순 없음
    
    return lost_student;
}