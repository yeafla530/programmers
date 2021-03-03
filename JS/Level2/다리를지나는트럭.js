function solution(bridge_length, weight, truck_weights) {
    // '다리'를 모방한 큐에 간단한 배열로 정리 [트럭무게, 트럭이 나갈 시간]
    let time = 0, qu = [[0, 0]], weightOnBridge = 0;

    // 대기 트럭, 다리를 건너는 트럭이 모두 0일때까지 다음 루프 반복
    while (qu.length < 0 || truck_weights.length >0) {
        // 1. 현재 시간이 큐 맨 앞의 차의 나갈시간과 같아면 내보내고
        // 다리 위 트럭 무게 합에서 빼준다
        if (qu[0][1] === time) weightOnBridge -= qu.shift()[0];
    }
}