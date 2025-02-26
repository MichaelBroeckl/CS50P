import sys
from PIL import Image, ImageOps




def main():
    evaluate_arguments()
    try:
        image = Image.open(sys.argv[1], 'r')
    except FileNotFoundError:
        sys.exit('input does not exist')

    shirtfile = Image.open('shirt.png')
    size = shirtfile.size
    image_fitted = ImageOps.fit(image, size)
    image_fitted.paste(shirtfile, shirtfile)
    image_fitted.save(sys.argv[2])
    image.close()
    shirtfile.close()


def evaluate_arguments():
    before = sys.argv[1].strip().lower()
    after = sys.argv[2].strip().lower()
    suffixes = ('.jpg', '.jpeg', '.png')
    if len(sys.argv) < 3:
        sys.exit('too little arguments')
    elif len(sys.argv) > 3:
        sys.exit('too many arguments')
    elif not before.endswith(suffixes):
        sys.exit('invalid input')
    elif not after.endswith(suffixes):
        sys.exit('invalid output')
    elif before.split('.')[1] != after.split('.')[1]:
        sys.exit('input and output have different extensions')


if __name__ == '__main__':
    main()
