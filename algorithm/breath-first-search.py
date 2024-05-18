# 너비 우선 탐색, BFS
# 기본적으로 큐 사용
# 방문한 노드는 모두 기록, 큐가 모두 탐색이 종료될 때까지 반복 탐색
# base_image.jpeg를 기준으로 탐색
# 너비 우선 탐색은 주로 최단거리를 구할 때 사용
from collections import deque


def breath_first_search(
    graph: list,
    start: str,
    end: str,
) -> list | None:
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        top, path = queue.popleft()
        if top not in visited:
            visited.add(top)
            for next in graph[top]:
                if next == end:
                    return path + [next]
                else:
                    queue.append((next, path + [next]))
    return None


graph: list = {
    "A": ["B", "C"],
    "B": ["E", "F"],
    "C": ["D", "E"],
    "D": ["H"],
    "E": ["G", "H"],
    "F": ["I", "G"],
    "G": ["J", "L"],
    "H": ["L"],
    "I": ["J", "K"],
    "J": ["K"],
    "K": ["L"],
    "L": [],
}
# 시작 노드 A에서 종료 노드 L까지의 경로
result = breath_first_search(graph=graph, start="A", end="L")
print("경로 : ", result)
