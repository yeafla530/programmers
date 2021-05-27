def rotate90_right(a):
	n = len(a)
	m = len(a[0])
	result = [[0]*n for _ in range(m)]
	for i in range(n):
		for j in range(m):
			result[j][n-i-1] = a[i][j]
	print(result)

def rotate90_left(a):
	n = len(a)
	m = len(a[0])
	result = [[0]*n for _ in range(m)]
	for i in range(n):
		for j in range(m):
			result[n-j-1][i] = a[i][j]
	print(result)

def rotate180_left(a):
	n = len(a)
	m = len(a[0])
	result = [[0]*n for _ in range(m)]
	for i in range(n):
		for j in range(m):
			result[n-i-1][j] = a[i][j]
	print(result)

# 대박 
# rotate90_right값이 나옴(시계방향)
def rotate(key):
    print(list(zip(*key[::-1])))


graph = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate90_right(graph)
rotate90_left(graph)
rotate180_left(graph)
rotate(graph)
