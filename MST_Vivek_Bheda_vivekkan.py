import math
import sys
node_num=0; #Number of nodes in the Tree/Graph
vertex_vector=[];
array=[0]; #Actual Heap Array

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
#All Operations of the Heap Down Below
def insert(vert):
	array.append(vert)
	array[0] = len(array)-1
	heapify_up(array[0])
	vertex_vector[vert.id-1].position=array[0]
def heapify_up(index):
	while(index>1):
		j=int(index/2)
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
	while(len(array)>1): #Do while heap is not empty
		v=extract_min()
		s.append(v) #Add v to result
		for vert in g.list[v.id-1]: #Visit every edge from node v
			if(int(vert.distance)<int(vertex_vector[vert.id-1].distance)):
				vertex_vector[vert.id-1].distance=vert.distance
				decrease_key(vertex_vector[vert.id-1].position, vert.distance, v.id)
				vertex_vector[vert.id-1].parentId=int(v.id)
	return s

#Set Input Path
input_path="input.txt"
output_path="output.txt"

#Reading Input
lines = [line.rstrip('\n') for line in open(input_path,"r")]
for i in range(0,len(lines)):
	if i==0:
		words = lines[i].split(' ');
		for j in range(0,len(words)):
			if j==0:
				node_num=int(words[j])
		g=graph(int(node_num))
	else:
		#Initializing Input Graph
		words = lines[i].split(' ');
		g.insert(int(words[0]),int(words[1]),int(words[2]))
		g.insert(int(words[1]),int(words[0]),int(words[2]))

#Initializing Vertex Vector
#Vertex Vector stores current position of node in Heap
#Vertex Vector stores current parent of node in Heap
#Vertex Vector stores current distance/weight of node from parent in Heap
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

#Calling MST Prim Algorithm
mst=mst_prim(g,vert)

#Calculating Total Weight/Distance
totalDistance=0
for vert in mst:
	if(vert.id!=0 and vert.parentId!=0):
		if(vert.id > vert.parentId):
			#Swapping parentId & id because algorithm prints them in reverse
			vert.parentId, vert.id = vert.id, vert.parentId
		totalDistance=totalDistance+vert.distance

#Writing output to output file
writer=open(output_path,"w")
writer.write(str(totalDistance))
for vert in mst:
	if(vert.id!=0 and vert.parentId!=0):
		writer.write("\n")
		writer.write(str(vert.id))
		writer.write(" ")
		writer.write(str(vert.parentId))
		writer.write(" ")
		writer.write(str(vert.distance))
