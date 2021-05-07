// arr[5][2]
let arr = [['a','b'],['a','b'],['a','b'],['a','b'],['a','b']]

// arr[5][2]
let arr1 = new Array(5)
console.log(arr1)

for (let i = 0; i < arr.length; i++) {
    arr[i] = new Array(2)
}
console.log(arr1)

// Array.from사용
// arr[5][2] 빈배열 생성
const arr2 = Array.from(Array(5), () => new Array(2))

// arr[5][2] 0으로 초기화
const arr3 = Array.from(Array(5), () => new Array(2).fill(0))