from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# assignment 1

url1 = "http://py4e-data.dr-chuck.net/comments_1152759.html"
html = urlopen(url1, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
# get all of the span tags
tags = soup('span')
count = 0
sum = 0
for tag in tags:
   count += 1
   sum += int(tag.contents[0])

print("count = ", count)
print("sum = ", sum)

# assignment 2

hops = int(input('count= '))
pos = int(input('pos= '))
url2 = "http://py4e-data.dr-chuck.net/known_by_Petra.html"


for hop in range(hops):
    html = urlopen(url2, context=ctx).read()
    soup2 = BeautifulSoup(html, "html.parser")
    # get all of the anchor tags
    tags2 = soup2('a')
    url2 = tags2[pos-1].get('href', None)
print(tags2[pos-1].get('href', None))



