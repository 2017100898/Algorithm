# SUM, MAX, MIN

🐢 프로그래머스의 [SQL 키트](https://programmers.co.kr/learn/courses/30/parts/17043)를 통해 연습했습니다.

### 최댓값 구하기
```sql
SELECT MAX(DATETIME) AS "시간"
FROM ANIMAL_INS;
```

### 최솟값 구하기
```sql
SELECT MIN(DATETIME) AS "시간"
FROM ANIMAL_INS;
```

### 동물 수 구하기
```sql
SELECT COUNT(ANIMAL_ID) AS "count"
FROM ANIMAL_INS;
```

### 중복 제거하기
```sql
SELECT COUNT(DISTINCT NAME)
FROM ANIMAL_INS
WHERE NAME != "NULL";
```