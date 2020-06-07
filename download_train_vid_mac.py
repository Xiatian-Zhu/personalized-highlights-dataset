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


def download_videos(fname):

	video_dir = '/Volumes/Untitled/'
	ydl_opts = {
    'outtmpl': video_dir + '%(id)s.%(ext)s'
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	
		with open(fname, newline='') as csvfile:
			
			# Go to a break point
			csv_reader = csv.reader(csvfile)
		
			# Skip header
			next(csv_reader)
			# Jump to a break point
			break_point = 51720
			for i in range(break_point):
				next(csv_reader)
		
			all_vid_num = 201527-break_point # len(list(csv_reader)) - 1
			vid_idx = 0
			dl_vid_num = 0
		
			for video_meta in csv_reader:
				
				yid = video_meta[0]
				print(yid)
	
				vid_idx += 1
		
				if path.exists(video_dir+yid+'.mp4'):
					dl_vid_num += 1
					print('\n\n {}-th (all {}) video !!! Exist !!! \n\n'.format(vid_idx, all_vid_num))
					continue
					
				# To download a video with ID yid
				vid_link = 'https://www.youtube.com/watch?v=' + yid
				try:
					ydl.download([vid_link])
					if path.exists(video_dir+yid+'.mp4'):
						dl_count += 1
						dl_vid_num += 1
						print('\n\n {}-th (all {}/{}) video ### downloaded ### \n\n'.format(vid_idx, dl_vid_num, all_vid_num))
						time.sleep(random.randint(5,7))
					else:
						print('\n\n {}-th (all {}/{}) video *** failed *** \n\n'.format(vid_idx, dl_vid_num, all_vid_num))
						time.sleep(random.randint(3,5))
						
				except:
					print('\n\n {}-th (all {}/{}) video --- unavailable --- \n\n'.format(vid_idx, dl_vid_num, all_vid_num))
					time.sleep(random.randint(3,5))
					
				
if __name__=='__main__':
    download_videos('training.csv')