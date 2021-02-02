function solution(board, moves) {
    var answer = 0;
    //뒤에서부터 뺄 수있음
    let toy = 0
    let array = []
    //moves에서 수 하나씩 빼기
    moves.forEach((num,idx) => {
        // moves자리에 인형있는지 확인
        // console.log(num)
        for (let i = 0; i < board.length; i++) {
            //인형이 있으면 바구니에 넣기
            // console.log(board[i][num-1])
            if(board[i][num-1]) {
                array.push(board[i][num-1])
                board[i][num-1] = 0
                break
            }
        }
        // console.log(array)
        if (array.length -1 >= 0 && array[array.length-1] === array[array.length-2]) {
            // console.log(array[array.length-1], array[array.length-2])
            // array.pop()
            // array.pop()
            array.splice(array.length-2, 2)
            answer += 2
            // console.log("찍힘?")
        }

    })
    return answer;
}