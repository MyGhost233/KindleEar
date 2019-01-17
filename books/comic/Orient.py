#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: insert0003 <https://github.com/insert0003>
from .manhuaguibase import ManHuaGuiBaseBook

def getBook():
    return Orient

class Orient(ManHuaGuiBaseBook):
    title               = u'[漫画]Orient'
    description         = u'原創作者： 大高忍'
    language            = 'zh-tw'
    feed_encoding       = 'big5'
    page_encoding       = 'big5'
    mastheadfile        = 'mh_default.gif'
    coverfile           = 'cv_bound.jpg'
    feeds               = [(u'[漫画]Orient', 'https://www.manhuagui.com/comic/28393/')]
