import math
import sys
node_num=0;
edge_num=0;
vertex_vector=[];
array=[0];
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
class vertex:
	position=0;
	parentId=0;
	distance=9999999;
	id=0;
	def getDistance(self):
		return self.distance
def insert(vert):
	array.append(vert)
	array[0] = len(array)-1
	heapify_up(array[0])
	vertex_vector[vert.id-1].position=array[0]
def heapify_up(index):
	while(index>1):
		j=index/2
		if(int(array[j].distance)>int(array[index].distance)):
			vertex_vector[array[index].id-1].position=j
			vertex_vector[array[j].id-1].position=index
			temp = array[index]
			array[index] = array[j]
			array[j]=temp
			index=j
		else:
			break;
def extract_min():
	vertex_vector[array[1].id-1].position=0
	lastIndex = array[0]
	vertex_vector[array[lastIndex].id-1].position=1
	ret = array[1]
	array[1] = array[lastIndex]
	array[0] = array[0]-1
	if array[0]>1:
		heapify_down(1)
	del array[-1]
	return ret
def decrease_key(heapIndex, updatedDistance,parentId):
	if(heapIndex>0):
		array[heapIndex].distance=updatedDistance;
		array[heapIndex].parentId=parentId;
		heapify_up(heapIndex);
def heapify_down(index):
	while (2*index<=array[0]):
		if(2*index==array[0]) or (array[2*index].distance<array[2*index+1].distance):
			j=2*index
		else:
			j=2*index+1
		if array[j].distance<array[index].distance:
			vertex_vector[array[index].id-1].position=j
			vertex_vector[array[j].id-1].position=index
			temp = array[index]
			array[index] = array[j]
			array[j]=temp
			index=j
		else:
			break;

#Prims Algorithm MST
def mst_prim(g,w):
	insert(w)	#insert starting node onto heap
	s=[];	#init empty result list
	for i in range(len(vertex_vector)):
		if(i!=w.id-1):
			vert=vertex()
			vert.id=i+1
			vert.position=0;
			vert.distance=999999;
			vert.parentId=0;
			insert(vert) #insert other nodes onto heap
	while(len(array)>1):
		v=extract_min()
		s.append(v)
		for vert in g.list[v.id-1]:
			if(int(vert.distance)<int(vertex_vector[vert.id-1].distance)):
				vertex_vector[vert.id-1].distance=vert.distance
				decrease_key(vertex_vector[vert.id-1].position, vert.distance, v.id)
				vertex_vector[vert.id-1].parentId=int(v.id)
	return s
lines = raw_input();
lines=lines.split(" ");
node_num=int(lines[0]);
edge_num=int(lines[1])
g = graph(node_num)
for i in range(0,int(lines[1])):
	words=raw_input();
	words = words.split(' ');
	g.insert(int(words[0]),int(words[1]),int(words[2]))
	g.insert(int(words[1]),int(words[0]),int(words[2]))
for i in range(0,node_num):
	vert = vertex()
	vert.id=i+1;
	vert.position=0;
	vert.distance=999999;
	vert.parentId=0;
	vertex_vector.append(vert)
vert= vertex()
vert.id=1
vert.position=0;
vert.distance=999999;
vert.parentId=0;
mst=mst_prim(g,vert)
totalDistance=0
for vert in mst:
	if(vert.id!=0 and vert.parentId!=0):
		totalDistance=totalDistance+vert.distance
print totalDistance