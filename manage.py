#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask_script import Manager
from application import init_app

app = init_app()

# 使用终端管理工具
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
