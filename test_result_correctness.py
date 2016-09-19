from create_matrix import write_array
import pdb


#will create a super simple data set, whose expected result I know beforehand. just to test algorithm correctness.


collection = list()

set_one = ['110.111.111.222/32','110.111.111.223/32']
collection.append(set_one)

#set two should contain set one, because the subnet includes only the first 3 bytes.
set_two= ['110.111.111.222/24', '110.111.111.223/24', '110.111.111.224/24']
collection.append(set_two)

#set three should be contained in set_two. it should also intersect with set_one
set_three = ['110.111.111.223/32', '110.111.111.224/32', '110.111.111.224/32']
collection.append(set_three)

#set_four and set_five are identical, just with the orders switched. to see if equality works well.
#they each are disjoint with set_three, set_two and set_one
set_four = [ '100.000.000.001/32', '100.000.000.002/32','100.000.000.003/32']
set_five = [ '100.000.000.003/32','100.000.000.001/32','100.000.000.002/32']
collection.append(set_four)
collection.append(set_five)

#finally, make one lone set to test disjoint once more. this will be disjoint with set_five, set_four, set_three, set_two, and set_one
set_six = ['123.132.131.113/32']
collection.append(set_six)


#in all, we expect: 11 disjoint, 1 intersection, 1 equality, a total of 2 sets included in others (but not equal), and one equality.

write_array(collection, False)

#which is indeed the result. 