from flask import jsonify, g, render_template


def render_json(code=200, msg="操作成功", data=None):
    if data is None:
        data = {}

    resp = {
        "code": code,
        "msg": msg,
        "data": data
    }
    return jsonify(resp)


def render_error_json(msg="系统繁忙，请稍后再试", data=None):
    if data is None:
        data = {}

    return render_json(code=-1, msg=msg, data=data)


def render_page(template, context=None):
    if context is None:
        context = {}

    if "current_user" in g:
        context["current_user"] = g.current_user
        context["movie_info"] = g.movie_info

    return render_template(template, **context)
