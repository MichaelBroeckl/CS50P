MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    order = []
    while True:
        try:
            item = input('Item: ').title().strip()
        except EOFError:
            print('\nThank you for your Order :)')
            break
        else:
            try:
                order.append(float(MENU[item]))
            except KeyError:
                continue
            except ValueError:
                continue
            else:
                print(f'Total: ${sum(order):.2f}')

main()
