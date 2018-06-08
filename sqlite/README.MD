进入某个数据库（以test.sqlite为例）
sqlite3 test.sqlite
回车进入命令行模式

帮助入口
.help

显示数据库中的所有表
.tables

创建一个表
CREATE TABLE athletes(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    dob DATE NOT NULL);

向表中插入数据
INSERT INTO athletes (name,dob) VALUES ("jason",2018);

查询表中的所有数据
select * from athletes;

查询表中的所有name
select name from athletes;

切换查询结果的显示模式
.mode list|line|（更多模式参考.help）

更多用法参考sqlite语法