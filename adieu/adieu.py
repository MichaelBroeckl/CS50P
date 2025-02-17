import inflect

p = inflect.engine()


def main():
    name_list = []
    while True:
        try:
            user_input = input('Add one name: ').title()
            name_list.append(user_input)
        except EOFError:
            break

    print(f'Adieu, adieu, to {p.join(name_list)}')

        #     if len(name_list) == 1:
        #         print(f'Adieu, adieu, to {name_list[0]}')
        #         break
        #     elif len(name_list) == 2:
        #         print(f'Adieu, adieu, to {name_list[0]} and {name_list[1]}')
        #         break
        #     else:
        #         names = ''
        #         for name in name_list[:-2]:
        #             names = names + name + ', '
        #         print(f'Adieu, adieu, to {names}{name_list[-2]} and '
        #               f'{name_list[-1]}')
        #         break
        # else:
        #     name_list.append(user_input)

if __name__ == "__main__":
    main()
