create database test;
use test;
create table post
(
    id          bigint auto_increment
        primary key,
    author      bigint                          not null,
    title       varchar(100) default 'no title' not null,
    content     varchar(500)                    not null,
    gen_time    bigint                          not null,
    modify_time bigint                          not null
);

INSERT INTO test.post (id, author, title, content, gen_time, modify_time) VALUES (3, 1, '22', 's', 1587471147911, 1587471147911);
INSERT INTO test.post (id, author, title, content, gen_time, modify_time) VALUES (4, 1, '22', 's2222', 1587471147911, 1587471147911);
INSERT INTO test.post (id, author, title, content, gen_time, modify_time) VALUES (5, 1, '22', 's', 1587471147911, 1587471147911);
INSERT INTO test.post (id, author, title, content, gen_time, modify_time) VALUES (6, 1, '22', 's', 1587471147911, 1587471147911);
INSERT INTO test.post (id, author, title, content, gen_time, modify_time) VALUES (7, 1, '22', 's', 1587471147911, 1587471147911);
INSERT INTO test.post (id, author, title, content, gen_time, modify_time) VALUES (8, 1, '22', 's', 1587471147911, 1587471147911);
INSERT INTO test.post (id, author, title, content, gen_time, modify_time) VALUES (9, 1, '22', 's', 1587471147911, 1587471147911);
INSERT INTO test.post (id, author, title, content, gen_time, modify_time) VALUES (10, 1, '22', 's', 1587471147911, 1587471147911);
INSERT INTO test.post (id, author, title, content, gen_time, modify_time) VALUES (11, 1, '22', 's', 1587471147911, 1587471147911);
INSERT INTO test.post (id, author, title, content, gen_time, modify_time) VALUES (12, 1, '22', 's', 1587471147911, 1587471147911);
INSERT INTO test.post (id, author, title, content, gen_time, modify_time) VALUES (13, 1, '22', 's', 1587471147911, 1587471147911);
create table user
(
    id    bigint auto_increment
        primary key,
    name  varchar(200) default 'anonymous' not null,
    email varchar(100)                     not null
);

INSERT INTO test.user (id, name, email) VALUES (1, '22', '11');
INSERT INTO test.user (id, name, email) VALUES (2, '22', '11');
INSERT INTO test.user (id, name, email) VALUES (3, '22', '11');
INSERT INTO test.user (id, name, email) VALUES (4, '22', '11');
INSERT INTO test.user (id, name, email) VALUES (5, '22', '11');