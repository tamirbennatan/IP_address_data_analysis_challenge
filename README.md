Instructions for use. 

Please open the 'index.html' file in a browser. There you will see a visualization built from my synthetic data, and a description of my work and reasoning.


This folder contains five python files and an HTML document.
A pdf copy of the challenge description can also be found in the main directory.

To run this application, you will need to install the pandas, numpy, and netaddr libraries. You can do so using pip in your command line with the following commands:
‘’’
pip install numpy
pip install pandas
pip install netaddr
‘’’


To run the algorithm, enter the 'create_matrix.py' file and go to line 82. There is a call to the method 'write_array([list], [boolean]).' This method will create a sample data set and manipulate it in a Pandas DataFrame. To print and return a simple dictionary within the counts of each interaction (inclusion, intersection, etc), set the second argument to 'False.' To build, print and return JSON data for visualization, set the second argument to 'True.'

To see how I built my test data, see ‘test_data.py’. I also discuss this in ‘index.html’.

I verified my results in a controlled way in ‘test_result_correctness.py’

the ‘test_runtime.py’ file times how long it takes to create sets of different sizes, and how long it takes to analyze them. Setting the parameters ‘subnet_start’ and ‘subnet_end’ will specify to test on addresses with subnets between those two values. This has a profound effect on runtime (see index.html).

Visualization idea and code inspired by the work of Mike Bostock http://bost.ocks.org/mike/miserables/

Thanks, 
-Tamir Bennatan