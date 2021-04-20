// 선택정렬
// 1. 먼저 주어진 리스트 중에 최소값 찾는다
// 2. 그 값을 맨 앞에 위치한 값과 교환한다
// 3. 이제 맨 앞을 제외하고 다시 순회하며 최소값을 찾는다
// 4. 그 값을 맨 앞 위치 바로 다음 위치와 교환한다... 반복

let array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for (let i = 0; i < array.length-1; i++) {
    let min_idx = i
    for (let j = i+1; j < array.length; j++) {
        if (array[min_idx] > array[j]) {
            min_idx = j
        }
    }
    if (min_idx !== i) {
        let swap = array[min_idx]
        array[min_idx] = array[i]
        array[i] = swap
    }
    console.log(`${i} 회전 : ${array}`)

}
return array;

