import sys

def main():
    print(analyze_file())

def analyze_file():
    prompt = sys.argv
    if len(prompt) < 2:
        sys.exit('Too few command-line arguments')
    elif len(prompt) > 2:
        sys.exit('Too many command-line arguments')
    elif not prompt[1].endswith('.py'):
        sys.exit('Not a Python file')
    elif len(prompt) == 2:
        try:
            with open(prompt[1], 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            sys.exit('File does not exist')
        else:
            return count_lines(lines)



def count_lines(lines):
    count = 0
    for line in lines:
        clean_line = line.lstrip()
        if clean_line.startswith('#') or len(clean_line) == 0:
            continue
        else:
            count += 1
    return count

if __name__ == "__main__":
    main()
