__author__ = 'qcp'
# -*- coding:utf-8 -*-
from random import choice
from Player import *


def generatePile():
    '''返回：
    随机排序生成的初始牌堆，类型list
    '''
    pileRandom = []
    wan = [1, 2, 3, 4, 5, 6, 7, 8, 9] * 4
    tong = [11, 12, 13, 14, 15, 16, 17, 18, 19] * 4
    tiao = [21, 22, 23, 24, 25, 26, 27, 28, 29] * 4
    pileInit = wan + tong + tiao
    for i in range(108):
        card = choice(pileInit)
        pileRandom.append(card)
        # print(card)
        # pileInit=delete(pileInit,card)
        del pileInit[pileInit.index(card)]
        # print(len(pileInit))
    # print(pileRandom)
    return pileRandom


def dealCard(pileRest, start=False):
    '''
    牌局初start=True，返回牌堆最顶上13张牌，类型list
    之后start=False，返回牌堆最顶上1张牌，类型list
    '''
    retCard = []
    if len(pileRest) > 0:
        if start == True:  # 开局发牌13张
            retCard = pileRest[0:13]
            del pileRest[0:13]
        else:
            retCard = pileRest[0]
            del pileRest[0]
        print('after deal, %d cards left' % len(pileRest))
    else:
        print('no card left')
    return retCard


def nextPlayer():
    pass


class GameState:
    def __init__(self):
        self.pileRest = generatePile()
        player1Cards = dealCard(self.pileRest, start=True)
        player2Cards = dealCard(self.pileRest, start=True)
        player3Cards = dealCard(self.pileRest, start=True)
        player4Cards = dealCard(self.pileRest, start=True)
        self.p1 = Player(player1Cards)
        self.p2 = Player(player2Cards)
        self.p3 = Player(player3Cards)
        self.p4 = Player(player4Cards)
        print('game initialized.')
        self.activePlayer = self.p1
        # self.activePlayer.newCard = dealCard(pileRest, start=False)
        #self.activePlayer.play()

    def initGameRule(self):
        '''initialize the game'''
        # 事先约定好的规则，封顶，断19之类
        print('Rules are set as:')

    def nextPlayer(self):

        return self

    def getState(self):
        print('p1.handCards =', self.p1.handCards)
        print('p2.handCards =', self.p2.handCards)
        print('p3.handCards =', self.p3.handCards)
        print('p4.handCards =', self.p4.handCards)
