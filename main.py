from vendingMachine import VendingMachine
from beverage import Beverage

vendingMachine = VendingMachine()
vendingMachine.addBeverage(Beverage("Coca Cola", 3200))
vendingMachine.addBeverage(Beverage("Suv", 1000))
vendingMachine.addBeverage(Beverage("Pepsi", 2500))

cocaColaPrice = vendingMachine.getPrice("Coca Cola")
print(cocaColaPrice)

vendingMachine.addBeverage(Beverage("Limanat", 2000))
limanatPrice = vendingMachine.getPrice("Limanat")
print(limanatPrice)
vendingMachine.rechargeCard(12, 5000)

vendingMachine.rechargeCard(34, 10000)

credit = vendingMachine.getCredit(12)
print(f"12-karta: {credit}")

credit = vendingMachine.getCredit(99)
print(f"99-karta: {credit}")

credit = vendingMachine.getCredit(50)
print(f"50-karta: {credit}")



vendingMachine.refillColumn(1, "Coca Cola", 1)
vendingMachine.refillColumn(2, "Water", 10)
vendingMachine.refillColumn(3, "Pepsi", 15)
vendingMachine.refillColumn(4, "Water", 20)

available_cans = vendingMachine.availableCans()
print("Available cans:", available_cans)