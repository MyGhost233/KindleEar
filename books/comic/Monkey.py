#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: insert0003 <https://github.com/insert0003>
from .cartoonmadbase import CartoonMadBaseBook

def getBook():
    return Monkey

class Hunter(CartoonMadBaseBook):
    title               = u'[漫画]Monkey Peak'
    description         = u'原創作者： 志名阪高次,粂田晃宏'
    language            = 'zh-tw'
    feed_encoding       = 'big5'
    page_encoding       = 'big5'
    mastheadfile        = 'mh_default.gif'
    coverfile           = 'cv_bound.jpg'
    feeds               = [(u'[漫画]Monkey Peak', 'https://www.cartoonmad.com/comic/5802.html')]
