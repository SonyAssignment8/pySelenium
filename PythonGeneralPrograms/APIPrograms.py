import requests
import jsons
parm={"page":2,"count":4}
r=requests.get("https://imgs.xkcd.com/comics/timeline_of_the_universe.png")
print(r)
print(r.status_code)
f=open("J:\sample1.png","wb")
f.write(r.content)
f.close()