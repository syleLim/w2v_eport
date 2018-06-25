#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import copy

from konlpy.tag import Kkma
from gensim.models import Word2Vec

file_1 = 'wiki_00'
file_2 = 'wiki_00.txt'
file_3 = 'wiki_00_1.txt'

f = codecs.open(file_1, 'r', 'utf-8')

text = ''

while True :
	line = f.readline()

	if not line : break
	
	if 'doc' in line or line == '\n' :
		continue
	else :
		text += line

print(text)