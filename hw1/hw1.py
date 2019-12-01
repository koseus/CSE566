import numpy as np

f = open("input.txt", "r")

size = int(f.readline())
# print(size)

data = []

for i in range(size):
	line = f.readline()
	# print(line)
	instance = []
	for l in line.split():
		# print(l)
		instance.append(float(l))

		# print(instance)
	data.append(instance)


data = np.asarray(data, dtype=np.float32)

# distinguish negative items from positive ones. We will use positives to compute S, and negatives to compute G.
negative = data[0:10]
positive = data[10:15]

# print(negative)
# print(positive)


##### Compute S #####

# Initial rectangle is equal to the first item
S_minX = positive[0][0]
S_maxX = positive[0][0]
S_minY = positive[0][1]
S_maxY = positive[0][1]

for p in positive:
	if(S_minX > p[0]):
		S_minX = p[0]

	if(S_maxX < p[0]):
		S_maxX = p[0]

	if(S_minY > p[1]):
		S_minY = p[1]

	if(S_maxY < p[1]):
		S_maxY = p[1]

print("Most specific hypothesis is (" + str(S_minX) + ", " + str(S_minY) + ") (" + str(S_maxX) + ", " + str(S_maxY) + ")")

##### Compute G #####
smallX = []
largeX = []
smallY = []
largeY = []

for n in negative:
	if(n[0] < S_minX):
		smallX.append(n[0])
	
	if(n[0] > S_maxX):
		largeX.append(n[0])
	
	if(n[1] < S_minY):
		smallY.append(n[1])
	
	if(n[1] > S_maxY):
		largeY.append(n[1])


# Find the largest X smaller than S_minX
max = 0
for s in smallX:
	if(s > max):
		max = s

G_minX = max

# Find the largest Y smaller than S_minY
max = 0
for s in smallY:
	if(s > max):
		max = s

G_minY = max

# Find the smallest X larger than S_maxX
min = 10
for l in largeX:
	if(l < min):
		min = l

G_maxX = min

# Find the smallest Y larger than S_maxY
min = 10
for l in largeY:
	if(l < min):
		min = l

G_maxY = min

# Squeeze the rectangle by 1 quantum from all sides so that the border does not contain any negatives
G_minX = round(G_minX + 0.05, 2)
G_maxX = round(G_maxX - 0.05, 2)
G_minY = round(G_minY + 0.05, 2)
G_maxY = round(G_maxY - 0.05, 2)

print("Most general hypothesis is (" + str(G_minX) + ", " + str(G_minY) + ") (" + str(G_maxX) + ", " + str(G_maxY) + ")")

