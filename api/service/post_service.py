from model.post import Post
from db.post_dao import select_post_by_id, select_posts, insert_post, update_post, delete_post_by_id


def get_post(id: int):
    res = select_post_by_id(id)
    return res if res is None else Post(id,
                                        res['author'],
                                        res['title'],
                                        res['content'],
                                        res['gen_time'],
                                        res['modify_time']
                                        )


def get_posts():
    res = select_posts()
    return res if res is None else [Post(r['id'],
                                         r['author'],
                                         r['title'],
                                         r['content'],
                                         r['gen_time'],
                                         r['modify_time']
                                         ) for r in res]


def add_post(post: Post):
    res, id = insert_post(post)
    return res, id


def update_post__(post: Post):
    res = update_post(post)
    return res


def delete_post(id: int):
    return delete_post_by_id(id)
