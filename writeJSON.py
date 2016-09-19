import pandas as pd
import json
import pdb



#build JSON data in format that is appropriate for this d3 visualization.
def writeJson(df):

	data = dict()
	links = list()
	groupList = list()
	size = df.shape[0]
	for i in range(size):
		groupList.append({"group" : i, "name": df.columns[i]})

		for j in range(i+1, size):

			d1 = dict()
			d2 = dict()
			d1["source"] = i
			d1["target"] = j
			d1["value"] = df.iloc[i,j]
			d2["source"] = j
			d2["target"] = i
			if(df.iloc[i,j] == 3):
				d2["value"] = 2
			elif ((df.iloc[i,j] == 2)):
				d2["value"] = 3
			else:
				d2["value"] = df.iloc[i,j]
			links.append(d1)
			links.append(d2)

	data["links"] = links
	data["nodes"] = groupList

	j = json.dumps(data)

	return j