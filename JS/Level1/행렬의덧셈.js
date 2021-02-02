//solution 1
function solution(arr1, arr2) {
    var answer = [[]];
    console.log(arr1.length)
    for (let a = 0; a < arr1.length -1; a++) {
        answer.push([])
    }
    // console.log(answer)
    for (let i = 0; i < arr1.length; i++) {
        for (let j = 0; j < arr1[i].length; j++) {
            // console.log(i, j)
            answer[i].push(arr1[i][j] + arr2[i][j])
        }
    }
    return answer;
}

//solution 2
function solution(arr1, arr2) {
    return arr1.map((arr, i) => arr.map((num, j) => arr2[i][j] + num))
}