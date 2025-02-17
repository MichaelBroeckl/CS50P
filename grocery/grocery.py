grocery_dict = {}


def main():
    while True:
        try:
            item = input('').strip().upper()
        except EOFError:
            print_grocery_list()
            break
        else:
            update_grocery_dict(item)


def update_grocery_dict(item):
    if item in grocery_dict:
        grocery_dict[item] += 1
    else:
        grocery_dict[item] = 1
    return grocery_dict


def print_grocery_list():
    for key in sorted(grocery_dict):
        print(f'{grocery_dict[key]} {key}')


main()
