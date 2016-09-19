
import random
import pdb

#for the follwing functions, 'write_json' is a boolean. if True, will write JSON data for visualizations. If 'False,'
# will return a simple dictionary indicating the frequency of each type of interaction between sets: disjoint, intersection, encapsulation, equality.


def synthetic_data():
	random.seed(100)

	collection = list()

	#first, make 5 sets that are extremely unlikely to intersect: Subnet /32. Useful for controling overlap.
	for i in range(5):
		eachSet = list()
		for j in range(50):
			eachElement= '' + str(random.randint(0,255)) +'.'+str(random.randint(0,255)) +'.'+ str(random.randint(0,255)) +'.'+str(random.randint(0,255)) +'/' + str(32) 
			eachSet.append(eachElement)
		collection.append(eachSet)
	#next, make 20 sets that progressively overlap. Do this by taking the existing 5 sets, and adding an identical set only with subnet to /24, /16, /8, /0

	for i in range(5):
		startSet = collection[i][:]
		subnet24 = list()
		subnet16 = list()
		subnet8 = list()
		subnet0 = list()
		for each in startSet:
			subnet24.append(each.replace('/32', '/24'))
			subnet16.append(each.replace('/32', '/16'))
			subnet8.append(each.replace('/32', '/8'))
			subnet0.append(each.replace('/32', '/0'))
		collection.append(subnet24)
		collection.append(subnet16)
		collection.append(subnet8)
		collection.append(subnet0)
	#test whether the is equal' checks work regardless of set content order. repeat first 5, but shuffle contents.
	#recall: the first five sets are extemely unlikely to any other sets otherwise. 
	for i in range(5):
		setCopy = collection[i][:]
		random.shuffle(setCopy)
		collection.append(setCopy)
	#add five sets that are identical to the first, with one more element. This is to test the 'contains' check.
	for i in range(5):
		eachSet = collection[i][:]
		eachSet.append('' + str(random.randint(0,255)) +'.'+str(random.randint(0,255)) +'.'+ str(random.randint(0,255)) +'.'+str(random.randint(0,255)) +'/' + str(32) )
		collection.append(eachSet)

	#add five sets where I remove an element and insert a new random one. To test intersection. 
	for i in range(5):
		eachSet = collection[i][:]
		eachSet[i] ='' + str(random.randint(0,255)) +'.'+str(random.randint(0,255)) +'.'+ str(random.randint(0,255)) +'.'+str(random.randint(0,255)) +'/' + str(32)
		collection.append(eachSet)

	#add five sets where I remove an element from the first five, to check containment
	for i in range(5):
		eachSet = collection[i][:]
		del eachSet[random.randint(0,len(eachSet)-1)]
		collection.append(eachSet)
	#add five sets identical to a previous set, with an aditional random element, and delete one. to check inersection
	for i in range(40, 45):
		eachSet = collection[i][:]
		eachSet.append('' + str(random.randint(0,255)) +'.'+str(random.randint(0,255)) +'.'+ str(random.randint(0,255)) +'.'+str(random.randint(0,255)) +'/' + str(32) )
 		del eachSet[random.randint(0,len(eachSet)-1)]
 		collection.append(eachSet)
	return collection


#random IP adress data, including random subnets.
def random_data():
	random.seed(100)

	collection = list()
	for i in range(50):
		eachSet = list()
		for j in range(random.randint(1,15)):
			eachSet.append('' + str(random.randint(0,255)) +'.'+str(random.randint(0,255)) +'.'+ str(random.randint(0,255)) +'.'+str(random.randint(0,255)) +'/' + str(random.randint(0,32) ))
		collection.append(eachSet)

	return collection

def symmetric_data():
	random.seed(100)
	collection = list()
	for i in range(25):
		eachSet = list()
		for j in range(random.randint(2,6)):
			eachSet.append('' + str(random.randint(0,150)) +'.'+str(random.randint(0,150)) +'.'+ str(random.randint(0,150)) +'.'+str(random.randint(0,150)) +'/' + str(random.randint(8,32) ))
		collection.append(eachSet)
		secondSet = list()
		# overlap will create inclusions
		for j in range(random.randint(2,6)):
			eachSet.append('' + str(random.randint(100,255)) +'.'+str(random.randint(100,255)) +'.'+ str(random.randint(100,255)) +'.'+str(random.randint(100,255)) +'/' + str(random.randint(8,32) ))
		collection.append(secondSet)

	return collection

#used to test runtime. also random data. N number of sets, each with 50 IP addresses
def runtime_test_data(number_of_sets, subnet_start, subnet_end):
	random.seed(100)

	collection = list()
	for i in range(number_of_sets):
		eachSet = list()
		for j in range(50):
			eachSet.append('' + str(random.randint(0,255)) +'.'+str(random.randint(0,255)) +'.'+ str(random.randint(0,255)) +'.'+str(random.randint(0,255)) +'/' + str(random.randint(subnet_start,subnet_end) ))
		collection.append(eachSet)

	return collection





