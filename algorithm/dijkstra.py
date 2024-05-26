# 다익스트라 알고리즘
# 가중치가 있는 그래프에서 특정 시작 노드로부터 다른 모든 노드까지의 최단 경로를 찾는 알고리즘
# 기본적으로 우선순위 큐를 사용하여 효율적으로 구현
# 각 노드의 최단 거리를 갱신하며, 방문하지 않은 노드 중 가장 거리가 짧은 노드를 선택하여 탐색
# 음의 가중치를 허용하지 않는 그래프에서 동작
# base_image.jpeg를 기준으로 탐색

# 양의 가중치: 그래프의 간선이 가진 값이 0보다 큰 경우. 이동이나 비용이 긍정적(추가)인 의미를 가짐.
# 음의 가중치: 그래프의 간선이 가진 값이 0보다 작은 경우. 이동이나 비용이 부정적(감소)인 의미를 가짐.
import heapq

graph = {
    "A": {"B": 1, "C": 1},
    "B": {"E": 1, "F": 1},
    "C": {"D": 1, "E": 1},
    "D": {"H": 1},
    "E": {"G": 1, "H": 1},
    "F": {"I": 1, "G": 1},
    "G": {"J": 1, "L": 1},
    "H": {"L": 1},
    "I": {"J": 1, "K": 1},
    "J": {"K": 1},
    "K": {"L": 1},
    "L": {},
}


def dijkstra(graph, start, end) -> tuple[list | None, float]:
    queue = [(0, start)]
    # 시작 노드부터 최단경로를 저장하는 노드 딕셔너리
    # float("inf")는 양의 무한대를 표현
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    # 경로 기록용 노드 집합
    previous_nodes = {node: None for node in graph}
    # 방문한 노드를 추적하는 집합
    visited = set()

    while queue:
        # 현재 거리와 노드를 우선순위 큐에서 추출
        current_distance, current_node = heapq.heappop(queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        # 목표 노드에 최종 도착, 최단 경로 반환
        if current_node == end:
            path = []
            while previous_nodes[current_node] is not None:
                path.insert(0, current_node)
                current_node = previous_nodes[current_node]
            path.insert(0, start)
            return path, distances[end]

        # 인접 노드와의 거리를 갱신
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # 더 짧은 경로를 발견하면 최단 거리와 경로 갱신
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return None, float("inf")


# 시작 노드 A에서 다른 모든 노드까지의 최단 경로
shortest_paths = dijkstra(graph=graph, start="A", end="L")
print("최단 경로:", shortest_paths)
