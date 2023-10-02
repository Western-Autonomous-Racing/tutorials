# Author: Daniel Xie
# Email: danxie2001@gmail.com
# Purpose: Helper functions for opencv tutorial

import numpy as np
import cv2
import argparse

def show_image(name: str, img, waitkey_ms: int): # helper function to show image
    cv2.imshow(name, img) # shows image
    key = cv2.waitKey(waitkey_ms) # waitkey function controls time to show image. Will close image either once time expires (number passed is in ms) or use presses key
    return key 

def read_image(name: str, turn_image_on : bool):
    img = cv2.imread(name)
    
    if turn_image_on:
        _ = show_image(name, img, 0)
        
def fps_to_ms(frame_rate: float):
    return int(1.0/frame_rate*1000.0) #convert fps to ms (truncated)

def init_videocapture(name: str):
    if name.isdigit():
        return cv2.VideoCapture(int(name)) # either use webcam
    
    return cv2.VideoCapture(name)      # use specified video
    
        
def play_video(name: str, frame_rate: float):
    """
    name: path/name of video to capture
    frame_rate: fps of video playback
    """
    
    waitkey_ms = fps_to_ms(frame_rate)
    
    cap = init_videocapture(name)
        
    if not cap.isOpened(): # throws error if capture object isn't open
        print("Error opening video file")
                
    while (cap.isOpened()): # while capture object is open
        
        ret, frame = cap.read() # ret: if frame is valid, frame: actual image array
        if ret:
            key = show_image(name, frame, waitkey_ms) # show frame
            if key == ord('q'): #quit when 'q' is pressed.
                break
        else:
            break

    cap.release()

def write_frame(video_writer, img):
    video_writer.write(img)

def init_videowriter(cap, save_path: str, fps: float, codec='mp4v'):
    fourcc = cv2.VideoWriter_fourcc(*codec)

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    return cv2.VideoWriter(save_path, fourcc, fps, (frame_width, frame_height))
        
def write_video(dev_name: str, save_path: str, fps: float, display_image=False):
    """
    dev_name: path/name of video to capture 
    save_path: where to save video
    fps: frames per second
    """

    waitkey_ms = fps_to_ms(fps)
    
    cap = init_videocapture(dev_name)

    if not cap.isOpened(): # throws error if capture object isn't open
        print("Error opening video file")

    videowriter = init_videowriter(cap, save_path, fps)

    while (cap.isOpened()): # while capture object is open
        ret, frame = cap.read() # ret: if frame is valid, frame: actual image array
        if ret:
            
            write_frame(videowriter, frame)

            if display_image:
                key = show_image(dev_name, frame, waitkey_ms)
            else:
                key = cv2.waitKey(waitkey_ms)

            if key == ord('s'):
                break
        else:
            break
    
    videowriter.release()
    cap.release()

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # Add an argument
    parser.add_argument('-f', '--function', type=str, help='The function to run')
    parser.add_argument('-p', '--path', type=str, help='Path to file')
    parser.add_argument('-s', '--save_path', type=str, default='../.media/output.mp4', help='Save path of video file.')
    parser.add_argument('-d', '--display_image', type=bool, default=False, help='To display or not display the image')
    parser.add_argument('-r', '--frame_rate', type=float, default=1000.0, help='Set playback framerate')

    # Parse the arguments
    args = parser.parse_args()
    
    if args.function == 'read_image':
        read_image(args.path, args.display_image)
    elif args.function == 'play_video':
        play_video(args.path, args.frame_rate)
    elif args.function == 'write_video':
        write_video(args.path, args.save_path, args.frame_rate, args.display_image)

        
    cv2.destroyAllWindows() #closes all cv2 windows open