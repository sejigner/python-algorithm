# BFS(Breadth First Search)
최대한 멀리 있는 노드를 우선적으로 탐색하는 DFS와 달리 가까운 노드부터 탐색하는 알고리즘

보통 큐 자료구조를 이용해서 BFS를 구현한다. 인접한 노드를 반복적으로 큐에 넣는다.

## BFS 동작 과정
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리한다.
2. 큐에서 노드를 꺼내고 그 노드의 인접 노드 중 방문하지 않는 노드를 전부 큐에 삽입한다.
3. 2번을 더 이상 수행이 불가할 때까지 반복 수행한다.

해당 알고리즘은 deque 라이브러리를 이용해서 구현하는 것이 좋다. 시간복잡도는 O(N)이며, 일반적으로 DFS보다 탐색 시간이 짧은 편이다.