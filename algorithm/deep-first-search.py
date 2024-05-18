# 깊이 우선 탐색, DFS
# 기본적으로 스택 사용, 재귀 함수를 이용하여 암묵적으로도 사용
# 모든 노드에 대하여 검색하고 방문하되 시작되면 끝 점까지 탐색
# base_image.jpeg를 기준으로 탐색
# 깊이 우선 탐색은 최단거리를 보장하지 않는다


def deep_first_search(
    graph: list,
    start: str,
    end: str,
    path: list | None = None,
    visited: bool | None = None,
):
    if not visited or not isinstance(visited, set):
        visited = set()

    if not path:
        path = []

    visited.add(start)
    path.append(start)

    if start == end:
        return path

    for neighbor in graph[start]:
        if neighbor not in visited:
            result = deep_first_search(
                graph=graph, start=neighbor, end=end, path=path, visited=visited
            )
            if result is not None:
                return result


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
result = deep_first_search(graph=graph, start="A", end="L")
print("경로 : ", result)
