import numpy as np
import cv2
import os

def one_video_to_frames(video_path, save_rate=5, save_extension=".jpg"):
    '''
    convert one video to frames
    @video_path path to the video you want to convert
    @save_rate save every N frames one image
    @save_extension the extension of written image like '.jpg' or '.png'
    
    output a folder for the video with same name and location of the video
    '''
    save_dir = os.path.splitext(video_path)[0] + "/"
    print(save_dir)
    
    cap = cv2.VideoCapture(video_path)
    success, frame = cap.read()
    
    frames_counter = 0
    img_counter = 0
    
    while success:
        success, frame = cap.read()
        if success:
            frames_counter+=1
            if (frames_counter % save_rate != 0):
                continue
            
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
                
            img_path = save_dir + str(img_counter) + save_extension
            img_counter+=1
            
            cv2.imwrite(img_path, frame)
    cap.release()

def videos_to_frames(videos_dir, extensions="mp4,avi,mov", save_rate=5, save_extension=".jpg"):
    '''
    convert multiple videos to frames,
    @parent_dir root where all videos exist (also accept sub-directories)
    @extensions of videos should be written with comma between them like avi,mp4,mov
    @save_rate save every N frames one image
    @save_extension the extension of written image like '.jpg' or '.png'
    
    output a folder foreach video with same name and location of each video
    '''
    all_files = [os.path.join(path, name) for path, subdirs, files in os.walk(videos_dir) for name in files]
    exts = extensions.split(',')
    video_files = []
    for file in all_files:
        for ext in exts:
            if file.lower().endswith(ext):
                video_files.append(file)
    
    for video_path in video_files:
        one_video_to_frames(video_path, save_rate, save_extension)