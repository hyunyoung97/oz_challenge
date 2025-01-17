-- 1. employees 테이블을 생성해주세요
CREATE TABLE employees(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    position VARCHAR(100),
    salary DECIMAL(10, 2)
);

-- 2. 직원 데이터를 employees에 추가해주세요
INSERT INTO employees(name, position, salary) VALUES
	('혜린', 'PM', '9000'),
    ('은우', 'Frontend', '8000'),
    ('가을', 'Backend', '9200'),
    ('지수', 'Frontend', '7800'),
    ('민혁', 'Frontend', '9600'),
    ('하은', 'Backend', '13000');