create database if not exists CTF_webboard;
use CTF_webboard;

create table if not exists Users
(
	id int(11) primary key not null auto_increment,
	username varchar(255) not null comment '用户名',
	password varchar(255) not null comment '密码',
	email varchar(255) not null comment '电子邮箱',
	points float(11,2) not null comment '获得分数（两位小数）',
	gender varchar(255) not null comment '性别' ,
	create_time time not null,
	update_time time not null
)default charset=utf8;

create table if not exists Problems
(
	id int(11) primary key not null auto_increment,
	name varchar(255) not null comment '题目名称',
	flag varchar(255) not null,
	content varchar(255) not null comment '题目描述',
	points float(11,2) not null comment '题目分数（两位小数)',
	create_time time not null,
	update_time time not null
)default charset=utf8;

create table if not exists WriteUp
(
	id int(11) primary key not null auto_increment,
	uid int(11) not null comment '所属用户',
	pid int(11) not null comment '所属题目',
	content varchar(255) not null,
	create_time time not null,
	update_time time not null
)default charset=utf8;

create table if not exists Record
(
	id int(11) primary key not null auto_increment,
	uid int(11) not null comment '提交用户',
	pid int(11) not null comment '提交问题',
	state int not null comment '提交结果',
	create_time time not null,
	update_time time not null
)default charset=utf8;




/*
	下面是原始数据的添加，在MySQL5.1版本下执行成功。

	NOW()函数以`'YYYY-MM-DD HH:MM:SS'返回当前的日期时间，可以直接存到DATETIME字段中。
	CURDATE()以’YYYY-MM-DD’的格式返回今天的日期，可以直接存到DATE字段中。
	CURTIME()以’HH:MM:SS’的格式返回当前的时间，可以直接存到TIME字段中。

	这里采用的是curtime记录时间。
*/

insert into Users 
(
	username,
	password,
	email,
	points,
	gender,
	create_time,
	update_time
)
values
(
	"duhbe",
	"85b2f42582a1606d79a8741d3f26e595",
	"dubhe@dubehe.com",
	10,
	"M",
	curtime(),
	curtime()
);

insert into Problems 
(
	name,
	flag,
	content,
	points,
	create_time,
	update_time
)
values
(
	"Web Puzzle 01",
	"flag{dubhe_best}",
	"dubhe@dubehe.com",
	10,
	curtime(),
	curtime()
);

insert into WriteUp
(
	uid,
	pid,
	content,
	create_time,
	update_time
)
values
(
	0,
	0,
	"this is a WriteUp",
	curtime(),
	curtime()
);

insert into Record
(
	uid,
	pid,
	state,
	create_time,
	update_time
)
values
(
	0,
	0,
	0,
	curtime(),
	curtime()
);
