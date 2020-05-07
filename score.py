from itertools import combinations

def flush(hand, flip = None):
    suit = hand[0].get_suit()
    if len([x for x in hand if x.get_suit() == suit]) == 4:
        return 5 if flip and flip.get_suit()==suit else 4
    return 0
    
def pairs(hand):
    return 2*len([x for x in list(combinations(hand,2)) if x[0].get_id() == x[1].get_id()])    
    
def runs(hand):
    sort = sorted([c.get_id() for c in hand])
    def recurse(arr, subarr, i, n):
        if i == len(arr):
            if len(subarr) == n:
                res.append(subarr)
        else:
            recurse(arr, subarr.copy(), i+1, n)
            if len(subarr) == 0 or subarr [-1] == arr[i]-1:
                subarr.append(arr[i])
                recurse(arr, subarr.copy(), i+1, n)
    
    for i in range(len(hand),2,-1):
        res = []    
        recurse(sort, [], 0, i)
        if len(res) > 0:
            break
            
    return sum([len(x) for x in res])

def fifteens(hand):
    subset_list = []
    for i in [2,3,4,5]:
        subset_list += combinations(hand,i)
    return 2*len([subset for subset in subset_list if sum(c.get_val() for c in subset) == 15])    

def nub(hand,flip):
    if flip:
        return len([x for x in hand if x.get_id() == 10 and x.get_suit() == flip.get_suit()])
    return 0

def score_hand(hand,flip,debug=False):
    
    if debug:
        print('scoring hand: ',hand+[flip])
    
    score = 0
    
    #fifteens
    score += fifteens(hand+[flip])
    if debug:
        print('after fifteens ', score)
    #runs
    score += runs(hand+[flip])
    if debug:
        print('after runs ', score)
    #pairs
    score += pairs(hand+[flip])
    if debug:
        print('after pairs ', score)
    #flush
    score += flush(hand, flip)
    if debug:
        print('after flush ', score)
    #nub
    score += nub(hand,flip)
    if debug:
        print('after nub ', score)
    
    return score

def mark_run(s):
    
    def run_score(cards):
        sorted_cards = sorted(cards)
        flag = False
        for i in range(len(sorted_cards)-1):
            if sorted_cards[i].get_val() != sorted_cards[i+1].get_val()-1:
                if cards[0] in sorted_cards[:i] and i >= 2:
                    return i+1
                else:
                    return 0  
        else:
            return 0 if len(sorted_cards) < 2 else len(sorted_cards)
            
    for i in range(len(s),2,-1):
        res = run_score(s[:i])
        if res > 0:
            return res
            
    return 0

def mark_pair(s):
    val = s[0].get_val()
    for i in [4,3,2]:
        if i == len([c for c in s[:i] if c.get_val() == val]):
            return 2*len(list(combinations(s[:i],2)))
    return 0

def handToStr(hand):
    ret = ''
    for i in range(len(hand)-1):
        ret += str(hand[i]) + ', '
    return ret + str(hand[-1])

def getValidIndex(hand):
    n=len(hand)
    while(1):
        try:
            stdin = int(input("Pick a card to discard: %s   "%hand))
            if 0 <= stdin < n:
                return stdin
            else:
                raise ValueError("bad index %d"%stdin)
        except Exception as e:
            print('caught: ',e)
            
def no_valid_move(hand, count):
    return len(hand) == 0 or min(hand).get_val() > (31 - count)