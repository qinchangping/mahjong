__author__ = 'qcp'
# -*- coding:utf-8 -*-
from numpy import *
from random import choice
from Player import *


def game():
    pileRest = generatePile()
    player1Cards = dealCard(pileRest, start=True)
    player1newCard = dealCard(pileRest, start=False)
    p1 = Player(player1Cards, player1newCard)
    # tableCards = []  # 桌子上被打出的牌
    # tableMingCards = []  # 桌子上的明牌，所有人杠和碰的牌
    print('game initialized.')
    # initialize

    p1.play(p1.tableCards, p1.tableMingCards)
    # isHu(player1Cards)


def test():
    # a = array([1, 1, 1, 3, 4])
    # b = array([1, 1, 1, 1, 2, 3, 4])
    # c = array([1, 1, 1, 2, 3, 4, 5, 6, 7, 11, 11, 12, 13, 14])
    # d = array([1, 1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 14])
    # print(whatHu(d))
    a = array([1, 1, 1, 2, 3, 4, 6, 11, 12, 13, 15, 16, 17])
    b = array([1, 1, 1, 1, 2, 3, 4, 5, 6, 11, 12, 13, 15, 15])
    c = array([1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 14, 15])
    d = array([1, 1, 1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 14])
    e = array([1, 1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 14, 15])
    # print(whatHu(d))

    #newCard = [5]
    #p1 = Player(a, newCard)
    # good

    p1 = Player(a)
    p1.newCard = [5]
    #p1.isHu(p1.handCards)

    #p.tableCards.append(2)
    #print('tableCards=', p1.tableCards)
    #print('tableMingCards=', p1.tableMingCards)

    #p1.tableMingCards.extend([6,6,6])
    #print('tableMingCards=', p1.tableMingCards)

    p1.play()
    #isShun2([1,1,2,3,3,4,5,6,9])

    #p1.play(p1.tableCards, p1.tableMingCards)
    #p1.tableCards.append(3)
    #print('tableCards=', p1.tableCards)
    #p2=Player(b)
    #print('tableCards=', p2.tableCards)


    #print(isShun(a))
    #print(whatHu(e))

# newCard = [2]
# p.tableCards.append(12)
# print('tableCards=',p.tableCards,p.tableMingCards)
# p.play(p.tableCards,p.tableMingCards)
# p.tableCards.append(p.discard())
#
# print(isKe(b))
# game()
# newCard = [1]
# p = Player(d, newCard)
#    p.play(p.tableCards, p.tableMingCards)
# isHu(c)
# print(isKe(b))
# isHu(b)
# print(findPair(a))
# print(findPair(b))
# print(findPair(c))
# print(isShun(a))
# print(isShun(b))
# print(isKe(b))
# print(howManySuits(a))
# print(howManySuits(c))
# isHu(c)
# print(c)


if __name__ == '__main__':
    test()



