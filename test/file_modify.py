import os
import codecs

path = './text'
path_list = []
save_path = './text_modi/'

def get_file():
	global path_list, path

	for directory in os.listdir(path) :
		for file_name in os.listdir(path + '/'+ directory) :
			path_list.append(path+'/'+directory+'/'+file_name)

if __name__ == '__main__' :
	get_file()

	for file in path_list :
		file = codecs.open(file_path, 'r', 'utf-8')

		text = ''

		while True :
			line = file.readline()

			if not line :
				break

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
