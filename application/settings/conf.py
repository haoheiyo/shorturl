#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 全局通用配置类
import platform


class GlobalConfig():
    REDIS_URL = "redis://:Mimashisha@172.86.126.81:6379/0"

    # 配置日志
    LOG_LEVEL = "INFO"

    # 应用日志目录
    if platform.system() == "Linux":
        LOG_DIR = "/var/log/shorturl/log"
    else:
        LOG_DIR = "logs/log"
