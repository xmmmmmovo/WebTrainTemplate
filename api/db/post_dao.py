from model.post import Post
from db.mysql_operator import MysqlOp


def select_post_by_id(id: int):
    return MysqlOp().select_one("select * from post where id = '%s'", (id))


def select_posts():
    return MysqlOp().select_all("select * from post")


def insert_post(post: Post):
    op = MysqlOp()
    res = op.op_sql("insert into post(author, title, content, gen_time, modify_time) "
                    "values (%s, %s, %s, %s, %s)",
                    (post.author, post.title, post.content, post.gen_time, post.modify_time))
    return res, op.cur.lastrowid


def update_post(post: Post):
    op = MysqlOp()
    res = op.op_sql("update post set "
                    "author = %s, title = %s, content = %s, gen_time = %s, modify_time = %s "
                    "where id = %s",
                    (post.author, post.title, post.content, post.gen_time, post.modify_time, post.id))
    return res


def delete_post_by_id(id: int):
    return MysqlOp().op_sql('delete from post where id = %s', (id))
