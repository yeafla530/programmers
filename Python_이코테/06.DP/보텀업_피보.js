let d = Array(100).fill(0)
// console.log(d)

d[1] = 1
d[2] = 1
const n = 99

for (let i = 3; i < n+1; i++) {
    d[i] = d[i-1] + d[i-2]
}

console.log(d[n]) // 218922995834555200000