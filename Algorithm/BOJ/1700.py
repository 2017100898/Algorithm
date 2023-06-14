N, K = list(map(int, input().split()))
mat = list(map(int, input().split()))

# 현재 사용중인 전기용품 리스트를 저장할 곳
now = list()

# 플러크를 뽑는 횟수
res = 0

# 전기용품 리스트 순회
for i in range (0, K):

    temp = list()
    
    # 현재 사용중인 전기용품의 개수가 한계보다 적을 때
    if len(now) < N:
        # 중복되는 전기용품을 사용하는 것이 아니라면, 추가해준다
        if mat[i] not in now:
            now.append(mat[i])
        else:
            pass

    # 한계에 도달했을 때
    else:
        # 앞으로 필요한 물건들을 순회하며, 현재 꽂혀있는 제품들 중 가장 나중에 필요한 물건을 찾음
        # 만약 앞으로 필요하지 않은 제품이 있다면 그것부터 뽑음
        for j in range(i, K):
            if mat[j] in now:
                # 현재 꽂혀있는 제품들 중 빠르게 필요한 순서대로 temp에 저장
                if mat[j] not in temp:
                    temp.append(mat[j])
        
        # 현재 쓰고 있는 모든 제품이 추후에 필요하다면, 가장 나중에 나오는 제품을 뽑고 다음 제품을 꽂음
        if len(temp) == len(now):
            # 다음 제품이 이미 꽂혀있다면, 뽑는 과정 굳이 필요하지 않으므로 패스
            if mat[i] not in now:
                now.remove(temp[-1])
                now.append(mat[i])
                # 뽑을 때마다 결과 + 1
                res += 1
        
        # 만약 앞으로 영원히 쓰지 않는 제품이 있다면, 그것부터 뽑고 다음 제품을 꽂음
        else:
            for k in range(0, len(now)):
                if now[k] not in temp:
                    if mat[i] not in now:
                        now.remove(now[k])
                        now.append(mat[i])
                        res += 1
                    break

print(res)