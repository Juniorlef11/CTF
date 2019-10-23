import urllib.request
import urllib.parse

phpSessionId = ""
r = urllib.request.Request("levels/coding/2",headers={'Cookie':"PHPSESSID="+phpSessionId})
dat = urllib.request.urlopen(r).read()

first_split = dat.decode().split("<textarea>")
second_split = first_split[1].split("</textarea>")
res = second_split[0].split(", ")
print(res)
res1 = [x.split(",") for x in res]
result = [j for i in res1 for j in i]

total = 94

for i in range(len(result)):
    if result[i] == '':
        result[i] = '32'
mylist = list(map(int, result))
for i in range(len(mylist)):
    if mylist[i] == ' ':
        mylist[i] = ' '
    else:
        mylist[i] = mylist[i] - 32
        mylist[i] = total - mylist[i]
        mylist[i] = mylist[i] + 32
        mylist[i] = chr(mylist[i])
for i in range(len(mylist)):
    if mylist[i] == '~':
        mylist[i] = ' '
mylist = ''.join(mylist)
print(mylist)

post = urllib.parse.urlencode({'answer':mylist}).encode()
url = urllib.request.Request("/levels/coding/2",post,headers={'Cookie':"PHPSESSID="+phpSessionId})
data = urllib.request.urlopen(url)















