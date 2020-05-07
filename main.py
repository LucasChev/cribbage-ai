from itertools import combinations
from random import shuffle

from card import card
from score import *

deck  = [card(i) for i in range(0,52)]
player_hand = []
ai_hand = []
crib = []

scores = [0,0]
deal = 0

while max(scores) < 121:
    
    ###### SETUP ######
    if len(deck) != 52:
        raise ValueError("deck len should be 52, [%d]"%len(deck))

    shuffle(deck)
    player_hand = [deck.pop() for i in range(6)]
    ai_hand = [deck.pop() for i in range(6)]
    deal ^= 1 # switch turns each time

    ###### SELECT ######

    #TODO implement AI behavior
    for comb in combinations(ai_hand,4):
        score_hand(comb)


    crib = [ai_hand.pop(), ai_hand.pop()]

    print("Select your hand")
    while len(player_hand) > 4:
        index = getValidIndex(player_hand)
        crib.append(player_hand.pop(index))

    # print("AI hand contains %s"%handToStr(ai_hand))
    
    flop = deck.pop()
    if flop.get_id() == 10:
        print("Counting nub for %s"%('Player' if deal==0 else 'AI'))
        scores[deal] += 2
        
    print("Flop is %s"%flop)
        
        
    ###### PLAY ######

    p1_turn = deal
    count = flop.get_val()
    h1 = player_hand.copy()
    h2 = ai_hand.copy()
    stack = [flop]
    
    while len(h1) > 0 or len(h2) > 0:
        print("count=%d"%count)
        
        if no_valid_move(h1,count) and no_valid_move(h2,count):
            print("%s played the last card, +%d point"%('Player' if p1_turn==0 else 'AI', 2 if count == 31 else 1))
            scores[p1_turn] += 2 if count == 31 else 1
            count = 0
            stack = []
            continue
        
        c = None
        
        if p1_turn:
            if no_valid_move(h1,count):
                print("Player can't play")
            else:
                index = getValidIndex(h1)
                c = h1.pop(index)
        else:
            if no_valid_move(h2,count):
                print("AI can't play")
            else:
                # TODO: Implement naive strategy
                c = min(h2)
                h2.remove(c)
                
        if c:
            print("%s played card %s"%("Player" if p1_turn else "Opponent",c))

            count += c.get_val()
            stack.insert(0,c)

            if count == 15:
                print("15 2: Counting 2 for %s"%('Player' if p1_turn else 'AI'))
                scores[p1_turn^1] += 2

            pair = mark_pair(stack)
            if pair > 0:
                print("pair: Counting %d for %s"%(pair,'Player' if p1_turn else 'AI'))
                scores[p1_turn^1] += pair

            run = mark_run(stack)
            if run > 0:
                print("run: Counting %d for %s"%(run,'Player' if p1_turn else 'AI'))
                scores[p1_turn^1] += run
                
        p1_turn ^= 1
    
    print("%s played the last card, +%d point"%('Player' if p1_turn==0 else 'AI', 2 if count == 31 else 1))
    scores[p1_turn] += 2 if count == 31 else 1

    print(scores)

    ###### SHOW ######
    print('Showing Cards')

    player_hand_score = score_hand(player_hand,flop)
    ai_hand_score = score_hand(ai_hand,flop)
    crib_score = score_hand(crib, flop)

    print('%s hand contains %s, marking %d points'%(('Player',player_hand,player_hand_score) if deal else 
                                                    ('AI',ai_hand,ai_hand_score)))
    scores[deal^1] += player_hand_score if deal else ai_hand_score

    if scores[deal^1] > 120:
        break

    print('%s hand contains %s, marking %d points'%(('AI',ai_hand,ai_hand_score) if deal else 
                                                    ('Player',player_hand,player_hand_score)))
    scores[deal] += ai_hand_score if deal else player_hand_score

    print('%s crib contains %s, marking %d points'%('AI' if deal else 'Player',crib,crib_score))
    scores[deal] += crib_score

    deck += player_hand + ai_hand + crib + [flop]
    player_hand = ai_hand = crib = None
    
    print(scores)
    
