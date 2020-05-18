'''
 This file shows how to download the dataset videos using python
 For each video in the test set it
  - randomly scores frames
  - computes the average precision and nMSD
'''
__author__ = 'xzhu'
import pdb
import re
from pytube import YouTube
import csv
 

def download_videos(fname):

	with open(fname, newline='') as csvfile:
		csv_reader = csv.reader(csvfile)
		next(csv_reader)
		pdb.set_trace()
		
		all_vid_num = len(csv_reader)
		vid_idx = 0
		dl_vid_num = 0
		
		for video_meta in csv_reader:
			print(video_meta[0])
	
			vid_idx += 1
		
			# To download a video with ID yid
			vid_link = 'https://www.youtube.com/watch?v=' + yid
			# print(vid_link)
			try:
				YouTube(vid_link).streams[0].download()
				dl_vid_num += 1
				print('\n\n {}-th (all {}/{}) video ### downloaded ### \n\n'.format(vid_idx, dl_vid_num, all_vid_num))
			except:
				print('\n\n {}-th (all {}/{}) video *** unavailable *** \n\n'.format(vid_idx, dl_vid_num, all_vid_num))
			
if __name__=='__main__':
    download_videos('testing.csv')