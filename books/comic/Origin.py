#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: insert0003 <https://github.com/insert0003>
from .manhuaguibase import ManHuaGuiBaseBook

def getBook():
    return Origin

class Origin(ManHuaGuiBaseBook):
    title               = u'[漫画]Origin-源型機'
    description         = u'原創作者： Boichi'
    language            = 'zh-tw'
    feed_encoding       = 'big5'
    page_encoding       = 'big5'
    mastheadfile        = 'mh_default.gif'
    coverfile           = 'cv_bound.jpg'
    feeds               = [(u'[漫画]Origin-源型機', 'https://www.manhuagui.com/comic/26942/')]
