import argparse
from video_converter import *

ap = argparse.ArgumentParser()

ap.add_argument("-p", "--path", required=False,
    help="path of one video you want to convert")

ap.add_argument("-d", "--dir", required=False,
    help="directory of all videos you want to convert")

ap.add_argument("-r", "--save_rate", required=False, type=int, default=5,
    help="save every N frames only one image")

ap.add_argument("-s", "--save_extension", required=False, default=".jpg",
    help="the extension of written images '.jpg' '.png' '.tif'")

ap.add_argument("-v", "--extensions", required=False, default="avi,mp4,mov",
    help="the extension of videos you want to convert, comma separated")

args = vars(ap.parse_args())

if args["path"] is None and args["dir"] is None:
    ap.print_help()

if args["dir"] is not None:
    print("processing:" + args["dir"])
    videos_to_frames(videos_dir=args["dir"], extensions=args["extensions"], 
                     save_rate=args["save_rate"], save_extension=args["save_extension"])

if args["path"] is not None:
    print("processing:" + args["path"])
    one_video_to_frames(video_path=args["path"], save_rate=args["save_rate"], save_extension=args["save_extension"])
