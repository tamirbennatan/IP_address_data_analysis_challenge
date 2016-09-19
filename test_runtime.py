import time
from test_data import synthetic_data, random_data, symmetric_data, runtime_test_data
from create_matrix import write_array





#test how long it takes to make a collection of 25 sets, each with 50 elements, 
# and then how long it takes to analyze it and return a frequency matrix.

#set the start subnet, and the end subnet.
subnet_start = 0
subnet_end = 16



start_time = time.time()
small_data = runtime_test_data(25, subnet_start, subnet_end)
print(" takes  %s seconds " % (time.time() - start_time) + "to build a collection of 25 sets")
start_time = time.time()
write_array(small_data,False)
print(" and  %s seconds " % (time.time() - start_time) + "to analyze it and return a matrix.")



#now, repeat with a collection of 250 sets, each with 50 elements
start_time = time.time()
medium_data = runtime_test_data(250,subnet_start,subnet_end)
print(" takes  %s seconds " % (time.time() - start_time) + "to build a collection of 250 sets")
start_time = time.time()
write_array(medium_data,False)
print(" and  %s seconds " % (time.time() - start_time) + "to analyze it and return a matrix.")

#finally, repeat with a collection of 1000 sets, each with 50 elements
start_time = time.time()
big_data = runtime_test_data(1000,subnet_start,subnet_end)
print(" takes  %s seconds " % (time.time() - start_time) + "to build a collection of 1000 sets")
start_time = time.time()
write_array(big_data,False)
print(" and  %s seconds " % (time.time() - start_time) + "to analyze it and return a matrix.")