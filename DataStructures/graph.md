# 그래프 (Graph)

* Graph = (V, E)
  * V : vertices, node
  * E : edge
  * Graph는 vertex와 edge의 집합이다.
* 그래프는 방향성이 있을 수도, 없을 수도 있다.
* 방향성이 없으면 undirected 그래프, 있으면 direct 그래프
* Tree는 그래프의 스페셜 케이스다. (directed)
* complete graph : 어떠한 vertex를 골라도 그 사이에 edge가 존재하는 그래프
  * complete directed graph 의 edge 수 : n(n-1) , O(N^2)
  * complete undirected graph 의 edge 수 : n(n-1)/2, O(N^2)
* Weighted graph : edge에 weight 있는 것 (거리 등)
* Weighted Directed Graph가 가장 다양한 정보를 처리할 수 있다.



## Adjacent Nodes
* 서로 연결되어있는 노드
* 5 → 7
  * 5 is adjacent to 7
  * 7 is adjacent from 5
* path : 두 노드를 연결할 때 지나쳐야하는 vertex의 집합



## Adjacency Matrix
* 2차원 array에 그래프를 표현하는 것이다.
* 단점 : Vertex에 비해 edge가 적으면 표의 상당히 많은 값이 0으로 존재한다. 따라서 sparse하면 좋지 않다.
* 장점 : Dense graph에 사용하기 좋다.
* 메모리 필요량 : O(|V|^2) - `비어있으면 공간이 낭비된다`

## Adjacency List
* Linked List 이용해서 그래프의 연결성을 표현하는 것이다.
* Sparse graph에 사용하기 좋다. (Tree)
* 메모리 필요량 : O(|V|)



## Graph Searching

### DFS
* 가장 깊이 있는 것부터 탐색하는 것 (LIFO)
* Stack을 사용한다.



### BFS

* 내려가지 말고 현재 노드에 붙은 것부터 탐색하는 것 (FIFO)
* Queue를 사용한다.

