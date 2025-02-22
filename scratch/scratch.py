full_names = [
    "Alice Johnson",
    "Bob Smith",
    "Charlie Brown",
    "David Williams",
    "Emma Jones",
    "Frank Miller",
    "Grace Davis",
    "Henry Wilson",
    "Isabella Moore",
    "Jack Taylor",
    "Kelly Anderson",
    "Liam Thomas",
    "Mia White",
    "Noah Harris",
    "Olivia Martin",
    "Paul Thompson",
    "Quinn Garcia",
    "Ryan Martinez",
    "Sophia Clark",
    "Tyler Rodriguez"
]


def main():
    person_dict_list = [person_dict(full_name.split()[0], full_name.split()[1]) for full_name in full_names]
    print(person_dict_list)

def person_dict(first_name, last_name):
    person = {'first' : first_name, 'last' : last_name}
    return person

if __name__ == "__main__":
    main()