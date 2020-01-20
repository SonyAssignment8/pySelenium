import pickle
f = open("anu.pkl","wb")
data = [1,2,3,"Hello"]
pickle.dump(data,f)