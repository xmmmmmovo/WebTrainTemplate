from flask import Blueprint, request

from exception.custom_exceptions import ContentEmptyException, DBException, DataNotFoundException
from exception.judge_utils import request_judge

from model.post import Post
from service.post_service import add_post_service, get_post_service, get_posts_service, update_post_service, \
    delete_post_service
from service.user_service import get_user_service

from response import response_success

post_bp = Blueprint('post_bp', __name__)


@post_bp.route('/<int:id>', methods=["GET"])
def get_info_by_id(id: int):
    if id == 0:
        raise DataNotFoundException()
    return response_success("success", get_post_service(id))


@post_bp.route('', methods=["GET"])
def get_infos():
    return response_success("success", get_posts_service())


@post_bp.route('', methods=["POST"])
def post_post():
    if request_judge(request, 'author', 'title', 'content', 'gen_time', 'modify_time'):
        raise ContentEmptyException()

    u = get_user_service(request.json['author'])
    if u is None:
        raise DataNotFoundException()
    res, id = add_post_service(Post(0,
                                    request.json['author'],
                                    request.json['title'],
                                    request.json['content'],
                                    request.json['gen_time'],
                                    request.json['modify_time']
                                    ))
    if res:
        return response_success("success", id)
    else:
        raise DBException()


@post_bp.route('', methods=["PUT"])
def update_post_():
    if request_judge(request, 'author', 'title', 'content', 'gen_time', 'modify_time'):
        raise ContentEmptyException()
    u = get_user_service(request.json['author'])
    if u is None:
        raise DataNotFoundException()
    res = update_post_service(Post(request.json['id'],
                                   request.json['author'],
                                   request.json['title'],
                                   request.json['content'],
                                   request.json['gen_time'],
                                   request.json['modify_time']
                                   ))
    if res:
        return response_success("success", '修改成功')
    else:
        raise DBException()


@post_bp.route('/<int:id>', methods=["DELETE"])
def delete_post_(id: int):
    if id == 0:
        raise DataNotFoundException()
    return response_success("success", delete_post_service(id))
