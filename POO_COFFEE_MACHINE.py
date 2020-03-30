# CÓDIGO ORIENTADO À OBJETOS
class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.coffee_ = []
        self.ok = False
        self.active = True

    def show(self):
        print(f'The coffee machine has:')
        print(self.water, 'of water')
        print(self.milk, 'of milk')
        print(self.beans, 'of beans')
        print(self.cups, 'of cups')
        print(f'${self.money} of money')
        print()

    def coffee(self):
        if self.water < self.coffee_[0]:
            print('Sorry, not enough water!')
            self.ok = False
        elif self.milk < self.coffee_[1]:
            print('Sorry, not enough milk')
            self.ok = False
        elif self.beans < self.coffee_[2]:
            print('Sorry, not enough beans of coffee')
            self.ok = False
        elif self.cups < self.coffee_[3]:
            print('Sorry, not enough cups')
            self.ok = False
        else:
            print('I have enough resources, making you a coffee!')
            self.ok = True
        print()

    def espresso(self):
        self.coffee_ = [250, 0, 16, 1]
        self.coffee()
        if self.ok:
            self.money += 4
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
        else:
            pass
    
    def latte(self):
        self.coffee_ = [350, 75, 20, 1]
        self.coffee()
        if self.ok:
            self.money += 7
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.cups -= 1

    def cappuccino(self):
        self.coffee_ = [200, 100, 12, 1]
        self.coffee()
        if self.ok:
            self.money += 6
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.cups -= 1

    def buy(self):
        choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino')
        if choice == '1':
            self.espresso()  # ESPRESSO
        elif choice == '2':
            self.latte()  # LATTE
        elif choice == '3':
            self.cappuccino()  # CAPPUCCINO
        elif choice == 'back':
            pass

    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add: '))
        self.milk += int(input('Write how many ml of milk do you want to add: '))
        self.beans += int(input('Write how many grams of coffee beans do you want to add: '))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add: '))
        print()

    def take(self):
        print(f'I gave you ${self.money}')
        self.money -= self.money

    def action(self):
        while self.active:
            action_ = str(input('Write action (buy, fill, take, remaining, exit) '))
            print()
            if action_ == 'buy':
                self.buy()
            elif action_ == 'fill':
                self.fill()
            elif action_ == 'take':
                self.take()
            elif action_ == 'remaining':
                self.show()
            elif action_ == 'exit':
                self.active = False


machine = CoffeeMachine(400, 540, 120, 9, 550)
machine.action()
