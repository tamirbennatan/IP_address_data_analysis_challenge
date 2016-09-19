In January of 2016 I completed a small data analysis/coding challenge for an internship application. I was given one week to find a method to build a method to analyze the relationship of sets of IP addresses in [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing), and to suggest a way to visualize my results. I thought it would be cool to share my work.

CIDR notation is similar to IPv4 notation, except that it is terminated with a "subnet mask" after a backslash `/`. This subnet mask represents the number of leading bits in the network mask. 

For example, 192.168.100.14/24 represents the IPv4 address 192.168.100.14 and its associated routing prefix 192.168.100.0, or equivalently, its subnet mask 255.255.255.0, which has 24 leading 1-bits (source - [wikipedia](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation))

In this way each IP address in CIDR notation is really _a set of IP addresses in IPv4 notation._ The set of IP addresses `192.168.100.14/30` would be contained in the IP address `192.168.100.14/24` because all the addresses in the former are included in the set with prefix `192.168.100.0`. 

I decided to create a co-occurence matrix using D3.js. This code is modified [from the work of Mike Bostock](http://bost.ocks.org/mike/miserables/), creator of D3.js. 


![](https://github.com/tamirbennatan/IP_adress_data_analysis_challenge/blob/master/image.gif)

I encourage you to download this code and play around with my work. To do so:

1. Download this repository.
2. Open the 'index.html' file in a browser. There you will see a visualization built from my synthetic data, and a description of my work and reasoning.
3. To run the scripts that create the synthetic data I use and analyze it, you will need to install the `numpy`, `pandas`  and `nataddr` libraries. To do so using [pip](https://pip.pypa.io/en/stable/):
```
pip install numpy
pip install pandas
pip install netaddr
```
- To run the algorithm, enter the 'create_matrix.py' file and go to line 82. There is a call to the method 'write_array([list], [boolean]).' This method will create a sample data set and manipulate it in a Pandas DataFrame. To print and return a simple dictionary within the counts of each interaction (inclusion, intersection, etc), set the second argument to 'False.' To build, print and return JSON data for visualization, set the second argument to 'True.'
- To see how I built my test data, see ‘test_data.py’. I also discuss this in ‘index.html’.

