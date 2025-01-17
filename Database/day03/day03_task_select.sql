-- 2. 직원 데이터를 employees에 추가해주세요
INSERT INTO employees(name, position, salary) VALUES
	('혜린', 'PM', '9000'),
    ('은우', 'Frontend', '8000'),
    ('가을', 'Backend', '9200'),
    ('지수', 'Frontend', '7800'),
    ('민혁', 'Frontend', '9600'),
    ('하은', 'Backend', '13000');

-- 3. 모든 직원의 이름과 연봉 정보만을 조회하는 쿼리를 작성해주세요
SELECT name, salary FROM employees

-- 4. Frontend 직책을 가진 직원 중에서 연봉이 90000 이하인 직원의 이름과 연봉을 조회하세요.
SELECT name, salary
FROM employees
WHERE position = 'Frontend' AND salary <= 9000;