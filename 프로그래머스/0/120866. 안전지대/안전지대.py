# np.where를 이용한 초 간결 코드

import numpy as np

def solution(board):
    board = np.array(board)
    for a, b in zip(*np.where(board == 1)) :    # np.where(조건) : 조건에 맞는 인덱스를 배열로 반환
        board[a-1 if a else 0: a+2, b-1 if b else 0: b+2] = 1
    
    return len(board[board == 0])


----------------------------------------------------------------------------
# BFS를 이용한 위치탐색 코드
# BFS : 1️큐(Queue) 자료구조를 이용하여 푼다

from collections import deque

def solution(board):
    dx = [-1, 1, 0 , 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    length = len(board)
    visited = [[False] * length for _ in range(length)]

    def bfs(x, y):
        dq = deque()
        dq.append((x, y))
        while dq:
            a, b = dq.popleft()
            visited[a][b] = True
            for i in range(8):
                nx = dx[i] + a
                ny = dy[i] + b
                #위험지역으로 둬야함 
                if 0<=nx<length and 0<=ny<length and not visited[nx][ny]:
                    if board[nx][ny] == 1:
                        dq.append((nx, ny))
                    else:
                        board[nx][ny] = 2 #위험지역 처리 

    for i in range(length):
        for j in range(length):
            if board[i][j] == 1:
                bfs(i, j)
    result = 0
    for i in range(length):
        result += board[i].count(0)
    return result
