-- 새로운 MySQL 사용자 생성 및 권한 부여, 확인
create user 'fishbread_user'@'localhost' identified by 'fish_bread';
grant all privileges on *.* to 'fishbread_user'@'localhost';
flush privileges;
show grants for 'fishbread_user'@'localhost';

-- 데이터베이스 생성
create database fishbread_db;

-- fishbread_db를 사용한다.
use fishbread_db;

-- users 테이블 생성
create table users (
	user_id int auto_increment primary key, -- 고유 ID, 숫자가 자동으로 1씩 증가
	name varchar(255) not null, -- 사용자 이름(필수 입력값, 최대 255자 입력 가능)
	age int not null, -- 사용자 나이(필수 입력값, 숫자만 입력 가능)
    email varchar(100) unique, -- 사용자 이메일(선택사항, 중복된 값 허용 안함)
    is_business varchar(10) default false
);

-- orders 테이블 생성
create table orders (
	order_id int auto_increment primary key, -- 주문의 고유 ID
    user_id int,
    foreign key(user_id) references users (user_id),
    -- users 테이블의 user_id를 참조하는 외래키로 설정한다.
    order_date date, -- 주문 날짜를 저장하는데 사용한다.
    amount decimal(10,2)
    -- 주문 금액은 10자리 이하의 정수와 2자리 이하의 소수점으로 표현한다.
    );
    
-- inventory 테이블 생성
create table inventory (
	item_id int auto_increment primary key, -- 재고 항목의 고유 ID
    item_name varchar(255) not null, -- 재고 항목 이름
    quantity int not null -- 재고 수량
);

-- sales 테이블 생성
create table sales (
	sale_id int auto_increment primary key, -- 판매의 고유 ID
    order_id int,
    item_id int,
    foreign key(order_id) references orders (order_id), -- order_id의 외래키로 설정
    foreign key(item_id) references inventory (item_id), -- item_id의 외래키로 설정
    quantity_sold int not null -- 판매된 수량
);

-- daily_sales 테이블 생성
create table daily_sales (
	date date primary key, -- 날짜
    total_sales decimal(10,2) not null
    -- 총 매출(필수 입력값, 10자리 이하의 정수와 2자리 이하의 소수점으로 표현)
);