#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import codecs
import os
from konlpy.tag import Kkma
from gensim.models import Word2Vec

path = './text'
path_list = []

# Get file name for train
def get_file():
	global path_list, path

	for directory in os.listdir(path) :
		for file_name in os.listdir(path + '/'+ directory) :
			path_list.append(path+'/'+directory+'/'+file_name)

if __name__ == '__main__' :

	print('start_process')
	kkma = Kkma()
	
	text = []
	error_line = []

	# get file name
	get_file()

	for file_path in path_list :
		# read by utf-8, but it doesn`t why?
		file = codecs.open(file_path, 'r', 'utf-8')

		while True :
			# only read with '\n' becuase encode error check
			line = file.readline()

			# Check read all
			if not line : 
				print(file_path +' is end')
				break

			# if it is sign or just blank = delete
			if 'doc' in line or line == '\n' :
				continue
			else :
				try:
					sentences = kkma.sentences(line)

				## if only made by space, it cause error, so delete it
				except Exception as e:
					print(e)
					print('error emit')
					## error line check, only have [' ']
					error_line.append(line)
					continue	
				
				#accumulate corpus data in text, i dont know retrain it !!!!!!!!
				for sentence in sentences :
					text.append(kkma.morphs(sentence))

		print(error_line)

		print('text_morpus_end')
		print('start trainning')

		# data embedding _ slow
		embedding_model = Word2Vec(text, size = 300, window=2,
			 min_count = 50, workers = 4, iter=100, sg=1)

		# model save when each file end
		embedding_model.save(file_path+'w2v_model')