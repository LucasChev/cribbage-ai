from itertools import combinations
from random import shuffle

from card import card
from score import *

deck  = [card(i) for i in range(0,52)]
player_hand = []
ai_hand = []
crib = []

scores = [0,0]
ai_deal = 0

while max(scores) < 121:
    
    ###### SETUP ######
    if len(deck) != 52:
        raise ValueError("deck len should be 52, [%d]"%len(deck))

    shuffle(deck)
    ai_hand = [deck.pop() for i in range(6)]
    ai_deal ^= 1 # switch turns each time

    ###### SELECT ######
    print("%s's deal (crib belongs to %s)"%('AI' if ai_deal else 'Player','AI' if ai_deal else 'Player'))
    # TODO: add memoization to prevent repeated scoring of duplicate hands
    # AI strategy is to select the hand with the highest expected score for all possible flops
    # Could be more sophisticated (endgame, crib min/max), but that's not quite the point of this project
    max_score = -1
    max_comb = []
    for comb in combinations(ai_hand,4):
        curr_score = 0
        for i in range(len(deck)):
            curr_score += score_hand(list(comb),deck[i])
        # print("score for %s is %d"%(comb,curr_score))
        if curr_score > max_score:
            max_score = curr_score
            max_comb = comb

    player_hand = [deck.pop() for i in range(6)]


    # print("hand was %s, best hand was %s with score %d"%(ai_hand,max_comb,max_score))


    crib = [ai_hand.pop(), ai_hand.pop()]

    print("Select your hand")
    while len(player_hand) > 4:
        index = getValidIndex(player_hand)
        crib.append(player_hand.pop(index))

    # print("AI hand contains %s"%handToStr(ai_hand))
    
    flop = deck.pop()
    if flop.get_id() == 10:
        scores[ai_deal] += 2
        print("%s: Counting nub for %s"%(scores, 'AI' if ai_deal else 'Player'))
        
    print("Flop is %s"%flop)
        

    ###### PLAY ######
    p1_turn = ai_deal
    count = flop.get_val()
    h1 = player_hand.copy()
    h2 = ai_hand.copy()
    stack = [flop]
    
    while len(h1) > 0 or len(h2) > 0:
        print("count=%d"%count)
        player_str = "Player" if p1_turn else "AI"
        
        if no_valid_move(h1,count) and no_valid_move(h2,count):
            scores[p1_turn] += 2 if count == 31 else 1
            print("%s: %s played the last card, +%d point"%(scores,'Player' if p1_turn==0 else 'AI', 2 if count == 31 else 1))
            count = 0
            stack = []
            continue
        
        c = None
        if p1_turn:
            if no_valid_move(h1,count):
                print("Player can't play")
            else:
                index = getValidCard(h1,count)
                c = h1.pop(index)
        else:
            if no_valid_move(h2,count):
                print("AI can't play")
            else:
                # TODO: Implement naive strategy
                max_score = -1
                max_option = None
                for card in h2:
                    curr_score = mark_pair([card]+stack) + mark_run([card]+stack) + 2*int(count+card.get_val() == 15)
                    # print("score for %s is %d"%(card,curr_score))
                    if curr_score > max_score:
                        max_score = curr_score
                        max_option = card
                
                # print("hand was %s, best option was %s with score %d"%(h2,max_option,max_score))

                c = max_option
                print(c)
                h2.remove(c)
                
        if c:
            print("%s played card %s"%(player_str, c))

            count += c.get_val()
            stack.insert(0,c)

            if count == 15:
                scores[p1_turn^1] += 2
                print("%s: 15 2: Counting 2 for %s"%(scores, player_str))

            pair = mark_pair(stack)
            if pair > 0:
                scores[p1_turn^1] += pair
                print("%s: pair: Counting %d for %s"%(scores,pair, player_str))

            run = mark_run(stack)
            if run > 0:
                scores[p1_turn^1] += run
                print("%s: run: Counting %d for %s"%(scores,run, player_str))
                
        p1_turn ^= 1
    
    scores[p1_turn] += 2 if count == 31 else 1
    print("%s: %s played the last card, +%d point"%(scores,'Player' if p1_turn==0 else 'AI', 2 if count == 31 else 1))

    print(scores)

    ###### SHOW ######
    print('Showing Cards')
    player_hand_score = score_hand(player_hand,flop)
    ai_hand_score = score_hand(ai_hand,flop)
    crib_score = score_hand(crib, flop)


    if ai_deal:
        print('Player hand contains %s, %s: marking %d points'%(flop,player_hand,player_hand_score))
        scores[0] += player_hand_score
    else:
        print('AI hand contains %s, %s: marking %d points'%(flop,ai_hand,ai_hand_score))
        scores[1] += ai_hand_score

    if scores[ai_deal^1] > 120:
        break

    if ai_deal:
        print('AI hand contains %s, %s: marking %d points'%(flop,ai_hand,ai_hand_score))
        print('AI crib contains %s, %s: marking %d points'%(flop,crib,crib_score))
        scores[1] += ai_hand_score + crib_score
    else:
        print('Player hand contains %s, %s: marking %d points'%(flop,player_hand,player_hand_score))
        print('Player crib contains %s, %s: marking %d points'%(flop,crib,crib_score))
        scores[0] += player_hand_score + crib_score


    deck += player_hand + ai_hand + crib + [flop]
    player_hand = ai_hand = crib = None
    
    print(scores)
    
## End while loop

if score[0] > 120:
    print("Player has won the game! Final score is %s"%score)
elif score[1] > 120:
    print("AI has won the game! Final score is %s"%score)
else:
    raise ValueError("Game ended with score %s"%score)
