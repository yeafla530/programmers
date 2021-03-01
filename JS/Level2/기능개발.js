// solution 1
function solution(progresses, speeds) {
    var answer = [];
    //1. 완료된 작업을 stack에 넣음
    let n = 0
    // console.log(progresses)
    while (progresses.length > 0) {
        // console.log(progresses)
        // 첫번째 수가 100보다 작으면 계속 반복
        if (progresses[0] < 100) {
            progresses = progresses.map((num,i) => num + speeds[i])
            continue
        // 100보다 클 때
        } else {
            //n += 1
            n += 1
            // 0idx 다음 idx살펴봄
            for (let i = 1; i < progresses.length; i++) {
                // 100보다 작으면 break
                if (progresses[i] < 100) {
                    // console.log('1', answer, progresses, n)
                    break
                // 아니면 n+=1 
                } else {
                    // console.log('2',answer, progresses, n)
                    n += 1
                }
            }
            // progress랑 speeds n추가된 만큼 잘라줌
            progresses.splice(0, n)
            speeds.splice(0, n)
            // n answer에 추가해줌
            answer.push(n)
            // console.log('3',answer, progresses)
            // n = 0으로 초기화
            n = 0
        }
    }
    return answer;
}

//solution 2
function solution(progresses, speeds) {
    let answer = [0];
    // 일수를 구해줌 (올림값)
    let days = progresses.map((progress, index) => Math.ceil((100 - progress) / speeds[index]))
    console.log(days)
    // 제일 처음 값을 걸리는 최대 일수
    let maxDay = days[0];

    // i는 저절로 증가, i는 수동 증가시킴
    for (let i = 0, j = 0; i < days.length; i++) {
        if (days[i] <= maxDay) {
            answer[j] += 1
        }  else {
            maxDay = days[i]
            console.log(maxDay, answer)
            // j를 먼저 증가시켜야 그 전 값이 
            // 1로 초기화 되지 않음
            answer[++j] = 1
            console.log(answer)
        }
    }
    return answer
}