import numpy as np
import os

class file_read :
	def __init__(self) :
		self.path = '/'
		self.file_name = os.listdir(self.path)
		print(self.path)

	def read_file() :
		for file in self.file_name :
			os.rename(self.path + '/' + file + '.txt')

if __name__ == "__main__" :
	temp = file_read()
	file_read.read_file('wiki_00')