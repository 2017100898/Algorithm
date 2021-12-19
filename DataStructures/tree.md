# 트리 (Tree)
* Tree는 Cycle이 없고 위아래 관계만이 있다.
* 부모와 자식을 고유하게 가지면서 Recursive와 Cycle이 존재하지 않는 2차원 자료구조다.

## Binary Tree
* Binary Tree는 최대 2개의 자식 노드를 가지는 Tree다.
* Height가 h인 Full Tree의 노드 개수는 **2^h-1** 이다.

## Binary Search Tree
* BST는 왼쪽 자식 노드는 자신보다 작고 오른쪽 자식 노드는 자신보다 큰 형태의 Tree다.
* 왼쪽과 오른쪽이 반대가 되어도 BST이다.
* 순서에 따라 모양이 달라지고 동일한 데이터라도 넣는 순서에 따라 최고, 최악으로 효율이 갈릴 수 있다.
* Pruning을 통해 연산 속도를 높일 수 있다.

## Tree Traversal
* Inorder : 왼쪽 - 자신 - 오른쪽
* Postorder : 왼쪽 - 오른쪽 - 자신
* Preorder : 자신 - 왼쪽 - 오른쪽