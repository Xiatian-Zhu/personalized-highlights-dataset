'''
 This file shows how to download the dataset videos using python
 For each video in the test set it
  - randomly scores frames
  - computes the average precision and nMSD
'''
__author__ = 'xzhu'

from __future__ import unicode_literals
import youtube_dl
import pdb
import csv

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc']) 

pdf.set_trace()

def download_videos(fname):

	with open(fname, newline='') as csvfile:
		csv_reader = csv.reader(csvfile)
# 		pdb.set_trace()
		
		all_vid_num = 20488 # len(list(csv_reader)) - 1
		vid_idx = 0
		dl_vid_num = 0
		
		next(csv_reader)
		for video_meta in csv_reader:
			yid = video_meta[0]
			print(yid)
	
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