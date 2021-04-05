'''
    Node      (0)
              | |
    Edge     7   5
            |     |
    Node   (1)   (2)
'''

INF = 999999999 # 무한의 비용 선언

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]
# graph(0=>0) graph(0=>1) graph(0=>2)
# graph(1=>0) graph(1=>1) graph(1=>2)
# graph(2=>0) graph(2=>1) graph(2=>2)

print(graph)