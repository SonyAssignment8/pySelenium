#8.How to store dictionary values in a file?

# dict values into txt file
dict = {'Python' : '.py', 'C++' : '.cpp', 'Java' : '.java'}
f = open("f2.txt","w")
f.write( str(dict) )
f.close()

# # dict values into json file
# import json
# dict = {'Python' : '.py', 'C++' : '.cpp', 'Java' : '.java'}
# json = json.dumps(dict)
# f = open("dict.json","w")
# f.write(json)
# f.close()
#
# # dict values into pickle file
# import pickle
# dict = {'Python' : '.py', 'C++' : '.cpp', 'Java' : '.java'}
# f = open("file.pkl","wb")
# pickle.dump(dict,f)
# f.close()

# # dict values into csv file
# import csv
# dict = {'Python' : '.py', 'C++' : '.cpp', 'Java' : '.java'}
# w = csv.writer(open("output.csv", "w"))
# for key, val in dict.items():
#     w.writerow([key, val])