__author__ = 'qcp'
# -*- coding:utf-8 -*-
from numpy import *
# wan = [1, 2, 3, 4, 5, 6, 7, 8, 9] * 4
# tong = [11, 12, 13, 14, 15, 16, 17, 18, 19] * 4
# tiao = [21, 22, 23, 24, 25, 26, 27, 28, 29] * 4

class Player:
    tableCards = []  # 桌子上被打出的牌
    tableMingCards = []  # 桌子上的明牌，所有人杠和碰的牌
    # @classmethod
    # def nextPlayer(cls):
    # pass

    def __init__(self, handCards, newCard=[], mingCards=[], myTableCards=[]):
        self.handCards = list(handCards)
        self.newCard = newCard  # 新摸上的牌
        self.mingCards = mingCards  # 已经杠和碰的牌，明牌
        self.numPeng = 0
        self.numGang = 0
        self.numMing = self.numGang + self.numPeng  # 明牌套数
        self.myTableCards = myTableCards  # 桌面上自己打出的牌
        self.huList = []  # whatHu(self.handCards)
        # self.value = [1.0] * 27
        self.fan = 1  # 计算翻数
        self.score = 0

    def play(self):
        '''
        摸牌、计算、打出
        返回：
        '''
        self.gang()
        oldCards = self.handCards[:]
        print(oldCards)
        self.huList = self.whatHu(self.handCards)
        print('Before new card, huList=', self.huList)
        if self.newCard[0] in self.huList:
            # 计算期望收益
            print('Now you zimo le!')
        else:
            self.huProb()
        '''
        self.handCards += self.newCard
        self.handCards.sort()
        print(self.handCards)
        # dis = self.discard()
        # dis = 11
        # self.handCards.remove(dis)
        # self.myTableCards.append(dis)
        # tableCards.append(dis)
        self.gang()
        self.peng()
        if self.isHu():
            #计算期望收益
            pass
        else:
            self.calcP()
        # print('tableMingCards:', tableMingCards)

        self.ChooseDiscard()'''


    def ChooseDiscard(self):
        '''
        决定弃哪张牌,还没写好
        '''
        # print('handCards=', self.handCards)
        return 0

    def huGain(self):
        '''
        计算胡牌的收益，还没写好
        '''
        huList = self.huList[:]
        huProb = self.huProb()


        # print('handCards=', self.handCards)
        return 0

        # @staticmethod

    # def updateTableCards(Play,dis):
    # Play.tableCards.append(dis)

    def huProb(self):
        '''
        计算胡牌概率，所胡的牌在剩余未知牌中的张数
        '''
        # self.huList = self.whatHu(self.handCards)
        # print('huList = ', self.huList)
        huProb = []
        if len(self.huList) > 0:
            for i in range(len(self.huList)):
                count = self.handCards.count(self.huList[i]) + \
                        Player.tableCards.count(self.huList[i]) + \
                        Player.tableMingCards.count(self.huList[i])  # 所胡的牌已经出现了几张
                probility = (4.0 - float(count)) / float(
                    108 - len(self.handCards) - len(Player.tableCards) - len(Player.tableMingCards))
                huProb.append(probility)
            print('huProb = ', huProb)
        else:
            print('no Hu yet')
        return huProb

    def gang(self):
        '''
        杠牌
        '''
        gangFlag = False
        for item in set(self.handCards):  # 自摸杠牌
            if self.handCards.count(item) == 4:
                self.mingCards.extend([item] * 4)
                Player.tableMingCards.extend([item] * 4)
                self.numGang += 1
                self.numMing += 1
                self.fan = self.fan * 2
                print('zimo gang:', self.mingCards)
                for i in range(4): self.handCards.remove(item)
                print('after gang, handCards=', self.handCards)
                gangFlag = True

        if len(Player.tableCards) > 0:  # 杠别人牌
            lastCard = Player.tableCards[-1]
            numKe, keList = isKe(self.handCards)
            if lastCard in keList:
                self.mingCards.extend([lastCard] * 4)
                Player.tableMingCards.extend([lastCard] * 4)
                self.numGang += 1
                self.numMing += 1
                self.fan = self.fan * 2
                print('other gang:', self.mingCards)
                while (lastCard in self.handCards):
                    self.handCards.remove(lastCard)
                print('after gang, handCards=', self.handCards)
                gangFlag = True

        return gangFlag

