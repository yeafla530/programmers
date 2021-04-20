const binary_search = function(array, target, start, end) {
  
  while (start <= end) {
    let mid = parseInt((start + end)/2)
    // console.log(mid)
    if (array[mid] == target) {
      return mid
    } 
    else if (array[mid] > target) {
      end = mid - 1
    } else {
      start = mid + 1
    }
  }
  return None
}


let N = 10
let target = 7
let array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

const result = binary_search(array, target, 0, array.length - 1)
console.log(result + 1)