const dfs = function(graph, v, visited, result) {
    visited[v] = true
    console.log(v + '\t')
    for (const i of graph[v]) {
        if (!visited[i]) {
            dfs(graph, i, visited)
        }
    }
}


graph = [
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

// 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = Array(9).fill(false)
let result = ''
dfs(graph, 1, visited, result)
