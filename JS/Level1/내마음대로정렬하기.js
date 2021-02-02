//solution 1
function solution(strings, n) {
    var answer = [];
    strings.sort((next, prev) => {
        let first = next[n] //e
        let second = prev[n] //u
        //가운데 글자가 같으면
        if (first === second) {
            //prev보다 next가 작으면 자리 바꾸기
            return (next > prev) - (next < prev)
        } else {
            //같지 않으면 n번째 글자만 비교해서 둘중에 작은거 순으로 반환
            return (first > second) - (first < second)
        }
    })
    console.log(strings)
    
    return strings;
}

//solution 2
function solution(strings, n) {
    //localCompare은 next보다 prev가 앞쪽에 있니?
    strings.sort((next, prev) => next[n] === prev[n] ? next.localeCompare(prev) : next[n].localeCompare(prev[n]))
    
    return strings;
}