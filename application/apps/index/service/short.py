#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random
from application import redis_client


def gen_key():
    num_set = [chr(i) for i in range(48, 58)]
    char_set1 = [chr(i) for i in range(65, 91)]
    char_set2 = [chr(i) for i in range(97, 123)]
    total_set = num_set + char_set1 + char_set2
    value_set = "".join(random.sample(total_set, 4))
    return value_set


def check_url(url):
    if url.startswith("http://") or url.startswith("https://"):
        return True


def add_expand_url(url):
    key = redis_client.get(url)
    if key:
        return key.decode()
    else:
        key = gen_key()
        redis_client.set(key, url)
        redis_client.set(url, key)
        return key


def get_expand_url(key):
    url = redis_client.get(key)
    if url:
        return url.decode()


if __name__ == '__main__':
    key = check_url("https://123123")
    print(key)
