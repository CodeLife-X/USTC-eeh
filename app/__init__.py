#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import Flask
from datetime import timedelta

app = Flask(__name__)

# 设置静态文件缓存过期时间
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)

from app import routes
