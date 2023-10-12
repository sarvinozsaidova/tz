from beverage import Beverage

class VendingMachine:
    def __init__(self):
        self.beverages = {}
        self.cards = {}

    def addBeverage(self, beverage):
        self.beverages[beverage.getName()] = beverage

    def getPrice(self, beverageName):
        if beverageName not in self.beverages:
            return -1.0
        return self.beverages[beverageName].getPrice()
    
    def rechargeCard(self, card_id, credit):
        if card_id in self.cards:
            self.cards[card_id] += credit
        else:
            self.cards[card_id] = credit

    def getCredit(self, card_id):
        if card_id in self.cards:
            return self.cards[card_id]
        else:
            return -1.0