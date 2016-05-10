import math
import random
import numpy
from numpy import *

def snn_response(data, w, h, t, sigma):
	import random
	res = [[0 for x in xrange(w)] for x in xrange(h)]
	for x in xrange(h):
		for y in xrange(w):
			p = data[x][y]
			formula = t / (1 + math.exp( sigma  * (128 - p) ))
			res[x][y] = formula
	# math.exp(x)
	return res


# formula V = Vo * e ^ (-t/T)
def weight(x1,y1,x,y):
	w = 10*math.exp(- (  ( math.pow((x1-x),2)+math.pow((y1-y),2) + math.pow(pixel[x1][y1]-pixel[x][y],2 )/d  ) ) )
	# print w
	return w

def formula(v, t, T):
	return v * math.exp(-t/T) 


# ============================ LIF Implementation ===============================
def spike(input):
	pre_v = 0
	for x in xrange(100):

		v = input[x] + formula(pre_v, x / 10.0, 20)
		# print 'v : ', v 
		if v >= 1:
			# print "spike : ", x/10.0, v 
			return x
		pre_v = v
	return 120

def response_time(pixel_data_dict):
	b = [0 for x in xrange(101)]
	# for x in a:
	# 	b[x*10] += 0.5 
	# float("{0:.2f}".format(
	for x in sorted(pixel_data_dict):
		val = int(round(x*10))
		# weight = float("{0:.2f}".format(pixel_data_dict[x]))
		weight = pixel_data_dict[x]
		b[val] = b[val] + (0.5*weight)


	index = spike(b)
	return (index/10.0)

# print second_layer
#print ('after:',len(second_layer))
#print ('after:',len(second_layer[0]))
# for x in xrange(h):
# 		for y in xrange(w):
# 			if second_layer[x][y] < numpy.median(second_layer):
# 				second_layer[x][y]=0

# print pixel_mat


