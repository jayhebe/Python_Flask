from flask import Blueprint, render_template, request, make_response, redirect

from application import db
from common.libs.helper import render_json, render_error_json
from common.libs.date_time_helper import get_current_time
from common.libs.user_service import UserService
from common.libs.url_manager import UrlManager
from common.models.user import User

member_page = Blueprint("member_page", __name__)


@member_page.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        req = request.values
        login_name = req["login_name"] if "login_name" in req else ""
        nickname = req["nickname"] if "nickname" in req else ""
        login_pwd = req["login_pwd"] if "login_pwd" in req else ""
        confirm_pwd = req["confirm_pwd"] if "confirm_pwd" in req else ""
        email = req["email"] if "email" in req else ""

        if login_name is None or len(login_name) < 1:
            return render_error_json(msg="请输入正确的用户名")

        if login_pwd is None or len(login_pwd) < 6:
            return render_error_json(msg="请输入正确的登录密码，密码长度不得小于6个字符")

        if confirm_pwd is None or login_pwd != confirm_pwd:
            return render_error_json(msg="密码与登录密码不一致，请重新输入")

        if nickname is None or len(nickname) < 1:
            nickname = login_name

        if email is None or len(email) < 1:
            return render_error_json(msg="请输入正确的邮箱地址")

        user_info = User.query.filter_by(login_name=login_name).first()
        if user_info:
            return render_error_json(msg="用户名已经被注册")

        email_info = User.query.filter_by(email=email).first()
        if email_info:
            return render_error_json(msg="邮箱已经被注册")

        model_user = User()
        model_user.login_name = login_name
        model_user.nickname = nickname
        model_user.login_salt = UserService.get_salt(6)
        model_user.login_pwd = UserService.generate_pwd(login_pwd, model_user.login_salt)
        model_user.email = email
        model_user.created_time = get_current_time()
        model_user.updated_time = get_current_time()

        db.session.add(model_user)
        db.session.commit()

        return render_json(msg="注册成功")

    return render_template("member/register.html")


@member_page.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        req = request.values
        login_name = req["login_name"] if "login_name" in req else ""
        login_pwd = req["login_pwd"] if "login_pwd" in req else ""

        if login_name is None or len(login_name) < 1:
            return render_error_json(msg="用户名不能为空")

        if login_pwd is None or len(login_pwd) < 1:
            return render_error_json(msg="登录密码不能为空")

        user_info = User.query.filter_by(login_name=login_name).first()
        if not user_info:
            return render_error_json(msg="登录失败，用户名或密码错误(-1)")

        if user_info.login_pwd != UserService.generate_pwd(login_pwd, user_info.login_salt):
            return render_error_json(msg="登录失败，用户名或密码错误(-2)")

        if user_info.status != 1:
            return render_error_json(msg="用户已被禁用，请与管理员联系")

        response = make_response(render_json(msg="登录成功"))
        auth_code = UserService.generate_auth_code(user_info)
        response.set_cookie("auth_cookie",  auth_code + "#" + str(user_info.id), 60 * 60 * 24)

        return response

    return render_template("member/login.html")


@member_page.route("/logout", methods=["GET", "POST"])
def logout():
    response = make_response(redirect(UrlManager.build_url("/")))
    response.delete_cookie("auth_cookie")

    return response