#需要更改成两个函数，
# 1判断是否满足碰的条件，isPengable()
# 2判断是否要碰,peng()
    def peng(self):
        '''
        碰牌
        '''
        pengFlag = False
        if len(Player.tableCards) > 0:
            lastCard = Player.tableCards[-1]
            pairIndex = findPair(self.handCards)
            if len(pairIndex) > 0:
                for i in range(len(pairIndex)):
                    if lastCard == pairIndex[i][0]:
                        self.mingCards.extend([lastCard] * 3)
                        Player.tableMingCards.extend([lastCard] * 3)
                        self.numPeng += 1
                        self.fan = self.fan * 2
                        print('peng:', self.mingCards)
                        self.handCards.remove(lastCard)
                        self.handCards.remove(lastCard)
                        print('after peng, handCards=', self.handCards)
                        pengFlag = True
        return pengFlag


    def isHu(self, cards=[]):
        '''返回：
        cards胡多少张牌，类型int
        #wan = cards[cards < 10]
        #tong = cards[(cards > 10) & (cards < 20)]
        #tiao = cards[cards > 20]
    '''
        cards = array(cards)
        if len(cards) == 0:
            cards = array(self.handCards)
        countHu = 0
        pairIndex = findPair(cards)
        if (len(pairIndex) != 0):
            for i in range(len(pairIndex)):
                mianCards = cards.copy()
                mianCards[pairIndex[i][0]] = 0
                mianCards[pairIndex[i][1]] = 0
                mianCards = mianCards[mianCards > 0]  # 除去对子之后判断面牌是否四套
                # if len(mianCards)==12+self.numGang:
                if isTingPai(mianCards, self.numMing) == 1:
                    print('mianCards Hu le: ', mianCards)
                    print('with pair: ', cards[pairIndex[i][0]], cards[pairIndex[i][1]])
                    countHu += 1
        return countHu

    def whatHu(self, cards):
        '''返回：
        胡哪些牌，类型list
        '''
        wan = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        tong = [11, 12, 13, 14, 15, 16, 17, 18, 19]
        tiao = [21, 22, 23, 24, 25, 26, 27, 28, 29]
        fullList = wan + tong + tiao
        cards = list(cards)
        cardsPlus = cards + Player.tableCards + Player.tableMingCards
        cardSet = set(cardsPlus)
        huList = []
        # 删去桌上所有明牌中计数为4的牌，即除去已经打绝了不可能再出现的牌
        for item in cardSet:
            if cardsPlus.count(item) == 4:
                gangIndex = fullList.index(item)
                del fullList[gangIndex]
        # 在剩余的牌中看是否有自己可胡的牌
        for i in range(len(fullList)):
            newCards = cards.copy()
            newCards.append(fullList[i])
            newCards.sort()
            if self.isHu(newCards) > 0:
                print('if next card is ', fullList[i])
                huList.append(fullList[i])
        return huList


def isTingPai(cards, numMing=0):
    if howManySuits(cards) == 4 - numMing:
        # print('ting pai')
        return 1
    else:
        # print('not ting pai')
        return 0


def findPair(cards):
    '''返回：
    cards中对子的下标，类型list
    '''
    pairIndex = []
    for i in range(len(cards)):
        # restCards=cards[:i]+cards[i+1:]
        restCards = cards.copy()
        restCards[i] = 0
        for j in range(len(restCards)):
            if (i < j) & (cards[i] == restCards[j]):
                # print('pair found:', cards[i], cards[j])
                pairIndex.append([i, j])
    return pairIndex


def howManySuits(cards):
    '''返回：
    顺子+刻子的套数，类型int
    '''
    cards = list(cards)
    restCards = []
    numKe, keList = isKe(cards)
    if numKe != 0:
        for i in range(len(cards)):
            if cards[i] not in keList:
                restCards.append(cards[i])
        shunList = getShun(restCards)
    else:
        shunList = getShun(cards)
    numShun = len(shunList)
    # print(shunList)
    return numKe + numShun


def getShun(cards_):
    '''返回：
    顺子（三个牌连续）组成的list，每个元素是一套顺子牌list，如[[1, 2, 3], [2, 3, 4],[6,8]]
    按照从前到后的顺序查找，不能查找中间的顺子,如1234中的234
    '''
    shunList = []
    cards = cards_[:]

    if len(cards) < 3:
        return shunList
    else:
        item = cards[0]
        if item + 1 in cards and item + 2 in cards:
            shunList.append([item, item + 1, item + 2])
            cards.remove(item)
            cards.remove(item + 1)
            cards.remove(item + 2)
            # print('cards=',cards)
            # print('shunList=',shunList)
            shunList += getShun(cards)
        else:
            shunList += getShun(cards[1:])
        # print(shunList)
        return shunList


def isKe(cards):
    '''返回：
    刻子（三个牌相同）的个数，类型int
    刻子牌，类型list
    '''
    n = len(cards)
    cards = list(cards)
    countKe = 0
    keList = []
    if n < 3:
        print('cards must >=3')
    else:
        # for i in range(n - 2):
        i = 0
        while (i < n - 2):
            # if (cards[i] == cards[i + 1]) & (cards[i] == cards[i + 2]):
            if cards.count(cards[i]) == 3:
                keList.append(cards[i])
                countKe += 1
                i += 3
            else:
                i += 1
                # print(countKe)
                # print(keList)
    return countKe, keList


def isPair(cards):
    '''返回对子的个数，类型int
    '''
    n = len(cards)
    flag = 0
    pairList = []
    if n < 2:
        print('cards must >=2')
    else:
        for i in range(n - 1):
            if (cards[i] == cards[i + 1]):
                # print('pair: ', cards[i], cards[i + 1])
                pairList.append(cards[i])
                flag += 1
    pairSet = set(pairList)
    return len(pairSet)

