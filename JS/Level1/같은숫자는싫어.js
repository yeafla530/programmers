//solution 1
function solution(arr)
{
    var answer = [];
    
    let comp = -1;
    for (let i = 0; i < arr.length; i ++) {
        if (arr[i] !== comp) {
            answer.push(arr[i])
            comp = arr[i]
            // console.log(comp)
        } else {
            continue
        }
    }
    
    return answer;
}


//solution 2
function solution(arr)
{
    return arr.filter((val,index) => val != arr[index+1]);
}
