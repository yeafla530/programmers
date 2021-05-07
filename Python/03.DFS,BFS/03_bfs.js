const bfs = function(graph, v, visited) {
    let queue = []
    // console.log(visited)
    visited[v] = true
    queue.push(v)
    while (!(queue.length === 0)) {
        // console.log(queue)
        v = queue.shift()
        console.log(v)
        for (const a of graph[v]) {
            if (visited[a] !== true) {
                visited[a] = true
                queue.push(a)
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

let visited = Array(9).fill(false)
bfs(graph, 1, visited)
