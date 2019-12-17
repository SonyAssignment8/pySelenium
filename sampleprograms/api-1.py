import requests
r=requests.get("https://img.xkcd.com/comics/python.png")
print(r)
print(r.status_code)
f=open("C:\\oar-flask\\sample.png",'wb')
f.write((r.content))
print(r.content)
f.close()