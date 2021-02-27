// solution 1
function solution(citations) {
    var answer = 0;
    let paper = citations.sort((a, b )=>a-b)
    // h번 이상 인용된 논문 h편 이상
    // console.log(paper)
    // 순회
    // h = 1
    for (let h = 0; h <= paper[paper.length-1]; h++) {
        // j = 3
        //paper.length = 4
        //paper[j] = 2
        for (let j = 0; j < paper.length; j++) {
            // 2이 1보다 크고 1번 이상 인용된 논문이 4-3개 이상이고
            // 나머지 논문()이 1번 이하 인용
            if ((paper[j] >= h) && (h <= paper.length-j)) {
                if (j === 0) {
                    answer = h
                } else if (h >= paper[j-1]) {
                    answer = h 
                }
                
                // console.log('answer', answer, j)
            } else {
                continue
            }
        }
    }
    // 나머지 h번 이하 인용
    // h의 최대값이 H-index
    return answer;
}

solution([1, 0, 0, 0])

//solution 2
// n편 중, h번 이상 인용된 논문이 h편 이상이고 
// 나머지 논문이 h번 이하 인용되었다면
// h의 최댓값이 이 과학자의 H-Index
function solution(citations) {
    // 오름차순 정렬
    citations = citations.sort((a, b) => b-a)
    let i = 0;
    // citations의 i번째 값이 i+1보다 작을때까지
    while (i + 1 <= citations[i]) {
        i++
    }
    return i;
}












