import requests
r=requests.get("https://imgs.xkcd.com/comics/alternative_energy_revolution.jpg")
print(r)
print(r.status_code)
f=open("D:\TestData\\sample.jpg","wb")
f.write(r.content)
print(r.content)
f.close()