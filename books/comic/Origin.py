#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: insert0003 <https://github.com/insert0003>
from .cartoonmadbase import CartoonMadBaseBook

def getBook():
    return Origin

class Hunter(CartoonMadBaseBook):
    title               = u'[漫画]Origin-源型機'
    description         = u'原創作者： Boichi'
    language            = 'zh-tw'
    feed_encoding       = 'big5'
    page_encoding       = 'big5'
    mastheadfile        = 'mh_default.gif'
    coverfile           = 'cv_bound.jpg'
    feeds               = [(u'[漫画]入间同学入魔了', 'https://www.cartoonmad.com/comic/7510.html')]
