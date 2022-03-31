# Graph Measures
## Global 측정
* 그래프의 글로벌 특성
* 각 그래프에 대해 단일 숫자로 구성된다.

## Nodal 측정
* 그래프 노드의 특성
* 숫자 벡터로 구성된다.

## Degree
* 노드에 연결된 총 엣지 수
* In-degree
* Out-degree
* 이외에도 Average (in/out) degree를 계산할 수 있다.

## Strength
* 노드에 연결된 엣지의 가중치 합계
* In-strength
* Out-strength
* 마찬가지로 Average (in/out) strength를 계산할 수 있다.

## Eccentricity (편심률)
### Nodal
* Eccentricity : 특정 노드와 다른 노드 사이의 최대 거리
* Average,  (in/out)  Eccentricity를 계산할 수 있다.

### Global
* Radius : 모든 노드의 최소 Eccentricity
* Diameter : 모든 노드의 최대 Eccentricity

### 참고사항
* 거리 행렬을 통해 편심률을 구할 수 있다.
* 연결이 끊어진 노드의 경우 편심률은 NaN으로 설정된다.

## Path length (경로 길이)
### Nodal
* Path length : 한 노드에서 다른 모든 노드까지의 평균 거리
* 마찬가지로 In/out 존재

### Global
* Characteristic path length : 모든 노드의 경로 길이에 대한 평균
* 마찬가지로 In/out 존재

### 참고사항
* 두 노드 사이의 거리는 노드 사이의 최단 경로의 길이로 정의된다. 
* 그래프에 대한 Dijkstra 알고리즘과 이진 그래프에 대한 너비 우선 검색(BFS)을 사용하여 찾을 수 있다.

## Closeness 
* Closeness : 노드의 경로 길이에 대한 Inverse

## Betweenness
* Betweenness : 해당 노드를 제외한 다른 모든 노드들을 최단 경로로 연결했을 때, 해당 경로가 최단 경로에 포함 되는 횟수

## Global efficiency
* Global efficiency : 한 노드에서 다른 모든 노드로 가는 역최단경로 길이의 평균

## Participation coefficient
* Participation coefficient : 커뮤니티 외부의 노드를 연결하는 엣지 수와 전체 엣지 수 사이의 관계를 정량화 한다.

### 참고사항
* 계산 이전에 커뮤니티 형성 필요
* 참여계수가 높은 노드(Connector hub)는 많은 커뮤니티에 연결되어 있으며, 글로벌 모듈 간 통합을 촉진할 가능성이 있다.

## Assortativity coefficient
* Assortativity coefficient : 엣지의 두 반대쪽 끝에 있는 모든 노드의 degree/strength 사이의 상관관계 계수다.

### 참고사항
* positive 값을 띠는 것은, 노드 자신이 유사한 degree/strength 를 가진 노드에 연결하려는 경향이 있음을 나타낸다.


`http://braph.org/manual/graph-measures/ 를 참고하여 정리했습니다.`