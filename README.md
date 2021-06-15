# cxk-dance

蔡徐坤跳舞字符画

## 怎么用

```bash
# 添加依赖
pip3 install Pillow

# 将原视频分帧
ffmpeg -i res/cxk-video.mov res/image_frames/%d.jpg

# 创建文件夹
mkdir ./res/image_frames
mkdir ./res/txt_frames

# 将帧转成 txt
python3 ./main.py compile

# 开始跳w舞
python3 ./main.py run
```

## 参数

```bash
./main.py run --speed 0.02 # 控制速度，单位为 seconds，这里数值为默认值

./main.py run --width 240 --height 100 # 控制宽高，这里数值为默认值
```
