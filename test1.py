__author__ = 'qcp'
# -*- coding:utf-8 -*-
'''
def f(a):
    aa=a[:]
    aa.remove(a[0])
    #del a[0]
    return aa

a1=[1,2,3]
b=f(a1)
print(b)
print(a1)
#remove和del操作都是在原数组上操作，传入参数也是如此
'''
# i = 0
# if cards[i] + 1 in cards and cards[i] + 2 in cards:
# shunList.append([cards[i], cards[i] + 1, cards[i] + 2])
# print(shunList)
#    cards.remove(cards[i])
#    cards.remove(cards[i]+1)此处card[i]已经不是上一行的card[i]了，兄弟！
#    cards.remove(cards[i]+2)
def init():
    a=1
    b=2

init()
c=a+b