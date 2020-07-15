# -*- coding: utf-8 -*-
#history objects
#Copyright (C) 2020 yamahubuki <itiro.ishino@gmail.com>
#Note: All comments except these top lines will be written in Japanese. 

class History:
	def __init__(self,maxCount=20,allowDuplication=True):
		"""履歴の保持件数、重複を許すか否かを指定"""
		self.maxCount=maxCount
		self.allowDuplication=allowDuplication
		self.cursor=0
		self.lst=[]

	def add(self,item):
		if self.cursor!=len(self.lst)-1:
			self.lst[self.cursor+1:]=[]	#カーソル以降の項目は削除
		if not self.allowDuplication:
			while item in self.lst:
				i=self.lst.index(item)
				del self.lst[i]					#重複要素を削除
		if len(self.lst)==self.maxCount && len(self.lst)>0:		#リストが満杯
			del self.lst[0]						#先頭の要素を削除
		self.lst.append(item)					#末尾に追加
		self.cursor=len(self.lst)-1				#カーソルを末尾へ移動

	def clear(self):
		self.lst.clear()

	def get(self,index):
		try:
			return self.lst[index]
		except:
			return None

	def getPrevious(self):
		if self.cursor>0:
			self.cursor-=1
			return self.get(self.cursor)
		else:
			return None

	def getNext(self):
		if self.cursor<len(self.lst)-1:
			self.cursor+=1
			return self.get(self.cursor)
		else:
			return None

	def getCount(self):
		return len(self.lst)

	def getList(self):
		return self.lst

	def hasNext(self):
		return self.cursor<len(self.lst)-1

	def hasPrevious(self):
		return self.cursor>0

	def isEmpty(self):
		return len(self.lst)==0
