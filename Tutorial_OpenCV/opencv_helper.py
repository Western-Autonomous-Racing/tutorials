# Author: Daniel Xie
# Email: danxie2001@gmail.com
# Purpose: Helper functions for opencv tutorial

import numpy as np
import cv2
import argparse

def show_image(name: str, img): # helper function to show image
    cv2.imshow(name, img) # shows image
    cv2.waitKey(0) # waitkey function controls time to show image. Will close image either once time expires (number passed is in ms) or use presses key
    
def read_image(name: str, turn_image_on : bool):
    img = cv2.imread(name)
    
    if turn_image_on:
        show_image(name, img)
        
def fps_to_ms(frame_rate: float):
    return int(1.0/frame_rate*1000.0) #convert fps to ms (truncated)

def read_video(name: str):
    if name.isdigit():
        return cv2.VideoCapture(int(name)) # either use webcam
    
    return cv2.VideoCapture(name)      # use specified video
    
        
def play_video(name: str, frame_rate: float):
    
    waitkey_ms = fps_to_ms(frame_rate)
    
    cap = read_video(name)
        
    if not cap.isOpened(): # throws error if capture object isn't open
        print("Error opening video file")
                
    while (cap.isOpened()): # while capture object is open
        
        ret, frame = cap.read() # ret: if frame is valid, frame: actual image array
        if ret == True:
            cv2.imshow(name, frame) # show frame
            if cv2.waitKey(waitkey_ms) == ord('q'): #quit when 'q' is pressed.
                break
        else:
            break
        
def write_video(name:)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # Add an argument
    parser.add_argument('-f', '--function', type=str, help='The function to run')
    parser.add_argument('-p', '--path', type=str, help='Path to file')
    parser.add_argument('-s', '--show_image', type=bool, default=False, help='To show or not show the image')
    parser.add_argument('-r', '--frame_rate', type=float, default=1000.0, help='Set playback framerate')

    # Parse the arguments
    args = parser.parse_args()
    
    if args.function == 'read_image':
        read_image(args.path, args.show_image)
    if args.function == 'play_video':
        play_video(args.path, args.frame_rate)

        
    cv2.destroyAllWindows() #closes all cv2 windows open