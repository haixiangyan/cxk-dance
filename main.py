from lib import get_args
from procedure import prepare, display, is_ready

if __name__ == '__main__':
    args = get_args()

    # 参数
    width = args.width
    height = args.height

    if not is_ready():
        prepare(width, height)

    display()
