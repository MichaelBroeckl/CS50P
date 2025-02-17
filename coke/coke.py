def main():
    money = 0
    while money < 50:
        print(f'Amount due: {50 - money}')
        coin = int(input('Insert coin:'))
        money = calculator(coin, money)

    print(f'Change Owed: {money - 50}')



def calculator(coin, money):
    match coin:
        case 25 | 10 | 5 :
            return money + coin
        case other:
            return money

main()


