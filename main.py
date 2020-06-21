from lib import get_args
from procedure import prepare

if __name__ == '__main__':
    args = get_args()

    # 参数
    width = args.width
    height = args.height

    prepare(width, height)
