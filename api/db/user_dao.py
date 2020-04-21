from model.user import User
from db.mysql_operator import MysqlOp


def select_user_by_id(id: int):
    return MysqlOp().select_one("select * from user where id = %s", (id))


def select_user_name_by_email(email: int):
    return MysqlOp().select_one("select name from user where email = %s", (email))


def insert_user(user: User):
    op = MysqlOp()
    res = op.op_sql("insert into user(email, name) values (%s, %s)",
                    (user.email, user.name))
    return res, op.cur.lastrowid
