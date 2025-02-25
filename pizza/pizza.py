import sys
import csv
from tabulate import tabulate

def main():
    try:
        with open(evaluate_command(), 'r') as f:
            reader = csv.reader(f)
            menue_list = [line for line in reader]
    except FileNotFoundError:
        sys.exit('File does not exist')
    else:
        print(tabulate(menue_list[1:], menue_list[0], tablefmt="grid"))


def evaluate_command():
    arguments = sys.argv
    if len(arguments) < 2:
        sys.exit('Too little arguments')
    elif len(arguments) > 2:
        sys.exit('Too many arguments')
    elif arguments[1].strip().endswith('.csv'):
        return arguments[1].strip()
    else:
        sys.exit('Not a CSV file')


if __name__ == "__main__":
    main()
