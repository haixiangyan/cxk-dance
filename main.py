from lib import get_args
from procedure import prepare, display, is_ready

if __name__ == '__main__':
    args = get_args()

    # 参数
    command = args.command
    width = args.width
    height = args.height

    if command == 'compile' or not is_ready():
        prepare(width, height)

    display()
