#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 全局通用配置类
import platform


class GlobalConfig():
    REDIS_URL = "redis://:123456@127.0.0.1:6379/0"

    # 配置日志
    LOG_LEVEL = "INFO"

    # 应用日志目录
    if platform.system() == "Linux":
        LOG_DIR = "/var/log/shorturl/info.log"
    else:
        LOG_DIR = "logs/info.log"
