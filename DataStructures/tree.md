# 트리 (Tree)
* Tree는 Cycle이 없고 위아래 관계만이 있다.
* 부모와 자식을 고유하게 가지면서 Recursive와 Cycle이 존재하지 않는 2차원 자료구조다.

## Tree 용어
<img width = "400" src= "https://user-images.githubusercontent.com/64299475/146689550-fc3d0a18-2b2d-4e06-8df4-1ea3643e388f.png">

* **Level**은 root 노드부터 **0, 1, 2, ...** 순이다.
* **Height**는 root 노드부터 **1, 2, 3, ...** 순이다. (Height = Level + 1)
* Leaf 노드 : Child가 하나도 없는 노드
	* *가장 깊은 Level의 노드가 leaf 노드라는 개념은 틀렸다.*
* Ancestor of a node : 부모와 부모보다 더 위에 있는 노드들
	* *다시 말해, 해당 노드에서 루트노드로 갈 때 지나가는 모든 노드다.*
* Descendant of a node : 자식과 자식보다 더 위에 있는 노드들
* 노드가 하나만 남아도 Tree라 부를 수 있다.

## Tree Traversal
* Inorder : 왼쪽 - 자신 - 오른쪽
* Postorder : 왼쪽 - 오른쪽 - 자신
* Preorder : 자신 - 왼쪽 - 오른쪽

## Full Tree
* Full Tree는 Leaf 노드가 모두 같은 Level에 있고 non-leaf 노드는 binary인 경우 모두 자식이 2개 있는 트리를 지칭한다.

## Binary Tree
* Binary Tree는 최대 2개의 자식 노드를 가지는 Tree다.
* Height가 h인 Full Tree의 노드 개수는 **2^h-1** 이다. *(!= level)*
	* 2^h -1 = N
	* 2^h = N+1
	* h= log(N+1) ⇒ `O(logN)`
* node가 n개 있을 때 height 가장 짧을 때는 Full Tree다.
* Searching a binary Tree : `O(N)`

> **Q. 전체 노드의 수가 n인 full binary tree에서 non-leaf node의 수는 (n – 1)/2임을 증명하세요.**   
> 먼저 height가 h인 **Full Tree node**는 1, 2, 4, 8 순으로 커지므로 2⁰+ 2¹+ 2²+...+2^(h-1) = **(2^h)-1**이다.   
> 고로, **n은 (2^h)-1과 같다.**  
> n - leaf nodes가 non-leaf nodes이다.  
> (2^h)-1 = n이므로 2^(h-1) = **(n+1)/2 가 leaf nodes**이다.  
> **non leaf nodes**는 n-(n+1)/2 = (n/2)-(1/2) = **(n-1)/2**이다.  

## Binary Search Tree
* BST는 **왼쪽 자식 노드는 자신보다 작고 오른쪽 자식 노드는 자신보다 큰 형태의 Tree다.**
	* 왼쪽과 오른쪽이 반대가 되어도 BST이다.
* 순서에 따라 모양이 달라지고 동일한 데이터라도 넣는 순서에 따라 최고, 최악으로 효율이 갈릴 수 있다.
* Pruning을 통해 연산 속도를 높일 수 있다.
* Searching a BST : `O(logN)`
	* 가장 아래 leaf까지 찾는 값이 없으면 없다고 판단한다.


### DeleteItem
* 트리에서 중간 노드가 삭제 되면 별도의 처리가 필요하다.
1. 자식이 하나인 경우는 그 자식을 위로 옮겨주면 된다.
2. 2개, 혹은 그 이상인 경우는
	1. 좌측 자식 중 가장 우측 후손 leaf 노드
	2. 또는 우측 자식 노드 중 가장 왼쪽을 위로 옮겨주면 된다.

### 시간 복잡도 

| operation    | BST     | Array-based List | Linked List |
| ------------ | ------- | ---------------- | ----------- |
| Constructor  | O(1)    | O(1)             | O(1)        |
| Destructor   | O(N)    | O(1)             | O(N)        |
| IsFull       | O(1)    | O(1)             | O(1)        |
| IsEmpty      | O(1)    | O(1)             | O(1)        |
| RetrieveItem | O(logN) | O(logN)          | O(N)        |
| InsertItem   | O(logN) | O(N)             | O(N)        |
| DeleteItem   | O(logN) | O(N)             | O(N)        |


### Array Representation
* index가 있을 때
	* leftChild = (index*2)+1
	* rightChild = (index*2)+2
	* parent = (index-1)/2
