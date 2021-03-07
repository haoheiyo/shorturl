#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib.parse

from flask import render_template, request, jsonify, redirect, url_for

from . import index
from .service import short


@index.route('/')
def index_blu():
    return "hello,this is 首页!"


@index.route('/<key>')
def expand(key):
    url = short.get_expand_url(key)
    if url:
        url = urllib.parse.unquote(url)
        return redirect(url, 301)
    else:
        return redirect(url_for("index.index_blu"), 302)


@index.route('/shorten')
def shorten():
    url = request.args.get("url","")
    if short.check_url(url):
        url = urllib.parse.quote(url)
        shorten_key = short.add_expand_url(url)
        data = {"error": 0, "msg": "", "short": "https://b7.cm/" + str(shorten_key)}
    else:
        data = {"error": 1001, "msg": "url格式错误！", "short": ""}
    return jsonify(data)
