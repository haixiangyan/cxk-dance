import argparse

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('command', type=str, default='run')
    parser.add_argument('--width', type=int, default=480)
    parser.add_argument('--height', type=int, default=180)
    parser.add_argument('--speed', type=float, default=0.005)

    return parser.parse_args()


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '

    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


def to_string(image, width, height):
    txt = ""

    for h in range(height):
        for w in range(width):
            txt += get_char(*image.getpixel((w, h)))  # * -> 将 tuple 传入
        txt += '\n'

    return txt
