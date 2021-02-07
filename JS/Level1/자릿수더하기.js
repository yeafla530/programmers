//solution 1
function solution(n)
{
    let answer = 0;
    for (let i = n.toString().length-1; i >=0; i--) {
        // console.log(n, i)
        let moc = parseInt(n / (10**i))
        answer += moc
        n = n - moc*(10**i)
        // console.log(answer)
    }

    return answer;
}

//solution 2
function solution(n)
{
    let answer = 0;
    n = n.toString()
    for (let i = 0; i < n.length; i++) {
        answer += parseInt(n[i])
    }

    return answer;
}