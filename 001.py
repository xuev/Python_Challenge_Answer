#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author:      xuev <xuewei918@gmail.com>
@Project:     Python_Challenge_Answer
@File:        001.py
@Version:     0.1
@License:     MIT Licence 
@Create Time: 16/8/22 23:42
@Description: Python_Challenge_Answer - 001.py
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

hints = 'g fmnc wms bgblr rpylqjyrc gr zw fylb.\n' \
        'rfyrq ufyr amknsrcpq ypc dmp.\n' \
        'bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle.\n' \
        'sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.\n' \
        'lmu ynnjw ml rfc spj.'

str_url = 'map'


def trans(str):
    list_base = list(str)
    tr = []
    for i in range(len(list_base)):
        if list_base[i] not in alphabet[:]:
            tr.append(list_base[i])
        else:
            for n in range(len(alphabet)):
                if list_base[i] == alphabet[n] and n <= 23:
                    tr.append(alphabet[n + 2])
                elif list_base[i] == alphabet[n]:
                    tr.append(alphabet[n - 24])
    list_tr = ''.join(tr)
    return list_tr


print '-----------------------------------------------------------------------'
print trans(hints)
print '-----------------------------------------------------------------------'
print "Translate the tail of current url 'map' with trans()"
print "'map' --> " + '\'' + trans(str_url) + '\''
print '-----------------------------------------------------------------------'

# The translation result:
#
# i hope you didnt translate it by hand.
# thats what computers are for.
# doing it in by hand is inefficient and that's why this text is so long.
# using string.maketrans() is recommended.
# -------------------------------------------------

print 'Visit http://www.pythonchallenge.com/pc/def/' + trans(str_url) + '.html for net challenge.\n'
print 'To see the official solutions, replace pc with pcc, \n' \
      'i.e. go to: http://www.pythonchallenge.com/pcc/def/ocr.html'
