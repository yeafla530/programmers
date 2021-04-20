let array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
// ...으로 array에 있는 값 spread해주기
let count = Array(Math.max(...array)+1).fill(0)
// console.log(count)

for (let i = 0; i < array.length; i++) {
    count[array[i]] += 1
}


result = ""
for (let i = 0; i < array.length; i++) {
    for (let j = 0; j < count[i]; j++) {
        result = result +String(i)
        result += '\t'
    }
}
console.log(result)
