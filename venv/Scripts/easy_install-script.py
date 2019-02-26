#!F:\牛客网算法\牛客网系列\牛客网项目课\牛客项目-VIP牛人计划\牛客网项目（高级）\代码\牛客高级项目课14课代码\venv\Scripts\python.exe -x
# EASY-INSTALL-ENTRY-SCRIPT: 'setuptools==39.1.0','console_scripts','easy_install'
__requires__ = 'setuptools==39.1.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('setuptools==39.1.0', 'console_scripts', 'easy_install')()
    )
