# Convert one video or batch of videos to frames

### Installation
you should install:
- pip install opencv-python
- pip install numpy
- pip install ffmpeg-python

### convert one video
python main.py -p "path to video" -r 5 -s ".png"

### convert multiple videos in directory
python main.py -d "dir/sub-dir of videos" -r 10 -s ".png" -v "mp4,avi,mov"

### Arguments:
-   -h, --help            show this help message and exit
-   -p PATH, --path PATH  path of one video you want to convert
-   -d DIR, --dir DIR     directory of all videos you want to convert
-   -r SAVE_RATE, --save_rate SAVE_RATE save every N frames only one image
-   -s SAVE_EXTENSION, --save_extension SAVE_EXTENSION the extension of written images '.jpg' '.png' '.tif'
-   -v EXTENSIONS, --extensions EXTENSIONS the extension of videos you want to convert, comma separated 'mp4,avi,mov'