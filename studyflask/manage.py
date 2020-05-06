from www import *
from application import manager
from flask_script import Server


manager.add_command("runserver", Server(host="0.0.0.0", use_debugger=True, use_reloader=True))


def main():
    manager.run()


if __name__ == "__main__":
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()
