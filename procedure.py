import glob
import os
from functools import cmp_to_key
from os import listdir
from os.path import isfile, join
from time import sleep

from PIL import Image

from lib import to_string

image_frames_dir = 'res/image_frames'
txt_frames_dir = 'res/txt_frames'


def is_ready():
    return len(listdir(txt_frames_dir)) != 0


def prepare(width, height):
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


def display():
    def compare_file_name(file_name1, file_name2):
        index1 = int(file_name1.split('.')[0])
        index2 = int(file_name2.split('.')[0])

        return index1 < index2

    for file_name in sorted(listdir(txt_frames_dir), key=cmp_to_key(compare_file_name)):
        txt_path = join(txt_frames_dir, file_name)

        os.system('cat ' + txt_path)
        sleep(0.1)


def clear():
    files = glob.glob(join(txt_frames_dir, '*'))
    for f in files:
        os.remove(f)
