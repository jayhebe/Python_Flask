;
var member_register_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        $(".reg_wrap .do-reg").click(function () {
            var btn_target = $(this);
            if (btn_target.hasClass("disabled")) {
                common_ops.alert("正在处理，请不要重复提交请求");
                return;
            }
            var login_name = $(".reg_wrap input[name=login_name]").val();
            var nickname = $(".reg_wrap input[name=nickname]").val();
            var login_pwd = $(".reg_wrap input[name=login_pwd]").val();
            var confirm_pwd = $(".reg_wrap input[name=confirm_pwd]").val();
            var email = $(".reg_wrap input[name=email]").val();

            if (login_name == undefined || login_name.length < 1) {
                common_ops.alert("请输入正确的用户名");
                return;
            }

            if (nickname == undefined || nickname.length < 1) {
                nickname = login_name;
            }

            if (login_pwd == undefined || login_pwd.length < 6) {
                common_ops.alert("请输入正确的登录密码，密码长度不得小于6个字符");
                return;
            }

            if (confirm_pwd == undefined || confirm_pwd != login_pwd) {
                common_ops.alert("密码与登录密码不一致，请重新输入");
                return;
            }

            if (email == undefined || email.length < 1) {
                common_ops.alert("请输入正确的邮箱地址")
                return
            }

            btn_target.addClass("disabled");
            $.ajax({
                url: common_ops.buildUrl("/member/register"),
                type: "POST",
                data: {
                    login_name: login_name,
                    nickname: nickname,
                    login_pwd: login_pwd,
                    confirm_pwd: confirm_pwd,
                    email: email
                },
                dataType: "json",
                success: function (res) {
                    btn_target.removeClass("disabled");
                    var callback = null;
                    if (res.code == 200) {
                        callback = function () {
                            window.location.href = common_ops.buildUrl("/");
                        };
                    }
                    common_ops.alert(res.msg, callback);
                }
            });
        });
    }
};

$(document).ready(function () {
    member_register_ops.init();
});