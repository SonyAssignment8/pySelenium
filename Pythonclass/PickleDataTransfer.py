import pickle
# f= open("pickledata.pkl","wb")
# data=['hi','hello','how']
# pickle.dump(data,f)
# print("successfully written..")
f= open("pickledata.pkl","rb")
data=f.read()
print(pickle.loads(data))
print("data read successfully...")
