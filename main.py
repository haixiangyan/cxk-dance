from PIL import Image
import argparse


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('file')
    parser.add_argument('-o', '--output')
    parser.add_argument('--width', type=int, default=80)
    parser.add_argument('--height', type=int, default=80)

    return parser.parse_args()


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '

    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


def to_string(image):
    txt = ""

    for h in range(height):
        for w in range(width):
            txt += get_char(*image.getpixel((w, h)))  # * -> 将 tuple 传入
        txt += '\n'

    print(txt)
    return txt


ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

if __name__ == '__main__':
    args = get_args()

    file = args.file
    width = args.width
    height = args.height
    output = args.output

    image = Image.open(file)
    image = image.resize((width, height), Image.NEAREST)  # NEAREST 低质量图

    txt = to_string(image)

    if output:
        with open(output, 'w') as f:
            f.write(txt)
    else:
        with open('output.txt', 'w') as f:
            f.write(txt)
