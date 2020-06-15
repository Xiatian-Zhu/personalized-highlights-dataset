'''
 This file shows how to download the dataset videos using python
 For each video in the test set it
  - randomly scores frames
  - computes the average precision and nMSD
'''
__author__ = 'xzhu'

import youtube_dl
import youtube_dl.utils
import pdb
import csv
import os.path
from os import path
import time
import random
from utils.count_video_number import video_ID_list


def download_videos(fname):

    vid_ID_list = video_ID_list('training.csv')
    # Total: 110611
    # Processed
    vid_ID_list = vid_ID_list[14180:]
    # Reverse the order
    vid_ID_list.reverse()

    # Stats
    all_vid_num = len(vid_ID_list)
    vid_idx = 0

    downloaded_num = 0

    ydl_opts = {
    'outtmpl': '/home/nfs/datasets/PHDD/train/%(id)s.%(ext)s'
	}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    
        for yid in vid_ID_list:

            vid_idx += 1
    
            # Skip what existing
            if path.exists('/home/nfs/datasets/PHDD/train/'+yid+'.mp4'):
                print('\n\n {}-th (all {}) !!! in place !!! \n\n'.format(vid_idx, all_vid_num))
                continue
                
            # To download a video with ID yid
            vid_link = 'https://www.youtube.com/watch?v=' + yid
            try:
                ydl.download([vid_link])
                
                # Double check if the video is obtained (errors: unavaiable, account terminated, private videos)
                if path.exists('/home/nfs/datasets/PHDD/train/'+yid+'.mp4'):
                    downloaded_num += 1
                    print('\n {}-th (all {}) ### downloaded ### (done: {}) \n'.format(vid_idx, all_vid_num, downloaded_num))
                    
                    # Stop strategy
                    if downloaded_num > 1 and downloaded_num % 50 == 0:
                        time.sleep(random.randint(300,600))
                    else:
                        time.sleep(random.randint(15,17))
                else:
                    print('\n {}-th (all {}) *** failed *** \n'.format(vid_idx, all_vid_num))
                    time.sleep(random.randint(3,5))
                    
            except:
                print('\n {}-th (all {}) --- unavailable --- \n'.format(vid_idx, all_vid_num))
                time.sleep(random.randint(5, 8))
					
				
if __name__=='__main__':
    download_videos('training.csv')