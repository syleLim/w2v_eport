#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import codecs
import os
from konlpy.tag import Kkma
from gensim.models import Word2Vec

path = './text'
path_list = []

def get_file():
	global path_list, path

	for directory in os.listdir(path) :
		for file_name in os.listdir(path + '/'+ directory) :
			path_list.append(path+'/'+directory+'/'+file_name)