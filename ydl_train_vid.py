'''
 This file shows how to download the dataset videos using python
 For each video in the test set it
  - randomly scores frames
  - computes the average precision and nMSD
'''
__author__ = 'xzhu'

import youtube_dl
import pdb
import csv
import os.path
from os import path
import time


def download_videos(fname):

	ydl_opts = {
    'outtmpl': './train/%(id)s.%(ext)s'
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	
		with open(fname, newline='') as csvfile:
			csv_reader = csv.reader(csvfile)
		
			all_vid_num = 201527 # len(list(csv_reader)) - 1
			vid_idx = 0
			dl_vid_num = 0
		
			next(csv_reader)
			for video_meta in csv_reader:
				yid = video_meta[0]
				print(yid)
	
				vid_idx += 1
		
				if path.exists('./train/'+yid+'.mp4'):
					print('\n\n {}-th (all {}) video !!! Exist !!! \n\n'.format(vid_idx, all_vid_num))
					continue
					
				# To download a video with ID yid
				vid_link = 'https://www.youtube.com/watch?v=' + yid
				try:
					ydl.download([vid_link])
					dl_vid_num += 1
					print('\n\n {}-th (all {}/{}) video ### downloaded ### \n\n'.format(vid_idx, dl_vid_num, all_vid_num))
				except:
					print('\n\n {}-th (all {}/{}) video --- unavailable --- \n\n'.format(vid_idx, dl_vid_num, all_vid_num))
			
				time.sleep(2)
				
if __name__=='__main__':
    download_videos('training.csv')