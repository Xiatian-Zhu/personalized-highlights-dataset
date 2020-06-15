'''
 To count the training video numbers of HPDD
'''
__author__ = 'xzhu'

import pdb
import csv


def count_videos(fname):

	with open(fname, newline='') as csvfile:
		
		csv_reader = csv.reader(csvfile)
		
		# Skip header
		next(csv_reader)
		
		vid_dict = {}
		for video_meta in csv_reader:
			yid = video_meta[0]
			vid_dict[yid] = 1
				
		print(fname + ' video number:{}'.format(len(vid_dict)))


def video_ID_list(fname):
	with open(fname, newline='') as csvfile:
		
		csv_reader = csv.reader(csvfile)
		
		# Skip header
		next(csv_reader)
		
		vid_dict = {}
		for video_meta in csv_reader:
			yid = video_meta[0]
			vid_dict[yid] = 1

	vid_list = list(vid_dict.keys())

	return vid_list


if __name__=='__main__':
	count_videos('training.csv')
	count_videos('testing.csv')
    