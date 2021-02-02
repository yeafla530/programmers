//solution 1 -> timeout ㅜㅜ
function solution(n) {
    var answer = 0;
    for (let i = 2; i <= n; i ++) { //2부터 n까지
        let count = 0
        for (let j = 1; j <= i; j ++) { //1부터 자기자신까지
            //2 1 2 
            //3 1 3 
            //4 1 2 4
            //6 1 2 3 6
            //나눴을 때 나머지가 0인 것 
            if (i % j === 0) {
                count += 1
            }
        }
        
        if (count === 2) {
            answer += 1
        }
    }
    return answer;
}

function numberOfPrime(n) {
    if(n == 2) return 1
  
    var count = 0;
    for(var i=2; i <= n; i++){
      var a = 2; // 사이클이 시작할때마다 a = 2 로 리셋
        while(a < i) { //이렇게하면 자신의 숫자로 나누어질 일은 없다.
          if(i % a != 0) { // 그리고 나누어지지않으면 계속, 나누어지면 카운트하고 끝
               a++;
          } else {
              count++
            break;
          }
        }
      }
    return n - count -1;
    // 카운트된 것은 소수가 아닌것들이고, -1을 더 해주는 이유는 1의 경우때문이다.
  }



//에라토스테네스의 체 : ;소수 판단 알고리즘
//소수를 구하기보다 수소가 아닌것을 제외하라 
//소수들 배수 제거 O(N*1/2)

function solution(n) {
    let arr = Array(n+1).fill(true).fill(false, 0, 2)
    //i의 제곱이 n보다 작을 때 까지 
    for (let i = 2; i*i <= n; i ++) {
        if(arr[i]) {
            //j는 i의 제곱
            //j(i*i)가 n보다 작을 때까지
            //j+i씩 증가 j가 4일경우 4, 6, 8, 10 ...
            for (let j=i*i; j<=n; j+=i) {
                arr[j] = false
            }
        }
    }
    
    return arr.filter(e => e).length;
}
