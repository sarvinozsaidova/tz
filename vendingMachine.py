from beverage import Beverage

class VendingMachine:
    def __init__(self):
        self.beverages = {}
        self.cards = {}
        self.column = {}

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
        
    # def refillColumn(self, column_number, drink_name, number_of_cans):
    #     self.vending_machine.columns[column_number] = {"ichimlik nomi": drink_name, "soni": number_of_cans}

    # def availableCans(self, drink_name):
    #     for column in self.vending_machine.columns:
    #         if column["ichimlik nomi"] == drink_name:
    #             return column["soni"]

    #     return 0
    def refillColumn(self, column_number, drink_name, number_of_cans):
        if column_number in self.column:
            self.column[column_number][(drink_name,)] = number_of_cans
        else:
            self.column[column_number] = {(drink_name,): number_of_cans}

    def availableCans(self):
        cans_count = 0
        for column in self.column.values():
            for drink_cans in column():
                for cans in drink_cans():
                    cans_count += cans
        return cans_count