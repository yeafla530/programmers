//solution 1
function solution(a, b) {
    var answer = '';
    let days = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    //31 29 31 30 31 30 31 31 30 31 30 31
    let days_num = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    let sum = 0
    days_num = days_num.filter((num, idx) => a >= idx+2) 
    if (a !== 1) {   
        sum = days_num.reduce((acc, cur) => acc+=cur)
    }
    sum += b
    sum = parseInt(sum % 7) - 1
    if (sum === -1) {
        sum = 6
    } 
    // console.log(sum)
    
    
    return days[sum];
}

//solution 2
function solution(a, b) {
    var answer = '';
    //주의 : 7로 나누어 떨어지는건 0나옴 
    let days = {1:"FRI",2:"SAT",3:"SUN",4:"MON",5:"TUE",6:"WED",0:"THU"}
    //31 29 31 30 31 30 31 31 30 31 30 31
    let days_num = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    let sum = 0
    days_num = days_num.filter((num, idx) => a >= idx+2) 
    if (a !== 1) {   
        sum = days_num.reduce((acc, cur) => acc+=cur)
    }
    sum += b
    sum = parseInt(sum % 7) 
    
    console.log(days[sum])
    return days[sum];
}