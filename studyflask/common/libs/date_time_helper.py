import datetime


def get_current_time(fmt="%Y-%m-%d %H:%M:%S"):
    dt = datetime.datetime.now()
    return dt.strftime(fmt)
