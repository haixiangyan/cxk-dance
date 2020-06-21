#!/usr/local/bin/python3
from lib import get_args
from procedure import prepare, display, is_ready, clear

if __name__ == '__main__':
    args = get_args()

    # 参数
    command = args.command
    width = args.width
    height = args.height
    speed = args.speed

    if command == 'clear':
        clear()
    if command == 'compile':
        prepare(width, height)
    if command == 'run':
        if not is_ready():
            print('运行 python3 main.py compile 来编译')
        else:
            display(speed)
