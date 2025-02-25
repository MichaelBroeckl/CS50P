import sys
import csv


def main():

    try:
        with open(evaluate_command()[0], 'r') as f, open(evaluate_command()[1], 'w') as nf:
            reader = list(csv.reader(f))
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(nf, fieldnames=fieldnames)
            writer.writeheader()
            for line in reader[1:]:
                first = line[0].split(',')[1].strip()
                last = line[0].split(',')[0].strip()
                house = line[1].strip()
                line = writer.writerow({'first': first, 'last': last, 'house': house})
    except FileNotFoundError:
        sys.exit('File does not exist')


def evaluate_command():
    arguments = sys.argv
    if len(arguments) < 3:
        sys.exit('Too little arguments')
    elif len(arguments) > 3:
        sys.exit('Too many arguments')
    elif arguments[1].strip().endswith('.csv') and arguments[2].strip().endswith('.csv'):
        return (arguments[1].strip(), arguments[2].strip())
    else:
        sys.exit('Not a CSV file')


if __name__ == "__main__":
    main()
