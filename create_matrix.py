# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 18:31:08 2016

@author: timibennatan
"""


from netaddr import *
import pandas as pd
import numpy as np
from writeJSON import writeJson
from test_data import synthetic_data, random_data, symmetric_data

def write_array(data, create_json):

	IPsets = list()
	for eachIPSet in data:
		IPsets.append(IPSet(eachIPSet))

	zeros = np.zeros((len(IPsets), len(IPsets)))
	resultArray = pd.DataFrame(zeros, index = [ 'set' + str(i) for i in range(1, len(IPsets) + 1)], columns = ['set' + str(i) for i in range(1, len(IPsets) + 1)])

	#this array represents [number disjoint, number intersection, number X in Y, number Y in X, number X = Y]
	count_dict = {"disjoint":0, "intersect":0, "X_in_Y": 0, "Y_in_X":0, "equal":0}

	#each element above the main diagonal represents the relationship between two sets, say Sx and Sy. Each element recieves a score. 

	# a score of 0 means Sx and Sy are disjoint.
	# a score of 1 means Sx and Sy intersect, but one is not contained in the other.
	# a score of 2 means Sx is contained in Sy.
	# a score of 3 means Sy is contained in Sx.
	# a score of 5 means Sx = Sy.

	for i in range(0, len(IPsets)):
		for j in range(i + 1, len(IPsets) ):
			# is the column index, j is the row. 
			if(IPsets[i].issubset(IPsets[j])):
				resultArray.ix[i,j] += 2
			if(IPsets[j].issubset(IPsets[i])):
				resultArray.ix[i,j]+=3
			if(resultArray.ix[i,j] == 0 ):
				if( not IPsets[i].isdisjoint(IPsets[j])):
					resultArray.ix[i,j] =1
			#only keep track of the number of occurences if the user wants you to. 
			if(not create_json):
				#check in order that seem most likely, to save checks. this is completely dependent  on the data. 
				if(resultArray.ix[i,j] == 1):
					count_dict['intersect']+=1
					continue
				elif (resultArray.ix[i,j] == 2):
					count_dict['X_in_Y']+=1
					continue
				elif (resultArray.ix[i,j] == 3):
					count_dict['Y_in_X']+=1
					continue
				elif (resultArray.ix[i,j] == 5):
					count_dict['equal']+=1
					continue
				elif(resultArray.ix[i,j] == 0):
					count_dict['disjoint']+= 1



	if(create_json):
		json_data = writeJson(resultArray)
		print json_data
		return json_data

	#if only want dictionary of counts, and not to create JSON (which is costly in terms of time)
	else:

		print count_dict
		return count_dict



# the commented out example first creates the test data, then runs the above algorithm on it.
#takes two parameters: the first is the data as an embedded list of IPSet objects,
#and the second is a boolean. if set to 'True,' will wirte JSON data for visualizations.
#if 'False,' will return a dictionary with the frequency of each classification. 


#write_array(symmetric_data(), False)





