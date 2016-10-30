from vertex import vertex;
class graph:
	list=[]
	def __init__(self,n):
		for i in range(0,n):
			self.list.append([]);
	def insert(self,u,v,w):
		vert=vertex();
		vert.id=v
		vert.parentId=u
		vert.distance=w
		vert.position=0
		self.list[u-1].append(vert)