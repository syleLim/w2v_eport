from konlpy.tag import Kkma
from gensim.models import Word2Vec
import os
import sys

# get model file name
path ='./'
file_list = os.listdir(path)
for file in file_list :
	if 'model' in file :
		file_name = file
try:
	model = Word2Vec.load(file_name)
	print('load file is ' + file_name)
except Exception as e:
	print(e)
	print('May be file not exist, please check')
	sys.exit(1)

while True :
	word = input('단어를 입력해 주세요 : ')

	print('simillar word :')
	print(model.most_similar(word))

	word_plus = input('더할 단어를 입력해 주세요. 더하지 않으면 1을 입력해 주세요. : ')

	if word_plus is not '1' :
		print('word + program')
		print(word + ' + ' + word_plus + ' :')
		print(model.most_similar(positive=[word, word_plus]))

	word_minus = input('뺄 단어를 입력해 주세요. 빼지 않으면 1을 입력해 주세요. : ')	

	if word_minus is not '1' :
		print('word - program')
		if word_plus is not '1' :
			print(word +' + '+ word_plus +' - '+ word_minus + ' :')
			print(model.most_similar(positive=[word, word_plus], negative=[word_minus]))	
		else :
			print(word +' - '+ word_minus + ' :')
			print(model.most_similar(positive=[word], negative=[word_minus]))

	flag = input('sequence end, again?(y/n) : ')

	if flag  == 'n':
		break
