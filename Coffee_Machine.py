# CÓDIGO FUNCIONAL!!


money = 550  # (u$)
water = 400  # (ml)
milk = 540  # (ml)
beans = 120  # (g)
cups = 9
while True:
    def show():
        print('The coffee machine has:')
        print(water, 'of water')
        print(milk, 'of milk')
        print(beans, 'of coffee beans')
        print(cups, 'of disposable cups')
        print('$', money, 'of money')

    def buy():
        global money
        global water
        global milk
        global beans
        global cups
        coffee = min(water // 200, milk // 50, beans // 15, cups // 1)
        choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        if choice == '1' and coffee >= 1:
            money += 4
            water -= 250
            beans -= 16
            cups -= 1
            print('I have enough resources, making you a coffee!')
            print()
        elif choice == '2' and coffee >= 1:
            money += 7
            water -= 350
            milk -= 75
            beans -= 20
            cups -= 1
            print('I have enough resources, making you a coffee!')
            print()
        elif choice == '3' and coffee >= 1:
            money += 6
            water -= 200
            milk -= 100
            beans -= 12
            cups -= 1
            print('I have enough resources, making you a coffee!')
            print()
        elif water < 250:
            print('Sorry, not enough water!')
            print()
        elif milk < 50:
            print('Sorry, not enough milk')
            print()
        elif beans < 15:
            print('Sorry, not enough beans of coffee')
            print()
        elif cups < 1:
            print('Sorry, not enough cups')
        elif choice == 'back':
            pass

    def fill():
        global money
        global water
        global milk
        global beans
        global cups
        choice_w = int(input('Write how many ml of water do you want to add:'))
        choice_m = int(input('Write how many ml of milk do you want to add:'))
        choice_b = int(input('Write how many grams of coffee beans do you want to add:'))
        choice_c = int(input('Write how many disposable cups of coffee do you want to add:'))
        water += choice_w
        milk += choice_m
        beans += choice_b
        cups += choice_c

    def take():
        global money
        print('I gave you $', money)
        money -= money
    action = str(input('Write action (buy, fill, take, remaining, exit):')).strip()
    print()
    if action == 'buy':
        buy()
    if action == 'fill':
        fill()
    if action == 'take':
        take()
    if action == 'remaining':
        show()
        print()
    if action == 'exit':
        exit()



### 74 