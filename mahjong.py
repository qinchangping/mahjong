__author__ = 'qcp'
# -*- coding:utf-8 -*-
# from numpy import *
from Game import *
from Player import *


def game():
    '''
    pileRest = generatePile()

    player1Cards = dealCard(pileRest, start=True)
    player2Cards = dealCard(pileRest, start=True)
    player3Cards = dealCard(pileRest, start=True)
    player4Cards = dealCard(pileRest, start=True)

    p1 = Player(player1Cards)
    p2 = Player(player2Cards)
    p3 = Player(player3Cards)
    p4 = Player(player4Cards)

    print('game initialized.')
    print('p1.handCards=', p1.handCards)
    print('p2.handCards=', p2.handCards)
    print('p3.handCards=', p3.handCards)
    print('p4.handCards=', p4.handCards)
    '''
    game_state = GameState()
    game_state.initGameRule()
    game_state.getState()
    #activePlayer = game_state.p1
    game_state.activePlayer.newCard = dealCard(pileRest, start=False)
    game_state.activePlayer.play()
    #while len(game_state.pileRest) > 0:
    #    game_state.activePlayer = game_state.nextPlayer()  # 看哪家碰or杠or胡
    #    game_state.activePlayer.play()
    print('This game is over.')


def test():
    a = array([1, 1, 1, 2, 3, 4, 6, 11, 12, 13, 15, 16, 17])
    b = array([1, 1, 1, 1, 2, 3, 4, 5, 6, 11, 12, 13, 15, 15])
    c = array([1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 14, 15])
    d = array([1, 1, 1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 14])
    e = array([1, 1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 14, 15])
    game()
    # newCard = [5]
    # p1 = Player(a, newCard)
    # good

    # p1 = Player(a)
    # p1.newCard = [4]
    #p1.play()
    #good

    # p1.isHu(p1.handCards)

    # p.tableCards.append(2)
    #print('tableCards=', p1.tableCards)
    #print('tableMingCards=', p1.tableMingCards)

    #p1.tableMingCards.extend([6,6,6])
    #print('tableMingCards=', p1.tableMingCards)


    #isShun2([1,1,2,3,3,4,5,6,9])

    #p1.play(p1.tableCards, p1.tableMingCards)
    #p1.tableCards.append(3)
    #print('tableCards=', p1.tableCards)
    #p2=Player(b)
    #print('tableCards=', p2.tableCards)


if __name__ == '__main__':
    test()



