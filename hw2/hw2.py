import numpy as np
import math

def variance(values):
	avg = average(values)
	var = 0.0

	for v in values:
		var = var + pow((v[0] - avg), 2)

	return round(var, 2)


def average(values):
	sum = 0.0
	count = 0

	for v in values:
		sum = sum + v[0]
		count = count + 1

	return round(sum / count, 2)


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
negative = data[0:5]
positive = data[5:10]


mean = [average(negative), average(positive)]
var = [variance(negative), variance(positive)]
dev = [math.sqrt(var[0]), math.sqrt(var[1])]

# print(mean)
# print(var)
# print(dev)

g = (mean[0] + mean[1]) / 2
print("Discriminant value is: " + str(round(g, 2)))

print("Enter an example value to test: ")
instance = float(input())

if(mean[0] < mean[1]):
	if(instance < g):
		print("Class is 0")
	else:
		print("Class is 1")
else:
	if(instance < g):
		print("Class is 1")
	else:
		print("Class is 0")


# g = []
# g.append(0 - 0.5 * math.log(2 * math.pi) - math.log(dev[0]) - math.pow(instance - mean[0], 2) / (2 * math.pow(var[0], 2)))
# g.append(0 - 0.5 * math.log(2 * math.pi) - math.log(dev[1]) - math.pow(instance - mean[1], 2) / (2 * math.pow(var[1], 2)))


# print("g[0] = " + str(g[0]))
# print("g[1] = " + str(g[1]))


# if g[0] < g[1]:
# 	print("Class is 0")
# else:
# 	print("Class is 1")




