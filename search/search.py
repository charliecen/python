#!/usr/bin/env python
#coding:utf-8


f = file('contact_list','rb')
n = raw_input('Please enter your search: ')
m = 0
for line in f.xreadlines():
  if n in line:
    m += 1
    print  line.replace(n,"\033[1;31;40m%s\033[0m" % n)
print "找到%s纪录" % m