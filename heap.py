class heap:
	array=[0];
	def insert(self,key_value):
		self.array.append(key_value)
		self.array[0] = len(self.array)-1
		self.heapify_up(self.array[0])
	def heapify_up(self,index):
		while(index>1):
			j=index/2
			if(int(self.array[j].distance)>int(self.array[index].distance)):
				temp = self.array[index]
				self.array[index] = self.array[j]
				self.array[j]=temp
				index=j
			else:
				break;
	def extract_min(self):
		lastIndex = self.array[0]
		ret = self.array[1]
		self.array[1] = self.array[lastIndex]
		self.array[0] = self.array[0]-1
		if self.array[0]>1:
			self.heapify_down(1)
		del self.array[-1]
		return ret
	def heapify_down(self,index):
		while (2*index<=self.array[0]):
			if(2*index==self.array[0]) or (self.array[2*index].distance<self.array[2*index+1].distance):
				j=2*index
			else:
				j=2*index+1
			if self.array[j].distance<self.array[index].distance:
				temp = self.array[index]
				self.array[index] = self.array[j]
				self.array[j]=temp
				index=j
			else:
				break;