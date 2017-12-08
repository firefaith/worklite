
create database worklite;

use mysql;
-- add user error way:
-- insert into user (Host,User,authentication_string) values('localhost','chunying',password('123456'));
-- ERROR 1364 (HY000): Field 'ssl_cipher' doesn't have a default value

-- correct way:
GRANT USAGE ON worklite.* TO 'chunying'@'localhost' IDENTIFIED BY '123456' WITH GRANT OPTION;
