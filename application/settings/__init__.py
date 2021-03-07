#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .dev import DevelopmentConfig
from .pro import ProductionConfig
# from .conf import GlobalConfig




class Set_env(object):
    """项目配置核心类"""
    # 配置环境
    ENV = 'dev'


config = {
    'dev': DevelopmentConfig,
    'pro': ProductionConfig,

}
Config = config[Set_env.ENV]