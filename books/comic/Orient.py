#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: insert0003 <https://github.com/insert0003>
from .cartoonmadbase import CartoonMadBaseBook

def getBook():
    return Orient

class Hunter(CartoonMadBaseBook):
    title               = u'[漫画]Orient'
    description         = u'原創作者： 大高忍'
    language            = 'zh-tw'
    feed_encoding       = 'big5'
    page_encoding       = 'big5'
    mastheadfile        = 'mh_default.gif'
    coverfile           = 'cv_bound.jpg'
    feeds               = [(u'[漫画]Orient', 'https://www.cartoonmad.com/comic/7915.html')]
