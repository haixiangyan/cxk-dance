from PIL import Image
from os import listdir
from os.path import isfile, join
from lib import to_string


def prepare(width, height):
    image_frames_dir = 'res/image_frames'
    txt_frames_dir = 'res/txt_frames'

    for file_name in listdir(image_frames_dir):
        print("正在处理 " + file_name)

        image_path = join(image_frames_dir, file_name)
        txt_path = join(txt_frames_dir, file_name.split('.')[0] + '.txt')

        if not isfile(image_path):
            continue

        image = Image.open(image_path)
        image = image.resize((width, height), Image.NEAREST)  # NEAREST 低质量图

        txt = to_string(image, width, height)

        with open(txt_path, 'w') as txt_file:
            txt_file.write(txt)


def show_video():
    pass
