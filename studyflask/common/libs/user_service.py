import hashlib
import random
import string


class UserService:
    @staticmethod
    def get_salt(length=16):
        salt = ""
        for i in range(length):
            salt += random.choice(string.ascii_letters + string.digits)

        return salt

    @staticmethod
    def generate_pwd(pwd, salt):
        hlmd5 = hashlib.md5()
        pwd = pwd + salt
        hlmd5.update(pwd.encode("utf-8"))

        return hlmd5.hexdigest()

    @staticmethod
    def generate_auth_code(user_info=None):
        hlmd5 = hashlib.md5()
        code = user_info.login_name + user_info.login_pwd + user_info.login_salt + str(user_info.status)
        hlmd5.update(code.encode("utf-8"))

        return hlmd5.hexdigest()
