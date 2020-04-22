from model.user import User
from db.user_dao import insert_user, select_user_by_id, select_user_name_by_email


def get_user_service(id: int):
    res = select_user_by_id(id)
    return res if res is None else User(id, res['email'], res['name'])


def get_user_name_service(email: str):
    res = select_user_name_by_email(email)
    return res if res is None else res['name']


def add_user_service(user: User):
    res, id = insert_user(user)
    return res, id
