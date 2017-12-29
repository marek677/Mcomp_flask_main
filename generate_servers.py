import json
import math
import random

nodes = [
]

edges = [
	{"source":"srv1","target":"srv0","id":"conn00"}
]

data = {
"edges": edges,
"nodes": nodes
}
# Generate nodes
n_nodes = 10
for i in xrange(0,n_nodes,1):
	x = math.sin(float(i)*2/(n_nodes)*math.pi)*100
	y = math.cos(float(i)*2/(n_nodes)*math.pi)*100
	nodes.append(
		{"label":"Server_%i"%i,"x":x,"y":y,"id":"srv%i"%i,"color":"rgb(%i,%i,%i)"%(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)),"size":8.540210723876953},
	)
	print "Generating node %i" % i 
#generate edges
for n1 in xrange(len(nodes)):
	for n2 in xrange(n1,len(nodes),1):
		#if(random.randint(0, 100) < 30) :
		edges.append(
				{"source":"srv%i"%n1,"target":"srv%i"%n2,"id":"conn%i_%i"%(n1,n2)}
			)
		
with open('servers.json', 'w') as outfile:
    json.dump(data, outfile)