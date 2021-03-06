-- 고양이와 개는 몇 마리 있을까
SELECT ANIMAL_TYPE, COUNT(*) FROM ANIMAL_INS GROUP BY ANIMAL_TYPE ORDER BY ANIMAL_TYPE

-- 동명 동물 수 찾기
-- 동물 이름 중 두번이상 쓰인 이름 AND 해당 이름이 쓰인 횟수 조회
-- 이때 결과 이름없는 동물은 제외, 결과는 이름순
SELECT NAME, COUNT(*) AS COUNT FROM ANIMAL_INS GROUP BY NAME HAVING COUNT(NAME) >= 2 ORDER BY NAME


-- 입양시각 구하기(1)
SELECT HOUR(DATETIME), COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) >= 9 AND HOUR(DATETIME) < 20 GROUP BY HOUR(DATETIME) ORDER BY HOUR(DATETIME)


-- 입양시각 구하기(2)
SET @hour := -1; -- 변수선언

SELECT (@hour := @hour + 1) as HOUR, 
(SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hour) as COUNT
FROM ANIMAL_OUTS
WHERE @hour < 23