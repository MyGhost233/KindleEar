#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: insert0003 <https://github.com/insert0003>
from .cartoonmadbase import CartoonMadBaseBook

def getBook():
    return OVERLORD

class Hunter(CartoonMadBaseBook):
    title               = u'[漫画]OVERLORD'
    description         = u'原創作者： 丸山くがね, 深山フギン'
    language            = 'zh-tw'
    feed_encoding       = 'big5'
    page_encoding       = 'big5'
    mastheadfile        = 'mh_default.gif'
    coverfile           = 'cv_bound.jpg'
    feeds               = [(u'[漫画]OVERLORD', 'https://www.cartoonmad.com/comic/4662.html')]
