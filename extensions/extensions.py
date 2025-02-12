def main():
    filename = input(
        'What\'s the name of your file?\n'
    ).strip().lower().split('.')
    suffix = f'.{filename[-1]}'

    evaluate_suffix(suffix)

def evaluate_suffix(suffix):
    match suffix:
        case '.gif'|'.jpeg'|'.png':
            print(f'image/{suffix.lstrip('.')}')
        case '.pdf'|'.zip':
            print(f'application/{suffix.lstrip('.')}')
        case '.jpg':
            print('image/jpeg')
        case '.txt':
            print('text/plain')
        case other:
            print('application/octet-stream')


main()
