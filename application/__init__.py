#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging
from logging.handlers import TimedRotatingFileHandler
from flask_redis import FlaskRedis
from flask import Flask


from application import settings
# from application.settings.dev import DevelopmentConfig
# from application.settings.pro import ProductionConfig
from application.settings import Config

redis_client = FlaskRedis()


# 增加日志模块
def setup_log(Config):
    # 设置日志等级
    logging.basicConfig(level=Config.LOG_LEVEL)
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    # file_log_handler=RotatingFileHandler('log/log',maxBytes=1024 * 1024 * 300, backupCount=10)

    # 按照时间分隔日志
    file_log_handler = TimedRotatingFileHandler(settings.Config.LOG_DIR, when='D', )

    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flaskapp使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


def init_app():
    '项目初始化'
    # 主应用的根目录
    app = Flask(__name__)
    # 设置配置类
    # Config = config[settings.Config.ENV]
    # Config

    # 加载配置
    app.config.from_object(Config)

    # redis
    redis_client.init_app(app)

    # 开启CSRF防范
    # CsrfProtect(app)
    # 启用日志
    setup_log(Config)

    # 注册蓝图
    from .apps.index import index

    # 路由绑定
    app.register_blueprint(index, url_prefix='')

    return app
