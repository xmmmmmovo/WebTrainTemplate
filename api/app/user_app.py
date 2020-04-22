from flask import Blueprint, request

from exception.custom_exceptions import ContentEmptyException, DBException, DataNotFoundException
from exception.judge_utils import request_judge

from model.user import User
from service.user_service import add_user_service, get_user_service

from response import response_success

user_bp = Blueprint('user_app', __name__)


@user_bp.route("/<int:id>", methods=["GET"])
def get_info_by_id(id: int):
    if id == 0:
        raise DataNotFoundException()
    return response_success("success", get_user_service(id))


@user_bp.route('', methods=["POST"])
def post_user():
    if request_judge(request, 'email', 'name'):
        raise ContentEmptyException()

    res, id = add_user_service(User(0, request.json['email'], request.json['name']))

    if res:
        return response_success("success", id)
    else:
        raise DBException()
