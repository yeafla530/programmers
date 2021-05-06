let result = 0
result = solution([1, 1, 1, 1, 1], 3)
console.log(result)

function solution(numbers , target) {
    let answer = 0 
    console.log(numbers)
    function subset(cnt,sum){
        if(cnt===numbers.length){
            if(sum===target){
                answer+=1;
            }
            return;
        }
        subset(cnt+1,sum+numbers[cnt]);
        subset(cnt+1,sum-numbers[cnt]);
    }
    subset(0,0);
    return answer;
}

