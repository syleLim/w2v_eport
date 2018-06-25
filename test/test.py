#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import copy
from konlpy.tag import Kkma
from konlpy.tag import Komoran
from konlpy.utils import pprint
from gensim.models import Word2Vec

file_1 = 'wiki_00'
file_2 = 'wiki_00.txt'
file_3 = 'wiki_00_1.txt'
kkma = Kkma()
komoran = Komoran()

f = codecs.open(file_1, 'r', 'utf-8')

text = []
error_line = []
sentext = []

while True :
	line = f.readline()

	if not line : break

	line = line.strip('\n')
	

	if 'doc' in line or line == '\n' :
		continue
	else :
		try:
			sentences = kkma.sentences(line)
		except Exception as e:
			error_line.append(line)
			continue	
		
		for sentence in sentences :
			sentext.append(sentence)
			text.append(kkma.morphs(sentence))

f = open('text.txt', 'w')
for x in text :
	f.write(str(x)+'\n')
f.close()

f_2 = open('sentext.txt', 'w')
for x in sentext :
	f_2.write(str(x) +'\n')
f_2.close()

embedding_model = Word2Vec(text, size = 300, window=2,
		 min_count = 50, workers = 4, iter=100, sg=1)

embedding_model.save('w2v_model')
