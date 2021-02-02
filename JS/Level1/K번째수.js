//solution 1
function solution(array, commands) {
    var answer = [];
    //array를 command[i]에 따름
    for (let idx = 0; idx < commands.length; idx++) {
        let i = commands[idx][0] - 1
        let j = commands[idx][1]
        let k = commands[idx][2] - 1
        //i부터 j까지 정렬 후 k번째 수를 구한다
        //answer에 push한다
        answer.push(array.slice(i, j).sort((a, b) => a - b)[k])

    }
    return answer;
}

//solution 2
function solution(array, commands) {
    return commands.map(command => {
        const [sPosition, ePosition, position] = command
        const newArray = array
            .filter((value, fIndex) => { //filter(elem, index, array)
                return fIndex >= sPosition - 1 && fIndex <= ePosition - 1
            })
            .sort((a, b) => a - b)
        return newArray[position-1]
    })
}