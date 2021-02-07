function solution(priorities, location) {
    let Max_num = Math.max.apply(null,priorities);
    let Max_location = priorities.indexOf(Max_num);
    let distance = Math.abs(Max_location - location);

    if(location<Max_location){
        distance *=-1;
    }

    var answer = 0;

    if(distance<0)
        return (priorities.length+distance+1)
    else
        return distance+1
}