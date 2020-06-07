'''
 To count the training video numbers of HPDD
'''
__author__ = 'xzhu'

import pdb
import csv
import os
import glob


def count_null_video(part):

	video_path = '/home/nfs/datasets/PHDD/' + part
	
	videos = glob.glob(video_path+'*.mp4'):
	null_video_num = 0
	for v in videos:
		# Check the size of a video
		v_stat = os.stat(v)
		if v_stat.st_size < 1000:
			null_video_num += 1
				
	print('null' + part + ' video number:{}'.format(null_video_num))
				
if __name__=='__main__':
    count_null_video('train')
    count_null_video('test')
    