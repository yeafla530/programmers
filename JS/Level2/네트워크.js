//solution 01. DFS

function dfs(start, computers, visited) {
    visited[start] = 1
    for (let i = 0; i < computers.length; i ++) {
        if (computers[start][i] && !visited[i]) {
            dfs(i, computers, visited)
        }
    }
}

function solution(n, computers) {
    var answer = 0
    let visited = Array(n).fill(0)
    // console.log(visited)
    for (let i = 0; i < n; i ++) {
        if (!visited[i]) { // 방문한 적이 없는 경우
            answer ++
            dfs(i, computers, visited)
            
        }
    }    
    return answer;
}


// solution 2. BFS
function bfs(start, computers, visited) {
    visited[start] = 1
    let queue = []
    queue.push(start)
    while (queue.length !== 0) {
        let v = queue.shift()
        // console.log(v)
        for (let i = 0; i < computers.length; i ++) {
            if (visited[i]) continue;
            if (computers[v][i] && !visited[i]) {
                visited[i] = 1
                queue.push(i)
            }
        }
    }
        
}

function solution(n, computers) {
    var answer = 0
    let visited = Array(n).fill(0)
    // console.log(visited)
    for (let i = 0; i < n; i ++) {
        if (!visited[i]) { // 방문한 적이 없는 경우
            answer ++
            bfs(i, computers, visited)
        }
    }    
    // console.log(visited)
    return answer;
}