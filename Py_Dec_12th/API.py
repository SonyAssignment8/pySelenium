import requests
r = requests.get("https://imgs.xkcd.com/comics/python.png")
print(r)
print(r.status_code)
f = open("E:\Python\\sample.png","wb")
f.write(r.content)
print(r.content)
f.close()
f = open("E:\Python\\sample.txt","wb")
f.write(r.content)
print(r.content)
f.close()