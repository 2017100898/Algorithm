# GROUP BY

🐢 프로그래머스의 [SQL 키트](https://programmers.co.kr/learn/courses/30/parts/17044)를 통해 연습했습니다.

### 고양이와 개는 몇 마리 있을까
```sql
SELECT ANIMAL_TYPE, COUNT(ANIMAL_ID) AS 'count'
FROM ANIMAL_INS
WHERE ANIMAL_TYPE IN ('Cat', 'Dog')
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE;
```

### 동명 동물 수 찾기
```sql
SELECT NAME, COUNT(ANIMAL_ID) AS COUNT
FROM ANIMAL_INS
WHERE NAME != 'Null'
GROUP BY NAME HAVING COUNT >= 2
ORDER BY NAME;
```

### 입양 시각 구하기(1)
```sql
SELECT HOUR(DATETIME) AS HOUR, COUNT(ANIMAL_ID) AS COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR(DATETIME) HAVING HOUR >= 9 AND HOUR <20
ORDER BY HOUR(DATETIME);
```
