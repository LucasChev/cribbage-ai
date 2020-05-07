class card():
    def __init__(self, id):
        if not 0 <= id <= 51:
            raise ValueError("id should be between 0 and 51, recieved %d",id)
        self.id = id
    
    def get_suit(self):
        return int(self.id/13)
    
    def get_val(self):
        return min((self.id%13+1),10)
    
    def get_id(self):
        return self.id%13
        
    def __add__(self,o):
        return self.get_val() + o.get_val()
    
    def __lt__(self,o):
        return self.get_val() < o.get_val()
    
    # bad solution - here so we can use 'if card in cards'
    def __eq__(self,o):
        return self.get_id() == o.get_id()
    
    def __str__(self):
        _id = self.get_id()
        if _id == 10:
            _id = 'J'
        elif _id == 11:
            _id = 'Q'
        elif _id == 12:
            _id = 'K'
        else:
            _id += 1
        suit = self.get_suit()
        if suit == 0:
            suit = "\u2660"
        elif suit == 1:
            suit = "\u2665"
        elif suit == 2:
            suit = "\u2666"
        elif suit == 3:
            suit = "\u2663"
        else:
            raise ValueError("Bad suit id")

        return "%s%s"%(suit,_id)
    
    def __repr__(self):
        return self.__str__()