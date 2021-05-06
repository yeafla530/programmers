const bfs = function(graph, v, visited) {
    let queue = []
    visited[v] = true
    queue.push(v)
    while (queue.length !== 0) {
        console.log(queue)
        v = queue.shift()
        for (const a of graph[v]) {
            console.log(a)
            if (visited[a] !== true) {
                visited[a] = true
                queue.push(a)
                console.log('a' + queue)
            } 
        }
    }
}

let graph = [
    [],
    [2, 3, 8],
    [1, 7], 
    [1, 4, 5],
    [3, 5],
    [3, 4], 
    [7], 
    [2, 6, 8],
    [1, 7]
]

let visited = [false] * 9
result = bfs(graph, 1, visited)
