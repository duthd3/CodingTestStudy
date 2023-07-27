from collections import deque
# 시험관 크기 및 바이러스 종류 저장
n, k = map(int, input().split())
# 바이러스 정보 저장
graph = []
#바이러스 추가 정보
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if(graph[i][j] != 0):
            data.append((graph[i][j], 0, i, j))
data.sort()
q = deque(data)

s, x, y = map(int, (input().split()))
dx = [-1, 1, 0, 0] # 상 하
dy = [0, 0, -1, 1] # 좌 우

while(q):
    virus, time, i, j = q.popleft()
    
    if (time == s):
        break
    for l in range(4):
        nx = i + dx[l]
        ny = j + dy[l]
        
        if (0<=nx and nx < n and 0 <= ny and ny < n and  graph[nx][ny] == 0):
            graph[nx][ny] = virus
            q.append((virus, time+1, nx, ny))
    
print(graph[x-1][y-1])
