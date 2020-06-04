'''
 This file shows how to download the dataset videos using python
 For each video in the test set it
  - randomly scores frames
  - computes the average precision and nMSD
'''
__author__ = 'xzhu'

from os import listdir
from os.path import isfile, join
import glob
import pdb

import pickle


def video_list(dirname):

	vfiles = glob.glob(dirname+'*.mp4')
# 	cfiles = glob.glob('./*.csv')
	
	pdb.set_trace()
	
	for idx in range(len(vfiles)):
		vfiles[idx] = vfiles[idx][2:-4]
	
	pdb.set_trace()
	with open('train_videos_done', 'wb') as fp:
		pickle.dump(vfiles, fp)
	
	print('Totally {} mp4 videos found'.format(len(vfiles)))
# 	with open ('train_videos_done', 'rb') as fp:
# 		vlist = pickle.load(fp)
				
if __name__=='__main__':
    video_list('./train/')