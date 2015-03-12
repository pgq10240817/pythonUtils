#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
print sys.getdefaultencoding()

import os
path = './'
gloablCount=1


def getAllFilesInPath(path):
	absPath = os.path.abspath(path)
	L = []
	print absPath
	for parent,direction,files in os.walk(absPath):
			for file in files:
				L.append(parent+os.sep+file)
	return L
def operateAllFilesByPath(fun,path):
	absPath = os.path.abspath(path)
	print absPath
	for parent,direction,files in os.walk(absPath):
			for file in files:
				fun(parent+os.sep+file)
def printFilsPath(file):
	print 'file is -->'+file
def outFile(file):
	input = open(file,'rb')
	lines = input.readlines()
	input.close()
	import os
	global gloablCount
	for line in lines:
		print line
		if(line.find('instanceof')>0 and (line.find('!=null')>0 or line.find('!= null')>0 )):
			print '%d -- %s' % (gloablCount,line)
			gloablCount = gloablCount + 1
	
if __name__ == '__main__':
	import sys
	currentPath = sys.path[0] 
	print 'your CurrentPath is ---> '+currentPath
	path =raw_input('please enter your path : if default is current path \'%s\' '%(currentPath))
	path = path.strip()
	if len(path)==0:
		path = currentPath
	else:
		print '**********'
	operateAllFilesByPath(printFilsPath,path)
	#getAllFilesInPath('G:\\test')