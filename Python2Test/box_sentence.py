# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 22:19:38 2015

@author: Administrator
"""

sentence = raw_input("sentence:")

screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2

print
print ' ' *left_margin + '+' + '-' *(box_width - 2) +  '+'
print ' ' *(left_margin + 1) + '| ' + ' ' * text_width     + ' |'
print ' ' *(left_margin + 1) + '| ' +       sentence       + ' |'
print ' ' *(left_margin + 1) + '| ' + ' ' * text_width     + ' |'
print ' ' *left_margin + '+' + '-' *(box_width - 2) +  '+'
print