#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
from threading import Timer

TIME = 60.0 * 20 # 20 分钟提醒一次
# ps ax | grep index.py 结束进程

def notify():
    title = '20/20/20 rule'
    text = 'hava a break'
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))
    Timer(TIME, notify).start()

Timer(TIME, notify).start()