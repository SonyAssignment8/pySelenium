import json
obj = json.load(open("C:\\Users\\Jyoti\\PycharmProjects\\Selenium\\my_jason.json",'r'))
for i in obj:
    print("Keys present in json file is: ",i)
    print("Values present in json file is: ",obj[i])
