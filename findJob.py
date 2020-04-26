# _*_coding:utf-8_*_
# Author      :ories  
# File_Name   :findJob.py    
# Create_Date :2020-02-12 19:58
# Description :
# IDE         :PyCharm
import random
import sys

from pymouse import PyMouse
from pykeyboard import PyKeyboard

from time import sleep

m = PyMouse()
k = PyKeyboard()


def dialog_once():
    t = round(random.uniform(2.0, 3.0), 2)
    sleep(t)
    m.click(685, 262, 1)
    sleep(t)
    m.click(740, 760, 1)
    sleep(t)
    m.click(740, 760, 1)
    sleep(t)
    m.click(470, 768, 1)
    sleep(t)
    m.click(662, 703, 1)
    sleep(t)
    # 点击发送
    m.click(870, 760, 1)
    sleep(t)
    # m.click(754, 497, 1) # 这句话解决温馨提示的弹窗
    # sleep(t)
    # m.click(567, 497, 1)  # 这句话解决温馨提示的弹窗,点取消
    # sleep(t)

    m.click(456, 90, 1)
    sleep(t)
    m.click(456, 90, 1)


def switch():
    m.press(680, 440)
    sleep(1)
    m.drag(685, 270)
    sleep(0.1)
    m.release(685, 270)


def start():
    sleep(1.5)
    dialog_once()
    sleep(3)
    switch()


for n in range(sys.maxsize):
    start()
