# IS NULL

🐢 프로그래머스의 [SQL 키트](https://programmers.co.kr/learn/courses/30/parts/17045)를 통해 연습했습니다.

### 이름이 없는 동물의 아이디
```sql
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL
```

### 이름이 있는 동물의 아이디
```sql
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
```

### NULL 처리하기
```sql
SELECT ANIMAL_TYPE, IF(NAME IS NULL, 'No name', NAME), SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```